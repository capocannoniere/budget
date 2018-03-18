# coding: utf-8

import codecs
import re
import json
from budget2013_common import *


class Budget2013_42_SubTable1Item(object):
	def __init__(self):
		self._no = None
		self._purpose = None
		self._principal = None
		self._value2014 = None
		self._value2015 = None
		self._regress = None
		self._check = None
		self._other = []
		self._parent = None
		self._children = []
	
	@property
	def no(self):
		return self._no
	@no.setter
	def no(self, value):
		self._no = value
	
	@property
	def purpose(self):
		return self._purpose
	@purpose.setter
	def purpose(self, value):
		self._purpose = value
	
	@property
	def principal(self):
		return self._principal
	@principal.setter
	def principal(self, value):
		self._principal = value
	
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
	def regress(self):
		return self._regress
	@regress.setter
	def regress(self, value):
		self._regress = value
	
	@property
	def check(self):
		return self._check
	@check.setter
	def check(self, value):
		self._check = value
	
	@property
	def other(self):
		return self._other
	@other.setter
	def other(self, value):
		self._other = value
	
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

class JsonEncoder_Budget2013_42_SubTable1Item(json.JSONEncoder):
	def default(self, o):
		return {
			"no": o.no,
			"purpose": o.purpose,
			"principal": o.principal,
			"value2014": o.value2014,
			"value2015": o.value2015,
			"regress": o.regress,
			"check": o.check,
			"other": o.other,
			"children": [self.default(child) for child in o.children]
		}

class Budget2013_42_SubTable1(object):
	def __init__(self):
		self._caption = None
		self._headers = []
		self._items = []
		self._notes = []
	
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

	@property
	def notes(self):
		return self._notes
	@notes.setter
	def notes(self, value):
		self._notes = value

class JsonEncoder_Budget2013_42_SubTable1(json.JSONEncoder):
	def default(self, o):
		item_encoder = JsonEncoder_Budget2013_42_SubTable1Item()
		return {
			"caption": o.caption,
			"headers": o.headers,
			"items": [item_encoder.default(item) for item in o.items],
			"notes": o.notes
		}

class Budget2013_42_SubTable2(object):
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

class JsonEncoder_Budget2013_42_SubTable2Item(json.JSONEncoder):
	def default(self, o):
		return {
			"name": o["name"],
			"value2014": o["value2014"],
			"value2015": o["value2015"]
		}

class JsonEncoder_Budget2013_42_SubTable2(json.JSONEncoder):
	def default(self, o):
		item_encoder = JsonEncoder_Budget2013_42_SubTable2Item()
		return {
			"caption": o.caption,
			"headers": o.headers,
			"items": [item_encoder.default(item) for item in o.items]
		}

class Budget2013_42_SubTables(object):
	def __init__(self):
		self._caption = None
		self._subtable1 = Budget2013_42_SubTable1()
		self._subtable2 = Budget2013_42_SubTable2()

	@property
	def caption(self):
		return self._caption
	@caption.setter
	def caption(self, value):
		self._caption = value
	
	@property
	def subtable1(self):
		return self._subtable1
	
	@property
	def subtable2(self):
		return self._subtable2

class JsonEncoder_Budget2013_42_SubTables(json.JSONEncoder):
	def default(self, o):
		subtable1_encoder = JsonEncoder_Budget2013_42_SubTable1()
		subtable2_encoder = JsonEncoder_Budget2013_42_SubTable2()
		return {
			"caption": o.caption,
			"subtable1": subtable1_encoder.default(o.subtable1),
			"subtable2": subtable2_encoder.default(o.subtable2)
		}

class Budget2013_42(object):
	def __init__(self):
		self._caption = None
		self._subtables1 = Budget2013_42_SubTables()
		self._subtables2 = Budget2013_42_SubTables()
	
	@property
	def caption(self):
		return self._caption
	@caption.setter
	def caption(self, value):
		self._caption = value
	
	@property
	def subtables1(self):
		return self._subtables1
	
	@property
	def subtables2(self):
		return self._subtables2

class JsonEncoder_Budget2013_42(json.JSONEncoder):
	def default(self, o):
		subtables_encoder = JsonEncoder_Budget2013_42_SubTables()
		return {
			"caption": o.caption,
			"subtables1": subtables_encoder.default(o.subtables1),
			"subtables2": subtables_encoder.default(o.subtables2)
		}

def check_subtables(subtables):
	total_value2014 = 0.0
	total_value2015 = 0.0
	for item in subtables.subtable1.items[:-1]:
		if item.value2014:
			total_value2014 += item.value2014
		if item.value2015:
			total_value2015 += item.value2015
	if total_value2014 != subtables.subtable1.items[-1].value2014:
		print subtables.subtable1.caption, total_value2014, subtables.subtable1.items[-1].value2014
		raise Exception(u"Сумма за 2014 год не сходится.")
	if total_value2015 != subtables.subtable1.items[-1].value2015:
		print subtables.subtable1.caption, total_value2015, subtables.subtable1.items[-1].value2015
		raise Exception(u"Сумма за 2015 год не сходится.")

