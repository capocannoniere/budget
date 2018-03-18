# coding: utf-8

import codecs
import re
import pickle
import argparse
from budget2013_common import *
import budget2013_13
import copy


def process_item(item):
	value = r"(?:\+|\-)\d\d?\d?( \d{3})*,\d+?"
	re_total = re.compile(r"(?:\s+(" + value + ")?)?$")
	regexps = [
		re.compile(r"\s+(\d{2})(?:\s\s+(" + value + ")?)?$"),
		re.compile(r"\s+(\d{2})\s+(\d{2})(?:\s+(" + value + ")?)?$"),
		re.compile(r"\s+(\d{2})\s+(\d{2})\s+(\d{7})(?:\s+(" + value + ")?)?$"),
		re.compile(r"\s+(\d{2})\s+(\d{2})\s+(\d{7})\s+(\d{3})(?:\s+(" + value + ")?)?$")
	]

	results = []
	success_count = 0
	for regexp in regexps:
		m = regexp.search(item)
		if m:
			success_count += 1
		results.append(m)
	
	if success_count == 2 and results[0] and results[1]:
		results[0] = None
		success_count = 1
	
	if success_count == 0:
		m = re_total.search(item)
		if m:
			name = item[:-len(m.group(0))].strip()
			if name == u"ВСЕГО":
				return (name, None, None, None, None, parse_value(m.group(1)) if m.group(1) else 0.0)
		print item
		raise Exception(u"No match for item data '{0}'".format(item))
	elif success_count == 1:
		if results[0]:
			return (item[:-len(results[0].group(0))].strip(), results[0].group(1), None, None, None, parse_value(results[0].group(2)) if results[0].group(2) else 0.0)
		elif results[1]:
			return (item[:-len(results[1].group(0))].strip(), results[1].group(1), results[1].group(2), None, None, parse_value(results[1].group(3)) if results[1].group(3) else 0.0)
		elif results[2]:
			return (item[:-len(results[2].group(0))].strip(), results[2].group(1), results[2].group(2), results[2].group(3), None, parse_value(results[2].group(4)) if results[2].group(4) else 0.0)
		elif results[3]:
			return (item[:-len(results[3].group(0))].strip(), results[3].group(1), results[3].group(2), results[3].group(3), results[3].group(4), parse_value(results[3].group(5)) if results[3].group(5) else 0.0)
		
		raise Exception("We should not get here.")
	else:
		success_results = [(result_index, result.re.pattern) for result_index, result in enumerate(results) if result]
		indices = map(lambda t: str(t[0]), success_results)
		patterns = map(lambda t: t[1], success_results)
		
		print u"Ambiguous match ({0}) for item data '{1}': matched {2}".format(",".join(indices), item, " and ".join(patterns))
		return (None, None, None, None, None, 0.0)

def process_items(items, document):
	for item in items:
		(name, rz, pr, csr, vr, value) = process_item(item)
		
		if name:
			while name.find("  ") != -1:
				name = name.replace("  ", " ")
		
		data_item = budget2013_13.Budget2013_13_DataItem()
		data_item.name = name
		data_item.rz = rz
		data_item.pr = pr
		data_item.csr = csr
		data_item.vr = vr
		data_item.value = value
		document.data.append(data_item)

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

def check_item_values(item):
	if item.children:
		children_value = get_item_children_sum(item)
		if not numbers_equal(item.value, children_value):
			print u"Values are NOT equal: ({0}), value {1} and its children, value {2}, diff={3}.".format(get_item_short_name(item), item.value, children_value, item.value - children_value)
		for child in item.children:
			check_item_values(child)

def check_document(document):
	for item in document.data:
		check_item_values(item)

def find_by_csr(item, current_item):
	if current_item.csr == item.csr:
		return current_item
	
	for child in current_item.children:
		found = find_by_csr(item, child)
		if found:
			return found
	
	return None

def find_by_vr(item, current_item):
	if current_item.vr == item.vr:
		return current_item
	
	for child in current_item.children:
		found = find_by_vr(item, child)
		if found:
			return found
	
	return None

