# coding: utf-8

import codecs
import pickle
import json
import re
import argparse

def join_lines(lines):
	return " ".join([line.strip() for line in lines])

epsilon = 1e-4
def numbers_equal(n1, n2):
	return abs(n1 - n2) < epsilon

def parse_value(s):
	return float(s.replace(",", ".").replace(" ", ""))

class JsonSimpleEncoder(json.JSONEncoder):
	def default(self, o):
		return o.__dict__

def write_pickle_document(document, output_file_name):
	with open(output_file_name, "wb") as output_file:
		pickle.dump(document, output_file)

def write_text_document(document, output_file_name, write_func):
	with codecs.open(output_file_name, "w", encoding = "utf-8") as output_file:
		write_func(output_file, document)

def write_json_document(document, output_file_name, json_encoder_class):
	with open(output_file_name, "w") as output_file:
		json.dump(document, output_file, cls = json_encoder_class)

def write_json_pretty_document(document, output_file_name, json_encoder_class):
	with codecs.open(output_file_name, "w", encoding = "utf-8") as output_file:
		s = json.dumps(document, cls = json_encoder_class, indent = 4)
		replaced = replace_json_unicode_symbols(s)
		output_file.write(replaced)

def replace_json_unicode_symbols(s):
	replaced = re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: unichr(int(m.group(1), 16)), s)
	return replaced

def get_default_argument_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--input", dest="input_file_name", required=True, help="Path to the input text file")
	parser.add_argument("--output-pickle", dest="output_pickle_file_name", help="Path to the output pickle file")
	parser.add_argument("--output-text", dest="output_text_file_name", help="Path to the output text file")
	parser.add_argument("--output-json", dest="output_json_file_name", help="Path to the output JSON file")
	parser.add_argument("--output-json-pretty", dest="output_json_pretty_file_name", help="Path to the output JSON file with indents and russian letters")
	return parser
