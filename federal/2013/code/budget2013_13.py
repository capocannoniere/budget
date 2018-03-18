# coding: utf-8

import codecs
import re
import json
from budget2013_common import *


class Budget2013_13_DataItem(object):
	def __init__(self):
		self._name = None
		self._rz = None
		self._pr = None
		self._csr = None
		self._vr = None
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
	def rz(self):
		return self._rz
	@rz.setter
	def rz(self, value):
		self._rz = value
		
	@property
	def pr(self):
		return self._pr
	@pr.setter
	def pr(self, value):
		self._pr = value
	
	@property
	def csr(self):
		return self._csr
	@csr.setter
	def csr(self, value):
		self._csr = value
	
	@property
	def vr(self):
		return self._vr
	@vr.setter
	def vr(self, value):
		self._vr = value
	
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

class JsonEncoder_Budget2013_13_DataItem(json.JSONEncoder):
	def default(self, o):
		return {
			"name": o.name,
			"rz": o.rz,
			"pr": o.pr,
			"csr": o.csr,
			"vr": o.vr,
			"value": o.value,
			"children": [self.default(child) for child in o.children]
		}

class Budget2013_13(object):
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
	
class JsonEncoder_Budget2013_13(json.JSONEncoder):
	def default(self, o):
		item_encoder = JsonEncoder_Budget2013_13_DataItem()
		return {
			"caption": o.caption,
			"header": o.header,
			"data": [item_encoder.default(item) for item in o.data]
		}

def parse_item_data(item_data):
	regexps = [
		re.compile("^(\\d{2})  ((?:(?:[1-9](?: \\d{3})*)|0),\\d\\d?)$"),
		re.compile("^(\\d{2})  ([1-9]\\d(?: \\d{3})*,\\d\\d?)$"),
		re.compile("^(\\d{2})  ([1-9]\\d{2}(?: \\d{3})*,\\d\\d?)$"),

		re.compile("^(\\d{2}) (\\d{2})  ((?:(?:[1-9](?: \\d{3})*)|0),\\d\\d?)$"),
		re.compile("^(\\d{2}) (\\d{2})  ([1-9]\\d(?: \\d{3})*,\\d\\d?)$"),
		re.compile("^(\\d{2}) (\\d{2})  ([1-9]\\d{2}(?: \\d{3})*,\\d\\d?)$"),

		re.compile("^(\\d{2}) (\\d{2}) (\\d{7})  ((?:(?:[1-9](?: \\d{3})*)|0),\\d\\d?)$"),
		re.compile("^(\\d{2}) (\\d{2}) (\\d{7})  ([1-9]\\d(?: \\d{3})*,\\d\\d?)$"),
		re.compile("^(\\d{2}) (\\d{2}) (\\d{7})  ([1-9]\\d{2}(?: \\d{3})*,\\d\\d?)$"),

		re.compile("^(\\d{2}) (\\d{2}) (\\d{7}) (\\d{3})  ((?:(?:[1-9](?: \\d{3})*)|0),\\d\\d?)$"),
		re.compile("^(\\d{2}) (\\d{2}) (\\d{7}) (\\d{3})  ([1-9]\\d(?: \\d{3})*,\\d\\d?)"),
		re.compile("^(\\d{2}) (\\d{2}) (\\d{7}) (\\d{3})  ([1-9]\\d{2}(?: \\d{3})*,\\d\\d?)")
	]
	
	results = []
	success_count = 0
	for regexp in regexps:
		m = regexp.match(item_data)
		if m:
			success_count += 1
		results.append(m)
	
	if success_count == 0:
		raise Exception(u"No match for item data '{0}'".format(item_data))
	elif success_count == 1:
		m = None
		
		if results[0]:
			m = results[0]
		elif results[1]:
			m = results[1]
		elif results[2]:
			m = results[2]
		if m:
			return (m.group(1), None, None, None, parse_value(m.group(2)))

		if results[3]:
			m = results[3]
		elif results[4]:
			m = results[4]
		elif results[5]:
			m = results[5]
		if m:
			return (m.group(1), m.group(2), None, None, parse_value(m.group(3)))

		if results[6]:
			m = results[6]
		elif results[7]:
			m = results[7]
		elif results[8]:
			m = results[8]
		if m:
			return (m.group(1), m.group(2), m.group(3), None, parse_value(m.group(4)))

		if results[9]:
			m = results[9]
		elif results[10]:
			m = results[10]
		elif results[11]:
			m = results[11]
		if m:
			return (m.group(1), m.group(2), m.group(3), m.group(4), parse_value(m.group(5)))
			
		raise Exception("We should not get here.")
	else:
		success_results = [(result_index, result.re.pattern) for result_index, result in enumerate(results) if result]
		indices = map(lambda t: str(t[0]), success_results)
		patterns = map(lambda t: t[1], success_results)
		print u"Ambiguous match ({0}) for item data '{1}': matched {2}".format(",".join(indices), item_data, " and ".join(patterns))
		return (None, None, None, None, 0.0)