def find_item(item, combined_document):
	current_item = combined_document.data[0]
	
	if not item.rz:
		return current_item
	for child in current_item.children:
		if child.rz == item.rz:
			current_item = child
			break
	if current_item.rz != item.rz:
		return None
	
	if not item.pr:
		return current_item
	for child in current_item.children:
		if child.pr == item.pr:
			current_item = child
			break
	if current_item.pr != item.pr:
		return None
	
	if not item.csr:
		return current_item
	found_item = find_by_csr(item, current_item)
	if not found_item:
		return None
	current_item = found_item
	
	if not item.vr:
		return current_item
	found_item = find_by_vr(item, current_item)
	if not found_item:
		return None
	current_item = found_item
	
	return current_item

def sort_items(item1, item2):
	if not item1.rz:
		return 0
	if item1.rz < item2.rz:
		return -1
	elif item1.rz > item2.rz:
		return 1
	
	if not item1.pr:
		return 0
	if item1.pr < item2.pr:
		return -1
	elif item1.pr > item2.pr:
		return 1
	
	if not item1.csr:
		return 0
	if item1.csr < item2.csr:
		return -1
	elif item1.csr > item2.csr:
		return 1
	
	if not item1.vr:
		return 0
	if item1.vr < item2.vr:
		return -1
	elif item1.vr > item2.vr:
		return 1
	
	return 0

def patch_item(item, combined_document):
	combined_item = find_item(item, combined_document)
	if not combined_item:
		combined_item_parent = find_item(item.parent, combined_document)
		
		#combined_item = copy.deepcopy(item)
		combined_item = budget2013_13.Budget2013_13_DataItem()
		combined_item.name = item.name
		combined_item.rz = item.rz
		combined_item.pr = item.pr
		combined_item.csr = item.csr
		combined_item.vr = item.vr
		combined_item.value = item.value
		combined_item.parent = combined_item_parent
		combined_item_parent.children.append(combined_item)
		
		combined_item_parent.children.sort(cmp = sort_items)
	else:
		if item.name != combined_item.name:
			print "Names are different:"
			print item.name
			print combined_item.name
			print
		combined_item.value += item.value
	
	if combined_item.vr:
		parent = combined_item.parent
		while parent and parent.vr:
			parent.value = get_item_children_sum(parent)
			parent = parent.parent
	elif combined_item.csr:
		parent = combined_item.parent
		while parent and parent.csr:
			parent.value = get_item_children_sum(parent)
			parent = parent.parent
	
	if item.children:
		for child in item.children:
			patch_item(child, combined_document)

def patch_document(main_document, document):
	combined_document = copy.deepcopy(main_document)
	
	for item in document.data:
		patch_item(item, combined_document)
	
	return combined_document

def correct_document_items(document, rz, pr, csr, vr, child_vrs, name):
	item = budget2013_13.Budget2013_13_DataItem()
	item.rz = rz
	item.pr = pr
	item.csr = csr
	item.vr = child_vrs[0]
	found_item = find_item(item, document)
	
	new_item = budget2013_13.Budget2013_13_DataItem()
	new_item.rz = rz
	new_item.pr = pr
	new_item.csr = csr
	new_item.vr = vr
	new_item.name = name
	new_item.parent = found_item.parent
	found_item.parent.children.append(new_item)
	new_item.children.append(found_item)
	found_item.parent = new_item
	new_item.parent.children.remove(found_item)
	
	for child_vr in child_vrs[1:]:
		item = budget2013_13.Budget2013_13_DataItem()
		item.rz = rz
		item.pr = pr
		item.csr = csr
		item.vr = child_vr
		found_item = find_item(item, document)
		
		new_item.children.append(found_item)
		found_item.parent = new_item
		new_item.parent.children.remove(found_item)
		
	value = 0.0
	for child in new_item.children:
		value += child.value
	new_item.value = value
	
	new_item.parent.children.sort(cmp = sort_items)

def correct_document(document):
	'''
	correct_document_items(document, "07", "05", "4299900", "610", ["611", "612"], u"Субсидии бюджетным учреждениям")
	correct_document_items(document, "03", "13", "0819900", "110", ["111", "112"], u"Расходы на выплаты персоналу казенных учреждений")
	correct_document_items(document, "07", "06", "4309900", "110", ["111", "112"], u"Расходы на выплаты персоналу казенных учреждений")
	'''