def correct_purpose(subtable1):
	for item in subtable1.items:
		item.purpose = re.sub(" (\\d\\) )", "\r\n\\1", item.purpose)

def correct_document(document):
	correct_purpose(document.subtables1.subtable1)
	correct_purpose(document.subtables2.subtable1)
	
	parent_item = document.subtables2.subtable1.items[0]
	item = Budget2013_42_SubTable1Item()
	item.purpose = parent_item.purpose[parent_item.purpose.find("\r\n") + 2:]
	parent_item.purpose = parent_item.purpose[:parent_item.purpose.find("\r\n")]
	item.principal = parent_item.principal
	parent_item.principal = None
	item.other = parent_item.other
	parent_item.other = None
	item.parent = parent_item
	parent_item.children.append(item)
	for item in document.subtables2.subtable1.items[1:-1]:
		item.parent = parent_item
		parent_item.children.append(item)
	document.subtables2.subtable1.items = [parent_item, document.subtables2.subtable1.items[-1]]

def check_document(document):
	check_subtables(document.subtables1)
	check_subtables(document.subtables2)

def read_subtables(subtables, line_index, input_data):
	re_value = "\\d\\d?\\d?(?: \\d{3})*,\\d+"
	re_value_wrapped = "(" + re_value + ")"
	
	# subtables caption
	caption_lines = []
	while line_index < len(input_data):
		caption_line = input_data[line_index].strip()
		line_index += 1
		if not caption_line:
			break
		caption_lines.append(caption_line)
	subtables.caption = join_lines(caption_lines)

	# subtable1 caption
	caption_lines = []
	while line_index < len(input_data):
		caption_line = input_data[line_index].strip()
		line_index += 1
		if not caption_line:
			break
		caption_lines.append(caption_line)
	subtables.subtable1.caption = join_lines(caption_lines)
	
	# subtable1 headers
	headers = input_data[line_index].strip()
	line_index += 2
	subtables.subtable1.headers = headers.split(";")
	
	# subtable1 data
	while not input_data[line_index].strip().startswith(u"ИТОГО"):
		item = Budget2013_42_SubTable1Item()
		
		# no + purpose
		purpose_lines = []
		while line_index < len(input_data):
			purpose_line = input_data[line_index].strip()
			line_index += 1
			if not purpose_line:
				break
			purpose_lines.append(purpose_line)
		purpose = join_lines(purpose_lines)
		m = re.compile(u"^(\\d+) (.*)").match(purpose)
		if m:
			item.no = int(m.group(1))
			item.purpose = m.group(2)
		else:
			item.purpose = purpose
		
		# principal
		principal_lines = []
		while line_index < len(input_data):
			principal_line = input_data[line_index].strip()
			line_index += 1
			if not principal_line:
				break
			principal_lines.append(principal_line)
		item.principal = join_lines(principal_lines)
		
		if item.no:
			# value2014
			item.value2014 = float(input_data[line_index].strip().replace(",", ".").replace(" ", ""))
			line_index += 2
		
			# value2015
			item.value2015 = float(input_data[line_index].strip().replace(",", ".").replace(" ", ""))
			line_index += 2

			# regress
			s = input_data[line_index].strip()
			if s == u"Нет":
				item.regress = False
			elif s == u"Есть":
				item.regress = True
			else:
				print s
				raise Exception(u"Unknown regress: " + s)
			line_index += 2
			
			# check
			s = input_data[line_index].strip()
			if s == u"Нет":
				item.check = False
			elif s == u"Есть":
				item.check = True
			else:
				print s
				raise Exception(u"Unknown check: " + s)
			line_index += 2
		
		# other
		other_lines = []
		while line_index < len(input_data):
			other_line = input_data[line_index].strip()
			line_index += 1
			if not other_line:
				break
			if re.compile("^\\d+\\. ").match(other_line):
				if other_lines:
					o = join_lines(other_lines)
					item.other.append(o)
					other_lines = []
			other_lines.append(other_line)
		if other_lines:
			o = join_lines(other_lines)
			item.other.append(o)
			other_lines = []
		
		subtables.subtable1.items.append(item)
	
	# ИТОГО
	s = input_data[line_index].strip()
	m = re.compile(u"^(ИТОГО)\\*? " + re_value_wrapped + " " + re_value_wrapped).match(s)
	item = Budget2013_42_SubTable1Item()
	item.purpose = m.group(1)
	item.value2014 = float(m.group(2).replace(",", ".").replace(" ", ""))
	item.value2015 = float(m.group(3).replace(",", ".").replace(" ", ""))
	subtables.subtable1.items.append(item)
	line_index += 2
	
	# notes
	if input_data[line_index].startswith("*"):
		notes_lines = []
		while line_index < len(input_data):
			notes_line = input_data[line_index].rstrip()
			line_index += 1
			if not notes_line:
				break
			m = re.compile("^\\*? (.*)").match(notes_line)
			if m:
				if notes_lines:
					note = join_lines(notes_lines)
					subtables.subtable1.notes.append(note)
					notes_lines = []
				notes_lines.append(m.group(1))
			else:
				notes_lines.append(notes_line.lstrip())
		if notes_lines:
			note = join_lines(notes_lines)
			subtables.subtable1.notes.append(note)
			notes_lines = []
	
	# subtable2 caption
	caption_lines = []
	while line_index < len(input_data):
		caption_line = input_data[line_index].strip()
		line_index += 1
		if not caption_line:
			break
		caption_lines.append(caption_line)
	subtables.subtable2.caption = join_lines(caption_lines)

	# subtable2 headers
	headers = input_data[line_index].strip()
	line_index += 2
	headers = headers.split(";")
	subtables.subtable2.headers = headers[:-1]
	m = re.compile("(.*):(.*),(.*)").match(headers[-1])
	subtables.subtable2.headers.append(m.group(1) + ": " + m.group(2))
	subtables.subtable2.headers.append(m.group(1) + ": " + m.group(3))
	
	#subtable2 data
	while line_index < len(input_data):
		data_line = input_data[line_index].strip()
		line_index += 1
		if not data_line:
			break
		m = re.compile(re_value_wrapped + " " + re_value_wrapped + "$").search(data_line)
		value2014 = float(m.group(1).replace(",", ".").replace(" ", ""))
		value2015 = float(m.group(2).replace(",", ".").replace(" ", ""))
		name = data_line[:-len(m.group(1)) - 1 - len(m.group(2))].strip()
		item = {"name": name, "value2014": value2014, "value2015": value2015}
		subtables.subtable2.items.append(item)
	
	return line_index