def parse_item(item_name, item_data):
	(rz, pr, csr, vr, value) = parse_item_data(item_data)
	
	item = Budget2013_13_DataItem()
	item.name = item_name
	item.rz = rz
	item.pr = pr
	item.csr = csr
	item.vr = vr
	item.value = value
	return item

def process_page(page, document, page_no):
#	print u"Page ", page_no
	
	r = re.compile("^\\d[ \\d]+\\d,\\d+$")
	count = 0
	for i in range(len(page)):
		if not r.match(page[-(i + 1)]):
			break
		count += 1
	data_in_the_end = count > 0

	if data_in_the_end:
		# данные находятся в конце страницы
		
		# выцепляем их
		page_number_data = page[-count:]
		page = page[:-count]
		
		# определяем наименования
		# считаем, что если строка начинается с большой буквы, то это новое наименование
		names = []
		name_lines = []
		for page_line in page:
			if page_line[0].istitle() and name_lines:
				name = join_lines(name_lines)
				names.append(name)
				name_lines = []
			if name_lines and page_line[0].istitle():
				raise Exception(u"A capital letter in the beginning of a line: {0}".format(page_line))
			name_lines.append(page_line)
		if name_lines:
			name = join_lines(name_lines)
			names.append(name)
			name_lines = []
		
		if len(names) != count:
			print "\r\n".join(page_number_data)
			print "\r\n\r\n".join(names)
			raise Exception("Length of data ({0}) != length of names ({1})".format(count, len(names)))
		
		for i in range(count):
			item_data = page_number_data[i]
			item_name = names[i]
			item = parse_item(item_name, item_data)
			document.data.append(item)
	else:
		r_check1 = re.compile(",\\d+$")
		r_check2 = re.compile("\\d{2}$")
		
		# данные находятся рядом с наименованиями
		r1 = re.compile("\\s+((?:\\d{2} )?(?:\\d{2} )?(?:\\d{7} )?(?:\\d{3} )? \\d\\d?\\d?(?: \\d{3})*,\\d\\d?)$")
		item_lines = []
		for page_line in page:
			m_total = re.compile(u"^(ВСЕГО) (.*)").match(page_line)
			if m_total:
				if item_lines:
					raise Exception("Expected that item_lines is empty.")
				item = Budget2013_13_DataItem()
				item.name = m_total.group(1)
				item.value = parse_value(m_total.group(2))
				document.data.append(item)
			else:
				m1 = r1.search(page_line)
				if m1:
					matched = m1.group(1)
					remainder = page_line[:len(page_line) - len(matched)]
					if r_check1.match(remainder) or r_check2.match(remainder):
						raise Exception(u"Numbers in the end of a line: {0}".format(remainder))
					item_lines.append(remainder)
					item_name = join_lines(item_lines)
					item_data = matched
					item = parse_item(item_name, item_data)
					document.data.append(item)
					item_lines = []
				else:
					if r_check1.match(page_line) or r_check1.match(page_line):
						raise Exception(u"Numbers in the end of a line: {0}".format(page_line))
					item_lines.append(page_line)
		if item_lines:
			print u"\r\n".join(page)
			raise Exception("Page must end with a data.")
