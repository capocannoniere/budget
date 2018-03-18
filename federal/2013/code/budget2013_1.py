# coding: utf-8

import codecs
import re
import json
from budget2013_common import *


class Budget2013_1_TableDataItem(object):
	def __init__(self):
		self._name = None
		self._parent = None
		self._federal_budget = None
		self._federal_budget_children = []
		self._regional_budget = None
		self._regional_budget_children = []
		self._children = []
		self._note = None
	
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
	def federal_budget(self):
		return self._federal_budget
	@federal_budget.setter
	def federal_budget(self, value):
		self._federal_budget = value
	
	@property
	def federal_budget_children(self):
		return self._federal_budget_children
	
	@property
	def regional_budget(self):
		return self._regional_budget
	@regional_budget.setter
	def regional_budget(self, value):
		self._regional_budget = value
	
	@property
	def regional_budget_children(self):
		return self._regional_budget_children
	
	@property
	def children(self):
		return self._children
	
	@property
	def note(self):
		return self._note
	@note.setter
	def note(self, value):
		self._note = value
	
	def level(self):
		return 0 if not self.parent else self.parent.level() + 1

class JsonEncoder_Budget2013_1_TableDataItem(json.JSONEncoder):
	def default(self, o):
		return {
			"name": o.name,
			"federal_budget": o.federal_budget,
			"federal_budget_children": [self.default(child) for child in o.federal_budget_children],
			"regional_budget": o.regional_budget,
			"regional_budget_children": [self.default(child) for child in o.regional_budget_children],
			"children": [self.default(child) for child in o.children],
			"note": o.note
		}

class Budget2013_1(object):
	def __init__(self):
		self._caption = None
		self._table_header = []
		self._table_data = []
		self._note = None
		self._notes = []
	
	@property
	def caption(self):
		return self._caption
	@caption.setter
	def caption(self, value):
		self._caption = value
	
	@property
	def table_header(self):
		return self._table_header
	@table_header.setter
	def table_header(self, value):
		self._table_header = value
	
	@property
	def table_data(self):
		return self._table_data
	@table_data.setter
	def table_data(self, value):
		self._table_data = value
	
	@property
	def note(self):
		return self._note
	@note.setter
	def note(self, value):
		self._note = value
	
	@property
	def notes(self):
		return self._notes
	@notes.setter
	def notes(self, value):
		self._notes = value

class JsonEncoder_Budget2013_1(json.JSONEncoder):
	def default(self, o):
		item_encoder = JsonEncoder_Budget2013_1_TableDataItem()
		return {
			"caption": o.caption,
			"table_header": o.table_header,
			"table_data": [item_encoder.default(item) for item in o.table_data],
			"note": o.note,
			"notes": o.notes
		}

def get_element_level(line):
	m_level = re.compile("^( +)").match(line)
	return 0 if not m_level else len(m_level.group(1))

def join_element_lines(lines):
	if lines == []:
		return []
	else:
		level = get_element_level(lines[0])
		return u" " * level + join_lines(lines)

class TableDataState(object):
	Initial = 0
	Header = 1
	Element = 2
	ElementEnd = 3

def parse_element_line(line):
	r1 = re.compile("(.*)\\s+(\\d+(?:,\\d+)?\\*?) (\\d+(?:,\\d+)?\\*?)$")
	m1 = r1.match(line)
	r2 = re.compile(u"(.*)\\s+(В порядке.*)")
	m2 = r2.match(line)
	
	if m1:
		return (m1.group(1), True, m1.group(2), m1.group(3))
	elif m2:
		return (m2.group(1), True, m2.group(2), m2.group(2))
	else:
		return (line, False, None, None)

