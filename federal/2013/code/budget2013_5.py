# coding: utf-8

import codecs
import re
import json
from budget2013_common import *


class Budget2013_5_DataItem(object):
	def __init__(self):
		self._kbk_admin = None
		self._kbk_income = None
		self._parent = None
		self._name = None
		self._children = []
		self._notes = []
	
	@property
	def kbk_admin(self):
		return self._kbk_admin
	@kbk_admin.setter
	def kbk_admin(self, value):
		self._kbk_admin = value
	
	@property
	def kbk_income(self):
		return self._kbk_income
	@kbk_income.setter
	def kbk_income(self, value):
		self._kbk_income = value
	
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
	
	@property
	def notes(self):
		return self._notes
	@notes.setter
	def notes(self, value):
		self._notes = value

class JsonEncoder_Budget2013_5_DataItem(json.JSONEncoder):
	def default(self, o):
		return {
			"kbk_admin": o.kbk_admin,
			"kbk_income": o.kbk_income,
			"name": o.name,
			"children": [self.default(child) for child in o.children],
			"notes": o.notes
		}

class Budget2013_5(object):
	def __init__(self):
		self._caption = None
		self._header = []
		self._data = []
		self._additional_data_caption = None
		self._additional_data = []
		self._notes = []
	
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
	
	@property
	def notes(self):
		return self._notes
	@notes.setter
	def notes(self, value):
		self._notes = value

class JsonEncoder_Budget2013_5(json.JSONEncoder):
	def default(self, o):
		item_encoder = JsonEncoder_Budget2013_5_DataItem()
		return {
			"caption": o.caption,
			"header": o.header,
			"data": [item_encoder.default(item) for item in o.data],
			"additional_data_caption": o.additional_data_caption,
			"additional_data": [item_encoder.default(item) for item in o.additional_data],
			"notes": o.notes
		}

def correct_item_notes(item, notes):
	r = re.compile("(?:\\d+,)*(\\d+)$")
	while True:
		m = r.search(item.name)
		if not m:
			break
		found_note = None
		for note in notes:
			if note.startswith(m.group(1) + " "):
				found_note = note
				break
		if found_note:
			item.name = item.name[:-len(m.group(1))]
			if item.name.endswith(","):
				item.name = item.name[:-1]
			item.notes.append(found_note)
		else:
			raise Exception("Note " + m.group(1) + " not found.")
	if item.notes:
		item.notes = list(reversed(item.notes))
	for child in item.children:
		correct_item_notes(child, notes)

def correct_notes(document):
	for item in document.data:
		correct_item_notes(item, document.notes)
	for item in document.additional_data:
		correct_item_notes(item, document.notes)

def get_document(input_file_name):
	with codecs.open(input_file_name, "r", encoding = "utf-8") as input_file:
		input_data = input_file.readlines()
		
		document = Budget2013_5()
		
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
		m = re.compile("(.*):(.*),(.*)").match(header[0])
		document.header.append(m.group(1) + " " + m.group(2))
		document.header.append(m.group(1) + " " + m.group(3))
		document.header.extend(header[1:])
		
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
			m2 = re.compile("^(\\d{3}) (\\d \\d{2} \\d{5} \\d{2} \\d{4} \\d{3})\\s+(.*)").match(d)
			if not m2:
				# министерство
				item = Budget2013_5_DataItem()
				item.kbk_admin = m1.group(1)
				item.name = m1.group(2)
				document.data.append(item)
			else:
				item = Budget2013_5_DataItem()
				item.kbk_admin = m2.group(1)
				item.kbk_income = m2.group(2)
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
			m = re.compile("^(\\d \\d{2} \\d{5} \\d{2} \\d{4} \\d{3})\\s+(.*)").match(d)
			item = Budget2013_5_DataItem()
			item.kbk_income = m.group(1)
			item.name = m.group(2)
			document.additional_data.append(item)
		
		#notes
		note_lines = []
		while line_index < len(input_data):
			note_line = input_data[line_index].strip()
			line_index += 1
			if not note_line:
				break
			if re.compile("^\\d+ ").match(note_line):
				if note_lines != []:
					document.notes.append(join_lines(note_lines))
				note_lines = []
			note_lines.append(note_line)
		if note_lines != []:
			document.notes.append(join_lines(note_lines))
		
		# correct notes
		correct_notes(document)

		return document

def write_data_item(output_file, item, level = 0):
	output_file.write("\t" * level + (item.kbk_admin + " " if item.kbk_admin else "") + (item.kbk_income + " " if item.kbk_income else "") + item.name + "\r\n")
	for note in item.notes:
		output_file.write("\t" * (level + 1) + note + "\r\n")
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
	for note in document.notes:
		output_file.write(note + "\r\n")


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
		write_json_document(document, output_json_file_name, JsonEncoder_Budget2013_5)
	if output_json_pretty_file_name:
		write_json_pretty_document(document, output_json_pretty_file_name, JsonEncoder_Budget2013_5)