#	print u""

def check_items_order(document):
	last = None
	for item in document.data:
		current = u""
		if item.rz:
			current += item.rz + " "
		if item.pr:
			current += item.pr + " "
		if item.csr:
			current += item.csr + " "
		if item.vr:
			current += item.vr + " "
		
		if last and last >= current:
			raise Exception(u"Items order is broken: {0}, {1}.".format(last, current))
		last = current

def is_parent_csr(csr_current, csr_parent):
	if len(csr_current) != len(csr_parent):
		raise Exception(u"Expected the same length csr: {0}, {1}.".format(csr_current, csr_parent))
	
	if csr_current == csr_parent:
		return False
	
	'''
	zeroes_count = 0
	i = 1
	while i <= len(csr_parent) and csr_parent[-i] == u'0':
		zeroes_count += 1
		i += 1
	if zeroes_count == 0 or (zeroes_count == 1 and csr_parent not in ['1008810', '1008850', '5500710', '5500730', '5500820']):
		return False
	
	prefix_len = len(csr_parent) - zeroes_count
	return csr_current[:prefix_len] == csr_parent[:prefix_len]
	'''
	csr_current_1 = csr_current[:3]
	csr_current_2 = csr_current[3:5]
	csr_current_3 = csr_current[5:7]
	csr_parent_1 = csr_parent[:3]
	csr_parent_2 = csr_parent[3:5]
	csr_parent_3 = csr_parent[5:7]
	if csr_parent_2 == u"00" and csr_parent_3 == u"00" and csr_parent_1 == csr_current_1:
		return True
	elif csr_parent_3 == u"00" and csr_parent_1 == csr_current_1 and csr_parent_2 == csr_current_2:
		return True
	elif csr_parent in ['1008810', '1008850', '5500710', '5500730', '5500820'] and csr_parent[:6] == csr_current[:6]:
		return True
	else:
		return False

def is_parent_vr(vr_current, vr_parent):
	if len(vr_current) != len(vr_parent):
		raise Exception(u"Expected the same length vr: {0}, {1}.".format(vr_current, vr_parent))
	
	if vr_current == vr_parent:
		return False
	
	zeroes_count = 0
	i = 1
	while i <= len(vr_parent) and vr_parent[-i] == u'0':
		zeroes_count += 1
		i += 1
	if zeroes_count == 0:
		return False
	
	prefix_len = len(vr_parent) - zeroes_count
	return vr_current[:prefix_len] == vr_parent[:prefix_len]

def find_item_parent(item, document, last_item):
	if item.rz and not last_item:
		return document.data[0] # ВСЕГО
	
	if item.rz and not last_item.rz:
		return last_item
	elif item.rz != last_item.rz:
		return find_item_parent(item, document, last_item.parent)

	# here item.rz == last_item.rz
	
	if not item.pr:
		raise Exception(u"Expected: item.pr is not null: {0}.".format(item.rz))
	if item.pr and not last_item.pr:
		if item.rz != last_item.rz:
			raise Exception(u"Expected: item.rz ({0}) == last_item.rz ({1})".format(item.rz, last_item.rz))
		return last_item
	elif item.pr != last_item.pr:
		return find_item_parent(item, document, last_item.parent)
	
	# here item.pr == last_item.pr
	
	if not item.csr:
		raise Exception(u"Expected: item.csr is not null: {0} {1}.".format(item.rz, item.pr))
	if item.csr and not last_item.csr:
		if item.pr != last_item.pr:
			raise Exception(u"Expected: item.pr ({0}) == last_item.pr ({1})".format(item.pr, last_item.pr))
		return last_item
	elif item.csr != last_item.csr:
		if is_parent_csr(item.csr, last_item.csr):
			return last_item
		else:
			return find_item_parent(item, document, last_item.parent)
	
	# here item.csr == last_item.csr
	
	if not item.vr:
		raise Exception(u"Expected: item.vr is not null: {0} {1} {2}.".format(item.rz, item.pr, item.csr))
	if item.vr and not last_item.vr:
		if item.csr != last_item.csr:
			raise Exception(u"Expected: item.csr ({0}) == last_item.csr ({1})".format(item.csr, last_item.csr))
		return last_item
	elif is_parent_vr(item.vr, last_item.vr):
		return last_item
	else:
		return find_item_parent(item, document, last_item.parent)

