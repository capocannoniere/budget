# coding: utf-8

import codecs
import re
import json
from budget2013_common import *


class Budget2013_39_SubTable(object):
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

class JsonEncoder_Budget2013_39_SubTable1Item(json.JSONEncoder):
	def default(self, o):
		return {
			"name": o["name"],
			"value": o["value"]
		}

class JsonEncoder_Budget2013_39_SubTable1(json.JSONEncoder):
	def default(self, o):
		item_encoder = JsonEncoder_Budget2013_39_SubTable1Item()
		return {
			"caption": o.caption,
			"headers": o.headers,
			"items": [item_encoder.default(item) for item in o.items]
		}

class JsonEncoder_Budget2013_39_SubTable2Item(json.JSONEncoder):
	def default(self, o):
		return {
			"name": o["name"],
			"source": o["source"],
			"value": o["value"],
			"period": o["period"]
		}

class JsonEncoder_Budget2013_39_SubTable2(json.JSONEncoder):
	def default(self, o):
		item_encoder = JsonEncoder_Budget2013_39_SubTable2Item()
		return {
			"caption": o.caption,
			"headers": o.headers,
			"items": [item_encoder.default(item) for item in o.items]
		}

class Budget2013_39_ReceiveItem(object):
	def __init__(self):
		self._name = None
		self._return_date = None
		self._loan_sum = None
		self._usage_before_2013 = None
		self._usage_2013 = None
		self._parent = None
		self._children = []
	
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self, value):
		self._name = value
	
	@property
	def return_date(self):
		return self._return_date
	@return_date.setter
	def return_date(self, value):
		self._return_date = value
	
	@property
	def loan_sum(self):
		return self._loan_sum
	@loan_sum.setter
	def loan_sum(self, value):
		self._loan_sum = value
	
	@property
	def usage_before_2013(self):
		return self._usage_before_2013
	@usage_before_2013.setter
	def usage_before_2013(self, value):
		self._usage_before_2013 = value
	
	@property
	def usage_2013(self):
		return self._usage_2013
	@usage_2013.setter
	def usage_2013(self, value):
		self._usage_2013 = value
	
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

class JsonEncoder_Budget2013_39_ReceiveItem(json.JSONEncoder):
	def default(self, o):
		return {
			"name": o.name,
			"return_date": o.return_date,
			"loan_sum": o.loan_sum,
			"usage_before_2013": o.usage_before_2013,
			"usage_2013": o.usage_2013,
			"children": [self.default(child) for child in o.children],
		}

class Budget2013_39_SubTable3Item(object):
	def __init__(self):
		self._rz_no = None
		self._project_name = None
		self._project_no = None
		self._project_source = None
		self._purpose = None
		self._target = None
		self._receive_item = Budget2013_39_ReceiveItem()
		self._receive_children = []
		self._garants = []
		self._note = None
		self._parent = None
		self._children = []
	
	@property
	def rz_no(self):
		return self._rz_no
	@rz_no.setter
	def rz_no(self, value):
		self._rz_no = value
	
	@property
	def project_name(self):
		return self._project_name
	@project_name.setter
	def project_name(self, value):
		self._project_name = value
	
	@property
	def project_no(self):
		return self._project_no
	@project_no.setter
	def project_no(self, value):
		self._project_no = value
	
	@property
	def project_source(self):
		return self._project_source
	@project_source.setter
	def project_source(self, value):
		self._project_source = value
	
	@property
	def purpose(self):
		return self._purpose
	@purpose.setter
	def purpose(self, value):
		self._purpose = value
	
	@property
	def target(self):
		return self._target
	@target.setter
	def target(self, value):
		self._target = value
	
	@property
	def receive_item(self):
		return self._receive_item
	@receive_item.setter
	def receive_item(self, value):
		self._receive_item = value
	
	@property
	def receive_children(self):
		return self._receive_children
	@receive_children.setter
	def receive_children(self, value):
		self._receive_children = value
	
	@property
	def garants(self):
		return self._garants
	@garants.setter
	def garants(self, value):
		self._garants = value
	
	@property
	def note(self):
		return self._note
	@note.setter
	def note(self, value):
		self._note = value
	
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

class JsonEncoder_Budget2013_39_SubTable3Item(json.JSONEncoder):
	def default(self, o):
		receive_item_encoder = JsonEncoder_Budget2013_39_ReceiveItem()
		return {
			"rz_no": o.rz_no,
			"project_name": o.project_name,
			"project_no": o.project_no,
			"project_source": o.project_source,
			"purpose": o.purpose,
			"target": o.target,
			"receive_item": receive_item_encoder.default(o.receive_item),
			"receive_children": o.receive_children,
			"garants": o.garants,
			"note": o.note,
			"children": [self.default(child) for child in o.children],
		}

