# coding: utf-8

import codecs
import re
import json
from budget2013_common import *


class Budget2013_26(object):
	def __init__(self):
		self._caption = None
		self._header = []
		self._data = []
	
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
	
class JsonEncoder_Budget2013_26(json.JSONEncoder):
	def default(self, o):
		return {
			"caption": o.caption,
			"header": o.header,
			"data": o.data
		}

def check_document(document):
	total2014 = 0
	total2015 = 0
	for item in document.data[:-1]:
		total2014 += item["value2014"]
		total2015 += item["value2015"]
	if not numbers_equal(total2014, document.data[-1]["value2014"]):
		raise Exception(u"Сумма за 2014 год не сходится.");
	if not numbers_equal(total2015, document.data[-1]["value2015"]):
		raise Exception(u"Сумма за 2015 год не сходится.");

def get_document(input_file_name):
	with codecs.open(input_file_name, "r", encoding = "utf-8") as input_file:
		input_data = input_file.readlines()
		
		document = Budget2013_26()
		
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
		header = header_line.split(";")
		document.header.extend(header[:-1])
		m = re.compile("(.*):(.*),(.*)").match(header[-1])
		document.header.append(m.group(1) + ": " + m.group(2))
		document.header.append(m.group(1) + ": " + m.group(3))
		
		# data
		while line_index < len(input_data):
			data_line = input_data[line_index].strip()
			line_index += 1
			if not data_line:
				break
			r = re.compile("\\s+(\\d+(?: \\d{3})*(?:,\\d+)?\\*?) (\\d+(?: \\d{3})*(?:,\\d+)?\\*?)")
			m = r.search(data_line)
			value2014 = m.group(1)
			value2015 = m.group(2)
			name = data_line[:len(data_line) - len(value2014) - 1 - len(value2015)].strip()
			item = {"name":name, "value2014": float(value2014.replace(',', '.').replace(' ', '')), "value2015": float(value2015.replace(',', '.').replace(' ', ''))}
			document.data.append(item)

		check_document(document)
		
		return document

def do_write_text_document(output_file, document):
	output_file.write(document.caption + "\r\n")
	output_file.write(u" ".join(document.header) + "\r\n")
	for item in document.data:
		output_file.write(item["name"] + " " + unicode(item["value2014"]) + " " + unicode(item["value2015"]) + "\r\n")


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
		write_json_document(document, output_json_file_name, JsonEncoder_Budget2013_26)
	if output_json_pretty_file_name:
		write_json_pretty_document(document, output_json_pretty_file_name, JsonEncoder_Budget2013_26)
