# coding: utf-8

import codecs
import re
import json
from budget2013_common import *


class Budget2013_36(object):
	def __init__(self):
		self._caption = None
		self._items = []
	
	@property
	def caption(self):
		return self._caption
	@caption.setter
	def caption(self, value):
		self._caption = value
	
	@property
	def items(self):
		return self._items
	@items.setter
	def items(self, value):
		self._items = value

class JsonEncoder_Budget2013_36_Item(json.JSONEncoder):
	def default(self, o):
		return {
			"name": o["name"],
			"value2014": o["value2014"],
			"value2015": o["value2015"],
			"children": [self.default(child) for child in o["children"]]
		}

class JsonEncoder_Budget2013_36(json.JSONEncoder):
	def default(self, o):
		item_encoder = JsonEncoder_Budget2013_36_Item()
		return {
			"caption": o.caption,
			"items": [item_encoder.default(item) for item in o.items]
		}

def check_item(item):
	if item["children"]:
		total2014 = 0
		total2015 = 0
		for child in item["children"]:
			total2014 += child["value2014"]
			total2015 += child["value2015"]
		if not numbers_equal(total2014, item["value2014"]):
			print item["name"], total2014, item["value2014"]
			raise Exception(u"Сумма за 2014 год не сходится.")
		if not numbers_equal(total2015, item["value2015"]):
			print item["name"], total2015, item["value2015"]
			raise Exception(u"Сумма за 2015 год не сходится.")
		for child in item["children"]:
			check_item(child)

def check_document(document):
	for item in document.items:
		check_item(item)

def get_document(input_file_name):
	with codecs.open(input_file_name, "r", encoding = "utf-8-sig") as input_file:
		input_data = input_file.readlines()
		
		document = Budget2013_36()
		
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

		headers = input_data[line_index]
		line_index += 1
		
		#tables
		last_parent = None
		while line_index < len(input_data):
			data_line = input_data[line_index].rstrip()
			line_index += 1
			if re.compile(u"^\\t+в том числе:?$").match(data_line):
				continue
			r = re.compile("\\s+(\\d+(?: \\d{3})*(?:,\\d+)?) (\\d+(?: \\d{3})*(?:,\\d+)?)$")
			m = r.search(data_line)
			value2014 = m.group(1)
			value2015 = m.group(2)
			name = data_line[:len(data_line) - len(value2014) - 1 - len(value2015)]
			is_child = name.startswith("\t")
			name = name.strip()
			item = {"name": name, "value2014": float(value2014.replace(',', '.').replace(' ', '')), "value2015": float(value2015.replace(',', '.').replace(' ', '')), "children": [], "parent": None}
			if not is_child:
				document.items.append(item)
				last_parent = item
			else:
				last_parent["children"].append(item)
				item["parent"] = last_parent
		
		check_document(document)
		
		return document

def write_table_item(output_file, item, level = 0):
	output_file.write("\t" * level + item["name"] + " " + unicode(item["value2014"]) + " " + unicode(item["value2015"]) + "\r\n")
	if item["children"]:
		for child in item["children"]:
			write_table_item(output_file, child, level + 1)

def do_write_text_document(output_file, document):
	output_file.write(document.caption + "\r\n\r\n")
	for item in document.items:
		write_table_item(output_file, item)
		output_file.write("\r\n")


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
		write_json_document(document, output_json_file_name, JsonEncoder_Budget2013_36)
	if output_json_pretty_file_name:
		write_json_pretty_document(document, output_json_pretty_file_name, JsonEncoder_Budget2013_36)