def get_document(input_file_name):
	with codecs.open(input_file_name, "r", encoding = "utf-8") as input_file:
		input_data = input_file.readlines()
		
		document = budget2013_13.Budget2013_13()
		
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
		line = input_data[line_index].strip()
		line_index += 2
		document.header = line.split(";")
		
		#data
		items = []
		while line_index < len(input_data):
			data_line = input_data[line_index].strip()
			line_index += 1
			items.append(data_line)
		
		process_items(items, document)
		
		check_items_order(document)
		group_items(document)
		check_document(document)
		
		return document

def get_combined_document(main_document, document):
	combined_document = patch_document(main_document, document)

	check_items_order(combined_document)
	check_document(combined_document)
	
	return combined_document

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
	parser = argparse.ArgumentParser()
	parser.add_argument("-m", "--main-input", dest="main_input_file_name", required=True, help="Path to the combined annex13 + annex13.1 pickle file")
	parser.add_argument("-i", "--input", dest="input_file_name", required=True, help="Path to the annex13.2 text file")
	
	parser.add_argument("--output-pickle", dest="output_pickle_file_name", help="Path to the output pickle file for annex13.2")
	parser.add_argument("--output-text", dest="output_text_file_name", help="Path to the output text file for annex13.2")
	parser.add_argument("--output-json", dest="output_json_file_name", help="Path to the output JSON file for annex13.2")
	parser.add_argument("--output-json-pretty", dest="output_json_pretty_file_name", help="Path to the output JSON file with indents and russian letters for annex13.2")
	
	parser.add_argument("--combined-output-pickle", dest="combined_output_pickle_file_name", help="Path to the output pickle file for combined annex13 + annex13.1 + annex13.2")
	parser.add_argument("--combined-output-text", dest="combined_output_text_file_name", help="Path to the output text file for combined annex13 + annex13.1 + annex13.2")
	parser.add_argument("--combined-output-json", dest="combined_output_json_file_name", help="Path to the output JSON file for combined annex13 + annex13.1 + annex13.2")
	parser.add_argument("--combined-output-json-pretty", dest="combined_output_json_pretty_file_name", help="Path to the output JSON file with indents and russian letters for combined annex13 + annex13.1 + annex13.2")

	args = parser.parse_args()

	main_input_file_name = args.main_input_file_name
	input_file_name = args.input_file_name
	
	output_pickle_file_name = args.output_pickle_file_name
	output_text_file_name = args.output_text_file_name
	output_json_file_name = args.output_json_file_name
	output_json_pretty_file_name = args.output_json_pretty_file_name

	combined_output_pickle_file_name = args.combined_output_pickle_file_name
	combined_output_text_file_name = args.combined_output_text_file_name
	combined_output_json_file_name = args.combined_output_json_file_name
	combined_output_json_pretty_file_name = args.combined_output_json_pretty_file_name

	if (not output_pickle_file_name) and (not output_text_file_name) and (not output_json_file_name) and (not output_json_pretty_file_name):
		raise Exception("No output file specified for annex13.1")

	if (not combined_output_pickle_file_name) and (not combined_output_text_file_name) and (not combined_output_json_file_name) and (not combined_output_json_pretty_file_name):
		raise Exception("No output file specified for combined annex13 + annex13.1")

	with open(main_input_file_name, "rb") as main_document_file:
		main_document = pickle.load(main_document_file)
	correct_document(main_document)
	document = get_document(input_file_name)
	combined_document = get_combined_document(main_document, document)

	if output_pickle_file_name:
		write_pickle_document(document, output_pickle_file_name)
	if output_text_file_name:
		write_text_document(document, output_text_file_name, do_write_text_document)
	if output_json_file_name:
		write_json_document(document, output_json_file_name, budget2013_13.JsonEncoder_Budget2013_13)
	if output_json_pretty_file_name:
		write_json_pretty_document(document, output_json_pretty_file_name, budget2013_13.JsonEncoder_Budget2013_13)

	if combined_output_pickle_file_name:
		write_pickle_document(combined_document, combined_output_pickle_file_name)
	if combined_output_text_file_name:
		write_text_document(combined_document, combined_output_text_file_name, budget2013_13.do_write_text_document)
	if combined_output_json_file_name:
		write_json_document(combined_document, combined_output_json_file_name, budget2013_13.JsonEncoder_Budget2013_13)
	if combined_output_json_pretty_file_name:
		write_json_pretty_document(combined_document, combined_output_json_pretty_file_name, budget2013_13.JsonEncoder_Budget2013_13)
