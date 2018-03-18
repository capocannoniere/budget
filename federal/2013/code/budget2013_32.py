# coding: utf-8

import codecs
import re
import json
from budget2013_common import *


class Budget2013_32_Table(object):
	def __init__(self):
		self._number = None
		self._caption = None
		self._header = []
		self._is_one_sum_column = False
		self._data = []

	@property
	def number(self):
		return self._number
	@number.setter
	def number(self, value):
		self._number = value
	
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
	def is_one_sum_column(self):
		return self._is_one_sum_column
	@is_one_sum_column.setter
	def is_one_sum_column(self, value):
		self._is_one_sum_column = value
	
	@property
	def data(self):
		return self._data
	@data.setter
	def data(self, value):
		self._data = value

class JsonEncoder_Budget2013_32_TableItem1(json.JSONEncoder):
	def default(self, o):
		return {
			"name": o["name"],
			"value": o["value"],
			"children": [self.default(child) for child in o["children"]]
		}

class JsonEncoder_Budget2013_32_TableItem2(json.JSONEncoder):
	def default(self, o):
		return {
			"name": o["name"],
			"value2014": o["value2014"],
			"value2015": o["value2015"],
			"children": [self.default(child) for child in o["children"]]
		}

class JsonEncoder_Budget2013_32_Table(json.JSONEncoder):
	def default(self, o):
		item1_encoder = JsonEncoder_Budget2013_32_TableItem1()
		item2_encoder = JsonEncoder_Budget2013_32_TableItem2()
		if o.is_one_sum_column:
			return {
				"number": o.number,
				"caption": o.caption,
				"header": o.header,
				"is_one_sum_column": o.is_one_sum_column,
				"data": [item1_encoder.default(item) for item in o.data]
			}
		else:
			return {
				"number": o.number,
				"caption": o.caption,
				"header": o.header,
				"is_one_sum_column": o.is_one_sum_column,
				"data": [item2_encoder.default(item) for item in o.data]
			}

class Budget2013_32(object):
	def __init__(self):
		self._tables = []
	
	@property
	def tables(self):
		return self._tables
	@tables.setter
	def tables(self, value):
		self._tables = value

class JsonEncoder_Budget2013_32(json.JSONEncoder):
	def default(self, o):
		table_encoder = JsonEncoder_Budget2013_32_Table()
		return {
			"tables": [table_encoder.default(table) for table in o.tables]
		}

def parse_table_header(header):
	headers = header.split(";")
	if headers[-1].find(":") == -1:
		return (headers, True)
	else:
		last_header = headers[-1]
		headers = headers[:-1]
		last_headers = last_header.split(":")
		for last_headers_year in last_headers[1].split(","):
			headers.append(last_headers[0] + ": " + last_headers_year)
		return (headers, False)

def process_table(table_lines, document):
	table = Budget2013_32_Table()
	
	caption_line = table_lines[0]
	table.number = int(re.compile(u"^Таблица (\\d+)$").match(caption_line).group(1))
	
	line_index = 1
	# caption
	caption_lines = []
	while line_index < len(table_lines):
		caption_line = table_lines[line_index].strip()
		line_index += 1
		if not caption_line:
			break
		caption_lines.append(caption_line)
	table.caption = join_lines(caption_lines)
	
	(table.header, table.is_one_sum_column) = parse_table_header(table_lines[line_index])
	line_index += 1
	
	last_parent = None
	while line_index < len(table_lines):
		table_line = table_lines[line_index]
		line_index += 1
		if re.compile(u"^\\t+в том числе:?$").match(table_line):
			continue
		regexp_value = "\\d+(?: \\d{3})*(?:,\\d+)?"
		if table.is_one_sum_column:
			r = re.compile("\\s+(" + regexp_value + ")$")
			m = r.search(table_line)
			value = m.group(1)
			name = table_line[:len(table_line) - len(value)]
			is_child = name.startswith("\t")
			name = name.strip()
			item = {"name": name, "value": float(value.replace(',', '.').replace(' ', '')), "children": [], "parent": None}
		else:
			r = re.compile("\\s+(" + regexp_value + ") (" + regexp_value + ")$")
			m = r.search(table_line)
			value2014 = m.group(1)
			value2015 = m.group(2)
			name = table_line[:len(table_line) - len(value2014) - 1 - len(value2015)]
			is_child = name.startswith("\t")
			name = name.strip()
			item = {"name": name, "value2014": float(value2014.replace(',', '.').replace(' ', '')), "value2015": float(value2015.replace(',', '.').replace(' ', '')), "children": [], "parent": None}
		if not is_child:
			table.data.append(item)
			last_parent = item
		else:
			last_parent["children"].append(item)
			item["parent"] = last_parent
	
	document.tables.append(table)

