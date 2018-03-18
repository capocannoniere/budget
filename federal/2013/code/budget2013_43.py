# coding: utf-8

import codecs
import re
import pickle
import optparse
from budget2013_common import *


class Budget2013_43_TableItem(object):
	def __init__(self):
		self._name = None
		self._value = None
		self._parent = None
		self._children = []
	
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self, value):
		self._name = value
	
	@property
	def value(self):
		return self._value
	@value.setter
	def value(self, value):
		self._value = value
	
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

class JsonEncoder_Budget2013_43_TableItem(json.JSONEncoder):
	def default(self, o):
		return {
			"name": o.name,
			"value": o.value,
			"children": [self.default(child) for child in o.children]
		}

class Budget2013_43(object):
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

class JsonEncoder_Budget2013_43(json.JSONEncoder):
	def default(self, o):
		item_encoder = JsonEncoder_Budget2013_43_TableItem()
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

	total_value = 0.0
	for child in item.children:
		total_value += child.value
		check_item(child)
	if not numbers_equal(total_value, item.value):
		print item.name, total_value, item.value
		raise Exception(u"Сумма не сходится.")

def check_document(document):
	for item in document.items:
		check_item(item)

def get_document(input_file_name):
	with codecs.open(input_file_name, "r", encoding = "utf-8-sig") as input_file:
		input_data = input_file.readlines()
		
		document = Budget2013_43()
		
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
		document.headers = headers.split(";")
		
		# items
		item_lines = []
		while line_index < len(input_data):
			item_line = input_data[line_index].strip()
			line_index += 1
			if not item_line:
				break
			m = re.compile("((?:- ?)?\\d\\d?\\d?(?: \\d{3})*,\\d+)$").search(item_line)
			if m:
				item_lines.append(item_line[:-len(m.group(1)) - 1].strip())
				item = Budget2013_43_TableItem()
				item.name = join_lines(item_lines)
				item.value = float(m.group(1).replace(",", ".").replace(" ", ""))
				document.items.append(item)
				item_lines = []
			else:
				if item_line != u"в том числе:":
					item_lines.append(item_line)

		correct_items(document)
		check_document(document)
		
		return document

def write_item(output_file, item, level = 0):
	output_file.write("\t" * level + item.name + " " + unicode(item.value) + "\r\n")
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
		write_json_document(document, output_json_file_name, JsonEncoder_Budget2013_43)
	if output_json_pretty_file_name:
		write_json_pretty_document(document, output_json_pretty_file_name, JsonEncoder_Budget2013_43)
