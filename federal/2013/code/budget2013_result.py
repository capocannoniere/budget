# coding: utf-8

import codecs
import re
import json
import argparse
import os
from budget2013_common import *
from budget2013_0 import Budget2013_0
from budget2013_1 import Budget2013_1, Budget2013_1_TableDataItem
from budget2013_2 import Budget2013_2
from budget2013_3 import Budget2013_3
from budget2013_4 import Budget2013_4
from budget2013_5 import Budget2013_5, Budget2013_5_DataItem
from budget2013_6 import Budget2013_6, Budget2013_6_DataItem
from budget2013_7 import Budget2013_7, Budget2013_7_DataItem
from budget2013_10 import Budget2013_10, Budget2013_10_DataItem
from budget2013_13 import Budget2013_13, Budget2013_13_DataItem
from budget2013_15 import Budget2013_15, Budget2013_15_DataItem
from budget2013_19 import Budget2013_19, Budget2013_19_DataItem
from budget2013_22 import Budget2013_22, Budget2013_22_DataItem
from budget2013_25 import Budget2013_25
from budget2013_26 import Budget2013_26
from budget2013_31 import Budget2013_31, Budget2013_31_Table
from budget2013_32 import Budget2013_32, Budget2013_32_Table
from budget2013_35 import Budget2013_35
from budget2013_36 import Budget2013_36
from budget2013_37 import Budget2013_37, Budget2013_37_SubTable1, Budget2013_37_SubTable1Item, Budget2013_37_SubTable2
from budget2013_38 import Budget2013_38, Budget2013_38_SubTable1, Budget2013_38_SubTable1Item, Budget2013_38_SubTable2
from budget2013_39 import Budget2013_39, Budget2013_39_SubTable, Budget2013_39_SubTable3, Budget2013_39_SubTable3Item, Budget2013_39_ReceiveItem
from budget2013_40 import Budget2013_40, Budget2013_40_SubTable, Budget2013_40_SubTable3, Budget2013_40_SubTable3Item, Budget2013_40_ReceiveItem
from budget2013_41 import Budget2013_41, Budget2013_41_SubTables, Budget2013_41_SubTable1, Budget2013_41_SubTable1Item, Budget2013_41_SubTable2
from budget2013_42 import Budget2013_42, Budget2013_42_SubTables, Budget2013_42_SubTable1, Budget2013_42_SubTable1Item, Budget2013_42_SubTable2
from budget2013_43 import Budget2013_43, Budget2013_43_TableItem
from budget2013_44 import Budget2013_44, Budget2013_44_TableItem

REVISION1 = "2012-12-03"
REVISION2 = "2013-06-07"
REVISION3 = "2013-12-02"