class Budget2013_39_SubTable3(object):
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

class JsonEncoder_Budget2013_39_SubTable3(json.JSONEncoder):
	def default(self, o):
		item_encoder = JsonEncoder_Budget2013_39_SubTable3Item()
		return {
			"caption": o.caption,
			"headers": o.headers,
			"items": [item_encoder.default(item) for item in o.items],
			"notes": o.notes
		}

class Budget2013_39(object):
	def __init__(self):
		self._caption = None
		self._subtable1 = Budget2013_39_SubTable()
		self._subtable2 = Budget2013_39_SubTable()
		self._subtable3 = Budget2013_39_SubTable3()
	
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
	
	@property
	def subtable3(self):
		return self._subtable3

class JsonEncoder_Budget2013_39(json.JSONEncoder):
	def default(self, o):
		subtable1_encoder = JsonEncoder_Budget2013_39_SubTable1()
		subtable2_encoder = JsonEncoder_Budget2013_39_SubTable2()
		subtable3_encoder = JsonEncoder_Budget2013_39_SubTable3()
		return {
			"caption": o.caption,
			"subtable1": subtable1_encoder.default(o.subtable1),
			"subtable2": subtable2_encoder.default(o.subtable2),
			"subtable3": subtable3_encoder.default(o.subtable3)
		}

def check_receive_item(receive_item):
	if not receive_item.children:
		return
	
	total_loan_sum = 0.0
	total_usage_before_2013 = 0.0
	total_usage_2013 = 0.0
	for child in receive_item.children:
		total_loan_sum += child.loan_sum
		total_usage_before_2013 += child.usage_before_2013
		total_usage_2013 += child.usage_2013
	if not numbers_equal(total_loan_sum, receive_item.loan_sum):
		print receive_item.name, total_loan_sum, receive_item.loan_sum
		raise Exception(u"Сумма заимствований по элементу не сходится.")
	if not numbers_equal(total_usage_before_2013, receive_item.usage_before_2013):
		print receive_item.name, total_usage_before_2013, receive_item.usage_before_2013
		raise Exception(u"Сумма, использованная до 2013 года, не сходится.")
	if not numbers_equal(total_usage_2013, receive_item.usage_2013):
		print receive_item.name, total_usage_2013, receive_item.usage_2013
		raise Exception(u"Сумма, используемая в 2013 году, не сходится.")

def check_item(item):
	if item.children:
		total_loan_sum = 0.0
		total_usage_before_2013 = 0.0
		total_usage_2013 = 0.0
		for child in item.children:
			total_loan_sum += child.receive_item.loan_sum
			total_usage_before_2013 += child.receive_item.usage_before_2013
			total_usage_2013 += child.receive_item.usage_2013
		if not numbers_equal(total_loan_sum, item.receive_item.loan_sum):
			print item.project_name, total_loan_sum, item.receive_item.loan_sum
			raise Exception(u"Сумма заимствований по элементу не сходится.")
		if not numbers_equal(total_usage_before_2013, item.receive_item.usage_before_2013):
			print item.project_name, total_usage_before_2013, item.receive_item.usage_before_2013
			raise Exception(u"Сумма, использованная до 2013 года, не сходится.")
		if not numbers_equal(total_usage_2013, item.receive_item.usage_2013):
			print item.project_name, total_usage_2013, item.receive_item.usage_2013
			raise Exception(u"Сумма, используемая в 2013 году, не сходится.")
	
	check_receive_item(item.receive_item)

def check_document(document):
	total_value = 0.0
	for item in document.subtable1.items[:-1]:
		total_value += item["value"]
	if total_value != document.subtable1.items[-1]["value"]:
		print total_value, document.subtable1.items[-1]["value"]
		raise Exception(u"Сумма по таблице 1 не сходится.")
	
	for item in document.subtable3.items:
		check_item(item)

def correct_notes(item, notes):
	if item.project_source:
		m = re.compile("(\\*+)$").search(item.project_source)
		if m:
			n = m.group(1)
			item.project_source = item.project_source[:-len(n)]
			item.note = notes[len(n) - 1]
	if item.children:
		for child in item.children:
			correct_notes(child, notes)