def get_document(input_file_name):
	with codecs.open(input_file_name, "r", encoding = "utf-8-sig") as input_file:
		input_data = input_file.readlines()
		
		document = Budget2013_42()
		
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

		line_index = read_subtables(document.subtables1, line_index, input_data)
		line_index = read_subtables(document.subtables2, line_index, input_data)
		
		correct_document(document)
		check_document(document)
		
		return document

def write_item(output_file, item, level = 0):
	output_file.write(" " * level + (unicode(item.no) + " " if item.no else "") + item.purpose + " " + 
		(item.principal + " " if item.principal else "") + (unicode(item.value2014) + " " if item.value2014 else "") + 
		(unicode(item.value2015) + " " if item.value2015 else "") + (unicode(item.regress) + " " if item.regress else "") + 
		(unicode(item.check) if item.check else "") + "\r\n")
	if item.other:
		for o in item.other:
			output_file.write(" " * level + o + "\r\n");
	output_file.write("\r\n")
	
	if item.children:
		for child in item.children:
			write_item(output_file, child, level + 1)

def write_subtables(output_file, subtables):
	output_file.write(subtables.subtable1.caption + "\r\n\r\n")
	output_file.write(u" ".join(subtables.subtable1.headers) + "\r\n\r\n")
	for item in subtables.subtable1.items[:-1]:
		write_item(output_file, item)
	output_file.write(subtables.subtable1.items[-1].purpose + " " + unicode(subtables.subtable1.items[-1].value2014) + " " + 
		unicode(subtables.subtable1.items[-1].value2015) + "\r\n\r\n")
	if subtables.subtable1.notes:
		for note in subtables.subtable1.notes:
			output_file.write(note + "\r\n")
		output_file.write("\r\n")

	output_file.write(subtables.subtable2.caption + "\r\n\r\n")
	output_file.write(u" ".join(subtables.subtable2.headers) + "\r\n\r\n")
	for item in subtables.subtable2.items:
		output_file.write(item["name"] + " " + unicode(item["value2014"]) + " " + unicode(item["value2015"]) + "\r\n")
	output_file.write("\r\n")

def do_write_text_document(output_file, document):
	output_file.write(document.caption + "\r\n\r\n")
	
	write_subtables(output_file, document.subtables1)
	write_subtables(output_file, document.subtables2)


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
		write_json_document(document, output_json_file_name, JsonEncoder_Budget2013_42)
	if output_json_pretty_file_name:
		write_json_pretty_document(document, output_json_pretty_file_name, JsonEncoder_Budget2013_42)