def parse_table_data(lines):
	items = []
	
	header_lines = []
	element_lines = []
	
	state = TableDataState.Initial
	for line_index, line in enumerate(lines):
		if state == TableDataState.Initial:
			# начальное состояние
			# ожидаем первую строку заголовочного элемента
			if line != line.upper():
				raise Exception("Expected: header line, got: " + line);
			header_lines.append(line)
			state = TableDataState.Header
		elif state == TableDataState.Header:
			if line == line.upper():
				# все еще заголовок
				header_lines.append(line)
			else:
				# заголовок закончился
				item = Budget2013_1_TableDataItem()
				item.name = join_lines(header_lines)
				items.append(item)
				header_lines = []
				
				# обрабатываем элемент
				(element_line, element_end, federal_budget, regional_budget) = parse_element_line(line)
				element_lines.append(element_line)
				if element_end:
					item = Budget2013_1_TableDataItem()
					item.name = join_element_lines(element_lines)
					item.federal_budget = federal_budget
					item.regional_budget = regional_budget
					items.append(item)
					
					element_lines = []
					state = TableDataState.ElementEnd
				else:
					state = TableDataState.Element
		elif state == TableDataState.Element or state == TableDataState.ElementEnd:
			# ожидаем либо заголовок, либо элемент
			if line == line.upper():
				# заголовок

				# если есть еще не добавленный элемент
				if state == TableDataState.Element:
					item = Budget2013_1_TableDataItem()
					item.name = join_element_lines(element_lines)
					items.append(item)
					element_lines = []
				
				header_lines.append(line)
				state = TableDataState.Header
			else:
				# элемент
				if line.endswith(u"в том числе:"):
					if element_lines != []:
						item = Budget2013_1_TableDataItem()
						item.name = join_element_lines(element_lines)
						items.append(item)
						element_lines = []
						state = TableDataState.ElementEnd
				else:
					(element_line, element_end, federal_budget, regional_budget) = parse_element_line(line)
					element_lines.append(element_line)
					if element_end:
						item = Budget2013_1_TableDataItem()
						item.name = join_element_lines(element_lines)
						item.federal_budget = federal_budget
						item.regional_budget = regional_budget
						items.append(item)
						
						element_lines = []
						state = TableDataState.ElementEnd
					else:
						state = TableDataState.Element
		else:
			raise Exception("Invalid state" + str(state))
	
	processed_items = []
	next_federal_budget_children = False
	next_regional_budget_children = False
	for item_index, item in enumerate(items):
		if item.name == item.name.upper():
			# заголовок
			processed_items.append(item)
		else:
			# элемент
			
			level = get_element_level(item.name)
			item.name = item.name[level:] # убрать пробелы в начале строки

			# вложенность
			if level == 0:
				parent = processed_items[-1]
				parent.children.append(item)
				item.parent = parent
			else:
				parent = items[item_index - 1]
				if next_federal_budget_children:
					parent.federal_budget_children.append(item)
					item.parent = parent
				elif next_regional_budget_children:
					parent.regional_budget_children.append(item)
					item.parent = parent
				else:
					while parent.level() != level:
						parent = parent.parent
					parent.children.append(item)
					item.parent = parent
			
			# федеральный бюджет
			next_federal_budget_children = item.federal_budget and item.federal_budget.endswith("*")
			if next_federal_budget_children:
				item.federal_budget = item.federal_budget[:-1]
			if item.federal_budget:
				try:
					item.federal_budget = float(item.federal_budget.replace(',', '.'))
				except ValueError:
					pass

			# региональный бюджет
			next_regional_budget_children = item.regional_budget and item.regional_budget.endswith("*")
			if next_regional_budget_children:
				item.regional_budget = item.regional_budget[:-1]
			if item.regional_budget:
				try:
					item.regional_budget = float(item.regional_budget.replace(',', '.'))
				except ValueError:
					pass
	
	return processed_items

def correct_item_notes(item, notes):
	r = re.compile("(.*)\\s*(\\(\\d+\\))")
	m = r.match(item.name)
	if m:
		found_note = None
		for note in notes:
			if note.startswith(m.group(2)):
				found_note = note
				break
		if found_note:
			item.name = m.group(1)
			item.note = found_note
	for child in item.children:
		correct_item_notes(child, notes)
	for child in item.federal_budget_children:
		correct_item_notes(child, notes)
	for child in item.regional_budget_children:
		correct_item_notes(child, notes)

def correct_notes(document):
	for item in document.table_data:
		correct_item_notes(item, document.notes)

def get_document(input_file_name):
	with codecs.open(input_file_name, "r", encoding = "utf-8") as input_file:
		input_data = input_file.readlines()
		
		document = Budget2013_1()
		
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
		
		# table header
		table_header_line = input_data[line_index].strip()
		line_index += 1
		document.table_header = table_header_line.split(";")
		
		# table data
		table_data_lines = []
		while line_index < len(input_data):
			table_data_line = input_data[line_index].rstrip()
			line_index += 1
			if not table_data_line.lstrip():
				break
			table_data_lines.append(table_data_line)
		document.table_data = parse_table_data(table_data_lines)
		
		# note
		note_lines = []
		while line_index < len(input_data):
			note_line = input_data[line_index].strip()
			line_index += 1
			if not note_line:
				break
			note_lines.append(note_line)
		document.note = join_lines(note_lines)

		#notes
		note_lines = []
		while line_index < len(input_data):
			note_line = input_data[line_index].strip()
			line_index += 1
			if not note_line:
				break
			if re.compile("^\\(\\d+\\)\\. *").match(note_line):
				if note_lines != []:
					document.notes.append(join_lines(note_lines))
				note_lines = []
			note_lines.append(note_line)
		if note_lines != []:
			document.notes.append(join_lines(note_lines))
		
		# correct notes
		correct_notes(document)
		
		return document

def write_table_item(output_file, item, level = 0):
	output_file.write("\t" * level + item.name + "\r\n")
	if item.federal_budget != None:
		output_file.write("\t" * level + unicode(item.federal_budget) + "\r\n")
	for federal_budget_child in item.federal_budget_children:
		write_table_item(output_file, federal_budget_child, level + 1)
	if item.regional_budget != None:
		output_file.write("\t" * level + unicode(item.regional_budget) + "\r\n")
	for regional_budget_child in item.regional_budget_children:
		write_table_item(output_file, regional_budget_child, level + 1)
	if item.note:
		output_file.write("\t" * level + item.note + "\r\n")
	for child in item.children:
		write_table_item(output_file, child, level + 1)

def do_write_text_document(output_file, document):
	output_file.write(document.caption + "\r\n")
	output_file.write(u" ".join(document.table_header) + "\r\n")
	for table_item in document.table_data:
		write_table_item(output_file, table_item)
	output_file.write(document.note + "\r\n")
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
		write_json_document(document, output_json_file_name, JsonEncoder_Budget2013_1)
	if output_json_pretty_file_name:
		write_json_pretty_document(document, output_json_pretty_file_name, JsonEncoder_Budget2013_1)
