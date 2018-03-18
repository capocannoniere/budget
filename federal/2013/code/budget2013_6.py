# coding: utf-8

import codecs
import re
import json
from budget2013_common import *


class Budget2013_6_DataItem(object):
	def __init__(self):
		self._code = None
		self._subcodes = None
		self._parent = None
		self._name = None
		self._children = []
	
	@property
	def code(self):
		return self._code
	@code.setter
	def code(self, value):
		self._code = value
	
	@property
	def subcodes(self):
		return self._subcodes
	@subcodes.setter
	def subcodes(self, value):
		self._subcodes = value
	
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self, value):
		self._name = value
	
	@property
	def parent(self):
		return self._parent
	@parent.setter
	def parent(self, value):
		self._parent = value
	
	@property
	def children(self):
		return self._children

class JsonEncoder_Budget2013_6_DataItem(json.JSONEncoder):
	def default(self, o):
		return {
			"code": o.code,
			"subcodes": o.subcodes,
			"name": o.name,
			"children": [self.default(child) for child in o.children]
		}

class Budget2013_6(object):
	def __init__(self):
		self._caption = None
		self._header = []
		self._data = []
		self._additional_data_caption = None
		self._additional_data = []
	
	@property
	def caption(self):
		return self._caption
	@caption.setter
	def caption(self, value):
		self._caption = value
	
	@property
	def header(self):
		return self._header
	@header.setter
	def header(self, value):
		self._header = value

	@property
	def data(self):
		return self._data
	@data.setter
	def data(self, value):
		self._data = value
	
	@property
	def additional_data_caption(self):
		return self._additional_data_caption
	@additional_data_caption.setter
	def additional_data_caption(self, value):
		self._additional_data_caption = value
	
	@property
	def additional_data(self):
		return self._additional_data
	@additional_data.setter
	def additional_data(self, value):
		self._additional_data = value

class JsonEncoder_Budget2013_6(json.JSONEncoder):
	def default(self, o):
		item_encoder = JsonEncoder_Budget2013_6_DataItem()
		return {
			"caption": o.caption,
			"header": o.header,
			"data": [item_encoder.default(item) for item in o.data],
			"additional_data_caption": o.additional_data_caption,
			"additional_data": [item_encoder.default(item) for item in o.additional_data]
		}

def get_document(input_file_name):
	with codecs.open(input_file_name, "r", encoding = "utf-8") as input_file:
		input_data = input_file.readlines()
		
		document = Budget2013_6()
		
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
		
		# header
		header_line = input_data[line_index].strip()
		line_index += 1
		document.header = header_line.split(";")
		
		# data
		data = []
		data_lines = []
		while line_index < len(input_data):
			data_line = input_data[line_index].strip()
			line_index += 1
			if not data_line:
				break
			m = re.compile("(\\d+)\\s+(.*)").match(data_line)
			if m:
				if data_lines:
					item = join_lines(data_lines)
					data.append(item)
					data_lines = []
				data_lines.append(data_line)
			else:
				data_lines.append(data_line)
		if data_lines:
			item = join_lines(data_lines)
			data.append(item)
			data_lines = []
		for d in data:
			m1 = re.compile("^(\\d{3})\\s+(.*)").match(d)
			m2 = re.compile("^(\\d{3}) (\\d{2} \\d{2} \\d{2} \\d{2} \\d{2} \\d{4} \\d{3})\\s+(.*)").match(d)
			if not m2:
				# министерство
				item = Budget2013_6_DataItem()
				item.code = m1.group(1)
				item.name = m1.group(2)
				document.data.append(item)
			else:
				item = Budget2013_6_DataItem()
				item.code = m2.group(1)
				item.subcodes = m2.group(2)
				item.name = m2.group(3)
				document.data[-1].children.append(item)
		
		# additional caption
		additional_caption_lines = []
		while line_index < len(input_data):
			additional_caption_line = input_data[line_index].strip()
			line_index += 1
			if not additional_caption_line:
				break
			additional_caption_lines.append(additional_caption_line)
		document.additional_data_caption = join_lines(additional_caption_lines)
		
		# additional data
		additional_data = []
		additional_data_lines = []
		while line_index < len(input_data):
			additional_data_line = input_data[line_index].strip()
			line_index += 1
			if not additional_data_line:
				break
			m = re.compile("(\\d+)\\s+(.*)").match(additional_data_line)
			if m:
				if additional_data_lines:
					item = join_lines(additional_data_lines)
					additional_data.append(item)
					additional_data_lines = []
				additional_data_lines.append(additional_data_line)
			else:
				additional_data_lines.append(additional_data_line)
		if additional_data_lines:
			item = join_lines(additional_data_lines)
			additional_data.append(item)
			additional_data_lines = []
		for d in additional_data:
			m = re.compile("^(\\d{2} \\d{2} \\d{2} \\d{2} \\d{2} \\d{4} \\d{3})\\s+(.*)").match(d)
			item = Budget2013_6_DataItem()
			item.subcodes = m.group(1)
			item.name = m.group(2)
			document.additional_data.append(item)
		
		return document

def write_data_item(output_file, item, level = 0):
	output_file.write("\t" * level + (item.code + " " if item.code else "") + (item.subcodes + " " if item.subcodes else "") + item.name + "\r\n")
	for child in item.children:
		write_data_item(output_file, child, level + 1)

def do_write_text_document(output_file, document):
	output_file.write(document.caption + "\r\n")
	output_file.write(u" ".join(document.header) + "\r\n")
	for item in document.data:
		write_data_item(output_file, item)
	output_file.write(document.additional_data_caption + "\r\n")
	for item in document.additional_data:
		write_data_item(output_file, item, 1)


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
		write_json_document(document, output_json_file_name, JsonEncoder_Budget2013_6)
	if output_json_pretty_file_name:
		write_json_pretty_document(document, output_json_pretty_file_name, JsonEncoder_Budget2013_6)