def group_items(document):
	# не трогать первый элемент (ВСЕГО)
	items_to_process = document.data[1:]
	document.data = [document.data[0]]
	
	for item_index, item in enumerate(items_to_process):
		parent = find_item_parent(item, document, items_to_process[item_index - 1])
		item.parent = parent
		parent.children.append(item)

def get_item_children_sum(item):
	val = 0
	for child in item.children:
		val += child.value
	return val

def get_item_short_name(item):
	return (item.rz + " " if item.rz else "") + (item.pr + " " if item.pr else "") + (item.csr + " " if item.csr else "") + (item.vr + " " if item.vr else "")

def get_item_text(item):
	return (item.rz + " " if item.rz else "") + (item.pr + " " if item.pr else "") + (item.csr + " " if item.csr else "") + (item.vr + " " if item.vr else "") + item.name + " " + unicode(item.value)

def check_item_values(item):
	if item.children:
		children_value = get_item_children_sum(item)
		if not numbers_equal(item.value, children_value):
			print u"Values are NOT equal: ({0}), value {1} and its children, value {2}, diff={3}.".format(get_item_short_name(item), item.value, children_value, item.value - children_value)
#		else:
#			print u"Values are equal: {0}".format(get_item_short_name(item))
		for child in item.children:
			check_item_values(child)

def check_values(document):
	for item in document.data:
		check_item_values(item)

def get_document(input_file_name):
	with codecs.open(input_file_name, "r", encoding = "utf-8") as input_file:
		input_data = input_file.readlines()
		
		document = Budget2013_13()
		
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
		
		#data
		pages = []
		data_lines = []
		while line_index < len(input_data):
			data_line = input_data[line_index].rstrip()
			line_index += 1
			if not data_line:
				pages.append(data_lines)
				data_lines = []
			else:
				data_lines.append(data_line)
		if data_lines:
			pages.append(data_lines)
			data_lines = []

		page_number = int(pages[0][0])
		header = pages[0][1]
		pages[0] = pages[0][2:]
		for i in range(1, len(pages)):
			page = pages[i]
			new_page_number = int(page[0])
			if page_number + 1 != new_page_number:
				raise Exception("Page numbers are not continuous: {0}, {1}".format(page_number, new_page_number) )
			else:
				page_number = new_page_number
			new_header = page[1]
			if header != new_header:
				print page_number
				raise Exception(u"Headers are not the same: '{0}', '{1}'".format(header, new_header))
			pages[i] = pages[i][2:]
		document.header = header.split(" ")

		page_no = 3078
		for page in pages:
			process_page(page, document, page_no)
			page_no += 1
		
		check_items_order(document)
		group_items(document)
		check_values(document)
		
		return document

def write_data_item(output_file, item, level = 0):
	output_file.write("\t" * level + 
		(item.rz + " " if item.rz else "") + (item.pr + " " if item.pr else "") + 
		(item.csr + " " if item.csr else "") + (item.vr + " " if item.vr else "") +
		item.name + " " + unicode(item.value) + "\r\n")
	for child in item.children:
		write_data_item(output_file, child, level + 1)

def do_write_text_document(output_file, document):
	output_file.write(document.caption + "\r\n")
	output_file.write(u" ".join(document.header) + "\r\n")
	for item in document.data:
		write_data_item(output_file, item)


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
		write_json_document(document, output_json_file_name, JsonEncoder_Budget2013_13)
	if output_json_pretty_file_name:
		write_json_pretty_document(document, output_json_pretty_file_name, JsonEncoder_Budget2013_13)