def get_document(input_file_name):
	with codecs.open(input_file_name, "r", encoding = "utf-8-sig") as input_file:
		input_data = input_file.readlines()
		
		document = Budget2013_39()
		
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

		# subtable1 caption
		caption_lines = []
		while line_index < len(input_data):
			caption_line = input_data[line_index].strip()
			line_index += 1
			if not caption_line:
				break
			caption_lines.append(caption_line)
		document.subtable1.caption = join_lines(caption_lines)
		
		# subtable1 headers
		headers = input_data[line_index].strip()
		line_index += 1
		document.subtable1.headers = headers.split(";")
		
		# subtable1 data
		lines = []
		while line_index < len(input_data):
			line = input_data[line_index].strip()
			line_index += 1
			if not line:
				break
			m = re.compile("-?\\d\\d?\\d?(?: \\d{3})*,\\d+$").search(line)
			if m:
				value = m.group(0)
				lines.append(line[:len(line) - len(value)].strip())
				name = join_lines(lines)
				value = float(value.replace(",", ".").replace(" ", ""))
				item = {"name": name, "value": value}
				document.subtable1.items.append(item)
				lines = []
			else:
				lines.append(line)
		if lines:
			value = m.group(0)
			lines.append(line[:len(line) - len(value)].strip())
			name = join_lines(lines)
			value = float(value.replace(",", ".").replace(" ", ""))
			item = {"name": name, "value": value}
			document.subtable1.items.append(item)
			lines = []
		
		# subtable2 caption
		caption_lines = []
		while line_index < len(input_data):
			caption_line = input_data[line_index].strip()
			line_index += 1
			if not caption_line:
				break
			caption_lines.append(caption_line)
		document.subtable2.caption = join_lines(caption_lines)
		
		# subtable2 headers
		headers = input_data[line_index].strip()
		line_index += 1
		document.subtable2.headers = headers.split(";")
		
		# subtable2 data
		lines = []
		while line_index < len(input_data):
			line = input_data[line_index].strip()
			line_index += 1
			if not line:
				break
			lines.append(line)
		value = float(lines[-2].replace(",", ".").replace(" ", ""))
		period = lines[-1]
		lines = lines[:-2]
		name_lines = []
		for idx, line in enumerate(lines[1:]):
			if line[0].istitle():
				idx += 1
				name_lines.extend(lines[:idx])
				name = join_lines(name_lines)
				source_lines = lines[idx:]
				source = join_lines(source_lines)
				break
		item = {"name": name, "source": source, "value": value, "period": period}
		document.subtable2.items.append(item)

		# subtable3 caption
		caption_lines = []
		while line_index < len(input_data):
			caption_line = input_data[line_index].strip()
			line_index += 1
			if not caption_line:
				break
			caption_lines.append(caption_line)
		document.subtable3.caption = join_lines(caption_lines)
		
		# subtable3 headers
		headers = input_data[line_index].strip()
		if headers.endswith("*"):
			headers = headers[:-1]
		line_index += 2
		document.subtable3.headers = headers.split(";")
		
		re_value = "\\d\\d?\\d?(?: \\d{3})*,\\d+"
		
		count_itogo = 0
		
		# subtable3 data
		while True:
			lines = []
			while line_index < len(input_data):
				line = input_data[line_index].strip()
				line_index += 1
				if not line:
					break
				lines.append(line)
			l = join_lines(lines)
				
			m = re.compile("^(\\d+) (.*) (" + re_value + ") (" + re_value + ") (" + re_value + ")$").match(l)
			if m:
				item = Budget2013_39_SubTable3Item()
				item.rz_no = m.group(1)
				item.project_name = m.group(2)
				item.receive_item.loan_sum = float(m.group(3).replace(",", ".").replace(" ", ""))
				item.receive_item.usage_before_2013 = float(m.group(4).replace(",", ".").replace(" ", ""))
				item.receive_item.usage_2013 = float(m.group(5).replace(",", ".").replace(" ", ""))
				document.subtable3.items.append(item)
				continue

			m = re.compile("(" + re_value + ") (" + re_value + ") (" + re_value + ")$").search(l)
			if m:
				name = l[:-len(m.group(1)) - 1 - len(m.group(2)) - 1 - len(m.group(3))].strip()
				if name == u"ВСЕГО":
					total_item = Budget2013_39_SubTable3Item()
					total_item.project_name = name
					total_item.receive_item.loan_sum = float(m.group(1).replace(",", ".").replace(" ", ""))
					total_item.receive_item.usage_before_2013 = float(m.group(2).replace(",", ".").replace(" ", ""))
					total_item.receive_item.usage_2013 = float(m.group(3).replace(",", ".").replace(" ", ""))
					for item in document.subtable3.items:
						total_item.children.append(item)
						item.parent = total_item
					document.subtable3.items = [total_item]
					break
				elif name == u"ИТОГО":
					count_itogo += 1
					if count_itogo == 1:
						lines = []
						while line_index < len(input_data):
							line = input_data[line_index].strip()
							line_index += 1
							if not line:
								break
							lines.append(line)
						l = join_lines(lines)
						parent_item = Budget2013_39_SubTable3Item()
						parent_item.project_name = l
						document.subtable3.items.append(parent_item)
						continue
					elif count_itogo == 2:
						parent_item.receive_item.loan_sum = float(m.group(1).replace(",", ".").replace(" ", ""))
						parent_item.receive_item.usage_before_2013 = float(m.group(2).replace(",", ".").replace(" ", ""))
						parent_item.receive_item.usage_2013 = float(m.group(3).replace(",", ".").replace(" ", ""))
						continue
				else:
					parent_item = Budget2013_39_SubTable3Item()
					parent_item.project_name = name
					parent_item.receive_item.loan_sum = float(m.group(1).replace(",", ".").replace(" ", ""))
					parent_item.receive_item.usage_before_2013 = float(m.group(2).replace(",", ".").replace(" ", ""))
					parent_item.receive_item.usage_2013 = float(m.group(3).replace(",", ".").replace(" ", ""))
					document.subtable3.items[-1].children.append(parent_item)
					parent_item.parent = document.subtable3.items[-1]
					continue
			
			item = Budget2013_39_SubTable3Item()

			item.project_source = lines[-1]
			lines = lines[:-1]
			if lines[-1].startswith(u"№"):
				item.project_no = lines[-1]
				lines = lines[:-1]
			item.project_name = join_lines(lines)
			
			lines = []
			while line_index < len(input_data):
				line = input_data[line_index].strip()
				line_index += 1
				if not line:
					break
				lines.append(line)
			item.purpose = join_lines(lines)
			
			lines = []
			while line_index < len(input_data):
				line = input_data[line_index].strip()
				line_index += 1
				if not line:
					break
				lines.append(line)
			item.target = join_lines(lines)
			
			re_date = re.compile(u"^(.*) (\\d\\d? .* \\d{4} года)$")
			
			line = input_data[line_index].strip()
			if line.startswith(u"Всего"):
				line_index += 1
				m = re.compile("(" + re_value + ") (" + re_value + ") (" + re_value + ")$").search(line)
				name = line[:-len(m.group(1)) - 1 - len(m.group(2)) - 1 - len(m.group(3))].strip()
				item.receive_item.name = name
				m1 = re_date.match(item.receive_item.name)
				if m1:
					item.receive_item.return_date = m1.group(2)
					item.receive_item.name = m1.group(1)
				item.receive_item.loan_sum = float(m.group(1).replace(",", ".").replace(" ", ""))
				item.receive_item.usage_before_2013 = float(m.group(2).replace(",", ".").replace(" ", ""))
				item.receive_item.usage_2013 = float(m.group(3).replace(",", ".").replace(" ", ""))
				if input_data[line_index].strip() == u"в том числе:":
					line_index += 1
				lines = []
				while line_index < len(input_data):
					line = input_data[line_index].strip()
					line_index += 1
					if not line:
						break
					m = re.compile("(" + re_value + ") (" + re_value + ") (" + re_value + ")$").search(line)
					if m:
						name = line[:-len(m.group(1)) - 1 - len(m.group(2)) - 1 - len(m.group(3))].strip()
						lines.append(name)
						receive_item = Budget2013_39_ReceiveItem()
						receive_item.name = join_lines(lines)
						m1 = re_date.match(receive_item.name)
						if m1:
							receive_item.return_date = m1.group(2)
							receive_item.name = m1.group(1)
						receive_item.loan_sum = float(m.group(1).replace(",", ".").replace(" ", ""))
						receive_item.usage_before_2013 = float(m.group(2).replace(",", ".").replace(" ", ""))
						receive_item.usage_2013 = float(m.group(3).replace(",", ".").replace(" ", ""))
						receive_item.parent = item.receive_item
						item.receive_item.children.append(receive_item)
						lines = []
					else:
						lines.append(line)
			else:
				lines = []
				while line_index < len(input_data):
					line = input_data[line_index].strip()
					line_index += 1
					if not line:
						break
					lines.append(line)
				l = join_lines(lines)
				m = re.compile("(" + re_value + ") (" + re_value + ") (" + re_value + ")$").search(l)
				name = l[:-len(m.group(1)) - 1 - len(m.group(2)) - 1 - len(m.group(3))].strip()
				item.receive_item.name = name
				m1 = re_date.match(item.receive_item.name)
				if m1:
					item.receive_item.return_date = m1.group(2)
					item.receive_item.name = m1.group(1)
				item.receive_item.loan_sum = float(m.group(1).replace(",", ".").replace(" ", ""))
				item.receive_item.usage_before_2013 = float(m.group(2).replace(",", ".").replace(" ", ""))
				item.receive_item.usage_2013 = float(m.group(3).replace(",", ".").replace(" ", ""))
			
			if input_data[line_index].startswith("*"):
				input_data[line_index] = input_data[line_index][1:]
				while line_index < len(input_data):
					line = input_data[line_index].strip()
					line_index += 1
					if not line:
						break
					item.garants.append(line)
			
			parent_item.children.append(item)
			item.parent = parent_item

		# notes
		note_lines = []
		while line_index < len(input_data):
			note_line = input_data[line_index].strip()
			line_index += 1
			if not note_line:
				break
			note_lines.append(note_line)
		document.subtable3.notes = [join_lines(note_lines)]
		
		notes = []
		note_lines = []
		while line_index < len(input_data):
			note_line = input_data[line_index].strip()
			line_index += 1
			if not note_line:
				note = join_lines(note_lines)
				m = re.compile("^\\*+ (.*)$").match(note)
				if m:
					note = m.group(1)
				notes.append(note)
				note_lines = []
				continue
			note_lines.append(note_line)
		if note_lines:
			note = join_lines(note_lines)
			m = re.compile("^\\*+ (.*)$").match(note)
			if m:
				note = m.group(1)
			notes.append(note)
			note_lines = []
		document.subtable3.notes.append(notes[0])
		notes[0] = None
		
		for item in document.subtable3.items:
			correct_notes(item, notes)
		
		check_document(document)
		
		return document

