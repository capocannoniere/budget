# coding: utf-8

import codecs
import re
import json
from budget2013_common import *


class Budget2013_44_TableItem(object):
	def __init__(self):
		self._name = None
		self._value2014 = None
		self._value2015 = None
		self._parent = None
		self._children = []
	
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self, value):
		self._name = value
	
	@property
	def value2014(self):
		return self._value2014
	@value2014.setter
	def value2014(self, value):
		self._value2014 = value
	
	@property
	def value2015(self):
		return self._value2015
	@value2015.setter
	def value2015(self, value):
		self._value2015 = value
	
	@property
	def parent(self):
		return self._parent
	@parent.setter
	def parent(self, value):
		self._parent = value
	
	@property
	def children(self):
		return self._children
	@children.setter
	def children(self, value):
		self._children = value

class JsonEncoder_Budget2013_44_TableItem(json.JSONEncoder):
	def default(self, o):
		return {
			"name": o.name,
			"value2014": o.value2014,
			"value2015": o.value2015,
			"children": [self.default(child) for child in o.children]
		}

class Budget2013_44(object):
	def __init__(self):
		self._caption = None
		self._headers = []
		self._items = []
	
	@property
	def caption(self):
		return self._caption
	@caption.setter
	def caption(self, value):
		self._caption = value
	
	@property
	def headers(self):
		return self._headers
	@headers.setter
	def headers(self, value):
		self._headers = value
	
	@property
	def items(self):
		return self._items
	@items.setter
	def items(self, value):
		self._items = value

class JsonEncoder_Budget2013_44(json.JSONEncoder):
	def default(self, o):
		item_encoder = JsonEncoder_Budget2013_44_TableItem()
		return {
			"caption": o.caption,
			"headers": o.headers,
			"items": [item_encoder.default(item) for item in o.items]
		}

def correct_items(document):
	items = document.items[1:]
	document.items = [document.items[0]]
	
	for item in items:
		if item.name == item.name.upper():
			document.items[0].children.append(item)
			item.parent = document.items[0]
			last_level2 = item
		else:
			if item.name[0].istitle():
				last_level2.children.append(item)
				item.parent = last_level2
				last_level3 = item
			else:
				last_level3.children.append(item)
				item.parent = last_level3

def check_item(item):
	if not item.children:
		return

	total_value2014 = 0.0
	total_value2015 = 0.0
	for child in item.children:
		total_value2014 += child.value2014
		total_value2015 += child.value2015
		check_item(child)
	if not numbers_equal(total_value2014, item.value2014):
		print item.name, total_value2014, item.value2014
		raise Exception(u"Сумма за 2014 год не сходится.")
	if not numbers_equal(total_value2015, item.value2015):
		print item.name, total_value2015, item.value2015
		raise Exception(u"Сумма за 2015 год не сходится.")

def check_document(document):
	for item in document.items:
		check_item(item)

def get_document(input_file_name):
	with codecs.open(input_file_name, "r", encoding = "utf-8-sig") as input_file:
		input_data = input_file.readlines()
		
		document = Budget2013_44()
		
		line_index = 0
		
		# caption
		caption_lines = []
		while line_index < len(input_data):
			caption_line = input_data[line_index].strip()
			line_index += 1
			if not caption_line:
				break
			caption_lines.append(caption_line)
		document.caption = join_lines(caption_lines)

		# headers
		headers = input_data[line_index].strip()
		line_index += 1
		headers = headers.split(";")
		document.headers = headers[:-1]
		m = re.compile("(.*):(.*),(.*)").match(headers[-1])
		document.headers.append(m.group(1) + ": " + m.group(2))
		document.headers.append(m.group(1) + ": " + m.group(3))
		
		# items
		item_lines = []
		while line_index < len(input_data):
			item_line = input_data[line_index].strip()
			line_index += 1
			if not item_line:
				break
			re_number = "((?:- ?)?\\d\\d?\\d?(?: \\d{3})*,\\d+)";
			m = re.compile(re_number + " " + re_number + "$").search(item_line)
			if m:
				item_lines.append(item_line[:-len(m.group(1)) - 1 - len(m.group(2))].strip())
				item = Budget2013_44_TableItem()
				item.name = join_lines(item_lines)
				item.value2014 = float(m.group(1).replace(",", ".").replace(" ", ""))
				item.value2015 = float(m.group(2).replace(",", ".").replace(" ", ""))
				document.items.append(item)
				item_lines = []
			else:
				if item_line != u"в том числе:":
					item_lines.append(item_line)

		correct_items(document)
		check_document(document)
		
		return document

def write_item(output_file, item, level = 0):
	output_file.write("\t" * level + item.name + " " + unicode(item.value2014) + " " + unicode(item.value2015) + "\r\n")
	for child in item.children:
		write_item(output_file, child, level + 1)

def do_write_text_document(output_file, document):
	output_file.write(document.caption + "\r\n\r\n")
	
	output_file.write(u" ".join(document.headers) + "\r\n\r\n")
	for item in document.items:
		write_item(output_file, item)


if __name__ == "__main__":
	parser = get_default_argument_parser()
	args = parser.parse_args()
	
	input_file_name = args.input_file_name
	output_pickle_file_name = args.output_pickle_file_name
	output_text_file_name = args.output_text_file_name
	output_json_file_name = args.output_json_file_name
	output_json_pretty_file_name = args.output_json_pretty_file_name
	
	if (not output_pickle_file_name) and (not output_text_file_name) and (not output_json_file_name) and (not output_json_pretty_file_name):
		raise Exception("No output file specified")
	
	document = get_document(input_file_name)
	if output_pickle_file_name:
		write_pickle_document(document, output_pickle_file_name)
	if output_text_file_name:
		write_text_document(document, output_text_file_name, do_write_text_document)
	if output_json_file_name:
		write_json_document(document, output_json_file_name, JsonEncoder_Budget2013_44)
	if output_json_pretty_file_name:
		write_json_pretty_document(document, output_json_pretty_file_name, JsonEncoder_Budget2013_44)
