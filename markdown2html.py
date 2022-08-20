#!/usr/bin/python3
''' write a script markdown2html.py that takes an argument of 2 strings: a markdown file and an html file'''

import sys
import os.path
import re
import hashlib

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print("Usage: ./markdown2html.py <markdown_file> <html_file>")
		exit(1)
	if not os.path.isfile(sys.argv[1]):
		print("Missing {}".format(sys.argv[1]))
		exit(1)
	if os.path.isfile(sys.argv[2]):
		print("File {} already exists".format(sys.argv[2]))
		exit(1)
	with open(sys.argv[1], 'r') as f:
		text = f.read()
	text = re.sub(r'\n\n', '\n', text)
	text = re.sub(r'\n', '<br />\n', text)
	text = re.sub(r'\*(.*)\*', r'<em>\1</em>', text)
	text = re.sub(r'_(.*)_', r'<em>\1</em>', text)
	text = re.sub(r'\[(.*)\]\((.*)\)', r'<a href="\2">\1</a>', text)
	text = re.sub(r'\#(.*)', r'<h1>\1</h1>', text)
	text = re.sub(r'\##(.*)', r'<h2>\1</h2>', text)
	text = re.sub(r'\###(.*)', r'<h3>\1</h3>', text)
	text = re.sub(r'\####(.*)', r'<h4>\1</h4>', text)
	text = re.sub(r'\#####(.*)', r'<h5>\1</h5>', text)
	text = re.sub(r'\######(.*)', r'<h6>\1</h6>', text)
	text = re.sub(r'\> (.*)', r'<blockquote>\1</blockquote>', text)