def write_subtable1(output_file, subtable):
	output_file.write(subtable.caption + "\r\n")
	output_file.write(u" ".join(subtable.headers) + "\r\n")
	for item in subtable.items:
		output_file.write(item["name"] + " " + unicode(item["value"]) + "\r\n")
	output_file.write("\r\n")

def write_subtable2(output_file, subtable):
	output_file.write(subtable.caption + "\r\n")
	output_file.write(u" ".join(subtable.headers) + "\r\n")
	for item in subtable.items:
		output_file.write(item["name"] + " " + item["source"] + " " + unicode(item["value"]) + " " + item["period"] + "\r\n")
	output_file.write("\r\n")

def write_receive_item(output_file, receive_item, level):
	output_file.write("\t" * level + "(" + (receive_item.name + " " if receive_item.name else "") + 
		(receive_item.return_date + " " if receive_item.return_date else "") + 
		unicode(receive_item.loan_sum) + " " + unicode(receive_item.usage_before_2013) + " " + unicode(receive_item.usage_2013) + ")\r\n")
	for child in receive_item.children:
		write_receive_item(output_file, child, level + 1)

def write_subtable3_item(output_file, item, level = 0):
	output_file.write("\t" * level + (item.rz_no + " " if item.rz_no else "") + item.project_name + " " +
		(item.project_no + " " if item.project_no else "") + (item.project_source + " " if item.project_source else "") + 
		(item.purpose + " " if item.purpose else "") + (item.target + " " if item.target else "") + "\r\n")
	if item.garants:
		for garant in item.garants:
			output_file.write("\t" * level + garant + "\r\n")
	write_receive_item(output_file, item.receive_item, level)
	if item.note:
		output_file.write("\t" * level + item.note + "\r\n")
	for child in item.children:
		write_subtable3_item(output_file, child, level + 1)

def write_subtable3(output_file, subtable):
	output_file.write(document.subtable3.caption + "\r\n")
	output_file.write(u" ".join(document.subtable3.headers) + "\r\n")
	for item in document.subtable3.items:
		write_subtable3_item(output_file, item)
	if document.subtable3.notes:
		for note in document.subtable3.notes:
			output_file.write(note + "\r\n")

def do_write_text_document(output_file, document):
	output_file.write(document.caption + "\r\n\r\n")
	
	write_subtable1(output_file, document.subtable1)
	write_subtable2(output_file, document.subtable2)
	write_subtable3(output_file, document.subtable3)


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
		write_json_document(document, output_json_file_name, JsonEncoder_Budget2013_39)
	if output_json_pretty_file_name:
		write_json_pretty_document(document, output_json_pretty_file_name, JsonEncoder_Budget2013_39)