def check_item(item, is_one_sum_column):
	if item["children"]:
		if is_one_sum_column:
			total = 0
			for child in item["children"]:
				total += child["value"]
			if not numbers_equal(total, item["value"]):
				print item["name"], total, item["value"]
				raise Exception(u"Сумма не сходится.")
			for child in item["children"]:
				check_item(child, True)
		else:
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
				check_item(child, False)

def check_document(document):
	for table in document.tables:
		if table.is_one_sum_column:
			total = 0
			for item in table.data[:-1]:
				check_item(item, True)
				total += item["value"]
			if not numbers_equal(total, table.data[-1]["value"]):
				print table.number, total, table.data[-1]["value"]
				raise Exception(u"Сумма не сходится.")
		else:
			total2014 = 0
			total2015 = 0
			for item in table.data[:-1]:
				check_item(item, False)
				total2014 += item["value2014"]
				total2015 += item["value2015"]
			if not numbers_equal(total2014, table.data[-1]["value2014"]):
				print table.number, total2014, table.data[-1]["value2014"]
				raise Exception(u"Сумма за 2014 год не сходится.")
			if not numbers_equal(total2015, table.data[-1]["value2015"]):
				print table.number, total2015, table.data[-1]["value2015"]
				raise Exception(u"Сумма за 2015 год не сходится.")

def get_document(input_file_name):
	with codecs.open(input_file_name, "r", encoding = "utf-8-sig") as input_file:
		input_data = input_file.readlines()
		
		document = Budget2013_32()
		
		line_index = 0
		
		#tables
		tables = []
		data_lines = []
		empty_lines_count = 0
		while line_index < len(input_data):
			data_line = input_data[line_index].rstrip()
			line_index += 1
			if not data_line:
				if empty_lines_count == 0:
					data_lines.append(data_line) # empty line
					empty_lines_count += 1
				elif empty_lines_count == 1:
					tables.append(data_lines)
					data_lines = []
					empty_lines_count = 0
			else:
				data_lines.append(data_line)
		if data_lines:
			tables.append(data_lines)
			data_lines = []
		
		for table in tables:
			process_table(table, document)
		
		check_document(document)
		
		return document

def write_table_item(output_file, item, is_one_sum_column, level = 0):
	output_file.write("\t" * level + item["name"] + " " + (unicode(item["value"]) if is_one_sum_column else unicode(item["value2014"]) + " " + unicode(item["value2015"])) + "\r\n")
	if item["children"]:
		for child in item["children"]:
			write_table_item(output_file, child, is_one_sum_column, level + 1)

def do_write_text_document(output_file, document):
	for table in document.tables:
		output_file.write(u"Таблица " + unicode(table.number) + "\r\n")
		output_file.write(table.caption + "\r\n")
		output_file.write(u" ".join(table.header) + "\r\n")
		for item in table.data:
			write_table_item(output_file, item, table.is_one_sum_column)
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
		write_json_document(document, output_json_file_name, JsonEncoder_Budget2013_32)
	if output_json_pretty_file_name:
		write_json_pretty_document(document, output_json_pretty_file_name, JsonEncoder_Budget2013_32)