ANNEX_NUMBERS = ["01", "02", "03", "04", "05", "06", "07", "07.1", "07.2", "07-combined", "10", "13", "13.1", "13.2", "13-combined",
	"15", "19", "19.1", "19.2", "19-combined", "22", "25", "26", "31", "32", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44"]

PICKLE_EXTENSION = ".pkl"
TEXT_EXTENSION = ".txt"
JSON_EXTENSION = ".json"
JSON_PRETTY_EXTENSION = ".pretty.json"

class ResultBudget2013(object):
	def __init__(self):
		self._main_budget = None
		self._annexes = {}
	
	@property
	def main_budget (self):
		return self._main_budget 
	@main_budget .setter
	def main_budget (self, value):
		self._main_budget  = value
	
	@property
	def annexes(self):
		return self._annexes
	@annexes.setter
	def annexes(self, value):
		self._annexes = value

def is_annex_exists_for_revision(annex_no, revision):
	if revision == REVISION1:
		return annex_no not in ["07.1", "07.2", "13.1", "13.2", "19.1", "19.2"]
	elif revision == REVISION2:
		return annex_no not in ["07.2", "13.2", "19.2"]
	elif revision == REVISION3:
		return True
	else:
		raise Exception("Unknown revision " + revision)
		
def get_main_budget_file_name(revision, extension):
	return "budget-" + revision + extension

def get_annex_file_name(annex_no, revision, extension):
	return "annex" + annex_no + "-" + revision + extension

def get_annex_description(annex_no):
	if annex_no == "07-combined":
		return u"07 (итог)"
	elif annex_no == "13-combined":
		return u"13 (итог)"
	elif annex_no == "19-combined":
		return u"19 (итог)"
	else:
		return annex_no

def get_main_budget_path(revision, extension):
	main_budget_file_name = get_main_budget_file_name(revision, extension)
	main_budget_path = os.path.join(input_directory, main_budget_file_name)
	return main_budget_path

def get_annex_path(annex_no, revision, extension):
	annex_file_name = get_annex_file_name(annex_no, revision, extension)
	annex_path = os.path.join(input_directory, annex_file_name)
	return annex_path

def get_main_budget_pickle(revision):
	main_budget_path = get_main_budget_path(revision, PICKLE_EXTENSION)
	with open(main_budget_path, "rb") as main_budget_file:
		main_budget = pickle.load(main_budget_file)
		return main_budget

def get_annex_pickle(annex_no, revision):
	annex_path = get_annex_path(annex_no, revision, PICKLE_EXTENSION)
	with open(annex_path, "rb") as annex_file:
		annex = pickle.load(annex_file)
		return annex

def get_main_budget_text(revision):
	main_budget_path = get_main_budget_path(revision, TEXT_EXTENSION)
	with codecs.open(main_budget_path, "r", encoding = "utf-8") as main_budget_file:
		lines = main_budget_file.readlines()
		return lines

def get_annex_text(annex_no, revision):
	annex_path = get_annex_path(annex_no, revision, TEXT_EXTENSION)
	with codecs.open(annex_path, "r", encoding = "utf-8") as annex_file:
		lines = annex_file.readlines()
		return lines

def do_get_main_budget_json(revision, extension):
	main_budget_path = get_main_budget_path(revision, extension)
	with codecs.open(main_budget_path, "r", encoding = "utf-8") as main_budget_file:
		main_budget = json.load(main_budget_file)
		return main_budget

def get_main_budget_json(revision):
	return do_get_main_budget_json(revision, JSON_EXTENSION)

def get_main_budget_json_pretty(revision):
	return do_get_main_budget_json(revision, JSON_PRETTY_EXTENSION)

def do_get_annex_json(annex_no, revision, extension):
	annex_path = get_annex_path(annex_no, revision, extension)
	with codecs.open(annex_path, "r", encoding = "utf-8") as annex_file:
		annex = json.load(annex_file)
		return annex

def get_annex_json(annex_no, revision):
	return do_get_annex_json(annex_no, revision, JSON_EXTENSION)

def get_annex_json_pretty(annex_no, revision):
	return do_get_annex_json(annex_no, revision, JSON_PRETTY_EXTENSION)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--input_directory", dest="input_directory", required=True, help="Input directory")
	parser.add_argument("-r", "--revision", dest="revision", required=True, help="Budget revision")
	parser.add_argument("--output-pickle", dest="output_pickle_file_name", help="Path to the output pickle file")
	parser.add_argument("--output-text", dest="output_text_file_name", help="Path to the output text file")
	parser.add_argument("--output-json", dest="output_json_file_name", help="Path to the output JSON file")
	parser.add_argument("--output-json-pretty", dest="output_json_pretty_file_name", help="Path to the output JSON file with indents and russian letters")
	args = parser.parse_args()
	
	input_directory = args.input_directory
	revision = args.revision
	output_pickle_file_name = args.output_pickle_file_name
	output_text_file_name = args.output_text_file_name
	output_json_file_name = args.output_json_file_name
	output_json_pretty_file_name = args.output_json_pretty_file_name

	if (not output_pickle_file_name) and (not output_text_file_name) and (not output_json_file_name) and (not output_json_pretty_file_name):
		raise Exception("No output file specified")

	if output_pickle_file_name:
		result_budget = ResultBudget2013()
		result_budget.main_budget = get_main_budget_pickle(revision)
		annexes = {}
		for annex_no in ANNEX_NUMBERS:
			if is_annex_exists_for_revision(annex_no, revision):
				annex = get_annex_pickle(annex_no, revision)
				annexes[annex_no] = annex
		result_budget.annexes = annexes
		write_pickle_document(result_budget, output_pickle_file_name)
	
	if output_text_file_name:
		main_budget = get_main_budget_text(revision)
		annexes = {}
		for annex_no in ANNEX_NUMBERS:
			if is_annex_exists_for_revision(annex_no, revision):
				annex = get_annex_text(annex_no, revision)
				annexes[annex_no] = annex
		with codecs.open(output_text_file_name, "w", encoding = "utf-8") as output_file:
			output_file.write(u"БЮДЖЕТ:\r\n\r\n")
			for line in main_budget:
				output_file.write(line)
			output_file.write(u"\r\n\r\n\r\n\r\n\r\n")
			
			for annex_no in ANNEX_NUMBERS:
				if annex_no not in annexes:
					continue
				annex = annexes[annex_no]
				output_file.write(u"ПРИЛОЖЕНИЕ " + get_annex_description(annex_no) + u":\r\n\r\n")
				for line in annex:
					output_file.write(line)
				output_file.write(u"\r\n\r\n\r\n\r\n\r\n")

	if output_json_file_name:
		document = {}
		document["main_budget"] = get_main_budget_json(revision)
		document["annexes"] = {}
		for annex_no in ANNEX_NUMBERS:
			if is_annex_exists_for_revision(annex_no, revision):
				annex = get_annex_json(annex_no, revision)
				document["annexes"][annex_no] = annex
		with codecs.open(output_json_file_name, "w", encoding = "utf-8") as output_file:
			json.dump(document, output_file)

	if output_json_pretty_file_name:
		document = {}
		document["main_budget"] = get_main_budget_json_pretty(revision)
		document["annexes"] = {}
		for annex_no in ANNEX_NUMBERS:
			if is_annex_exists_for_revision(annex_no, revision):
				annex = get_annex_json_pretty(annex_no, revision)
				document["annexes"][annex_no] = annex
		with codecs.open(output_json_pretty_file_name, "w", encoding = "utf-8") as output_file:
			s = unicode(json.dumps(document, indent = 4))
			replaced = replace_json_unicode_symbols(s)
			output_file.write(replaced)
