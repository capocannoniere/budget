# coding: utf-8

import codecs
import re
import json
from budget2013_common import *


class Budget2013_0(object):
	def __init__(self):
		self._text = []
		self._headers = []
		self._items = []
		self._footers = []
	
	@property
	def text(self):
		return self._text
	@text.setter
	def text(self, value):
		self._text = value
	
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
	
	@property
	def footers(self):
		return self._footers
	@footers.setter
	def footers(self, value):
		self._footers = value

class JsonEncoder_Budget2013_0_Item(json.JSONEncoder):
	def default(self, o):
		return {
			"text": o["text"],
			"children": [self.default(child) for child in o["children"]]
		}

class JsonEncoder_Budget2013_0(json.JSONEncoder):
	def default(self, o):
		item_encoder = JsonEncoder_Budget2013_0_Item()
		return {
			"text": o.text,
			"headers": o.headers,
			"items": [item_encoder.default(item) for item in o.items],
			"footers": o.footers
		}
		
def create_item(line):
	return {
		"text": [line],
		"children": [],
		"parent": None
	}

def process_lines(lines, document):
	last_level1 = last_level2 = last_level3 = last_item = None
	for line in lines:
		if re.compile(u"^Статья \\d+").match(line):
			item = create_item(line)
			document.items.append(item)
			last_level1 = item
			last_item = item
		elif re.compile(u"^\\d+\\.").match(line):
			item = create_item(line)
			item["parent"] = last_level1
			last_level1["children"].append(item)
			last_level2 = item
			last_item = item
		elif re.compile(u"^\\d+\\)").match(line):
			item = create_item(line)
			item["parent"] = last_level2
			last_level2["children"].append(item)
			last_level3 = item
			last_item = item
		else:
			last_item["text"].append(line)

def get_document(input_file_name):
	with codecs.open(input_file_name, "r", encoding = "utf-8-sig") as input_file:
		input_data = input_file.readlines()
		
		document = Budget2013_0()
		document.text = input_data
		document.headers = input_data[:8]
		
		line_index = 9
		lines = []
		while line_index < len(input_data):
			line = input_data[line_index].strip()
			line_index += 1
			if not line:
				break
			lines.append(line)
		process_lines(lines, document)

		document.footers = input_data[line_index:]
		
		return document
	
def write_text_item(output_file, item, level = 0):
	for line in item["text"]:
		output_file.write("\t" * level + line + "\r\n")
		for child in item["children"]:
			write_text_item(output_file, child, level + 1)

def do_write_text_document(output_file, document):
	output_file.write(u"".join(document.headers) + "\r\n")
	for item in document.items:
		write_text_item(output_file, item)
	output_file.write("\r\n" + u"".join(document.footers))

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
		write_json_document(document, output_json_file_name, JsonEncoder_Budget2013_0)
	if output_json_pretty_file_name:
		write_json_pretty_document(document, output_json_pretty_file_name, JsonEncoder_Budget2013_0)
