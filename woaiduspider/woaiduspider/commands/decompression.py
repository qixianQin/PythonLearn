# -*- coding:utf-8 -*- 

"""
Deconpression all the zip and rar files in the specific directory 
"""

import os 
import zipfile 
import traceback
import argparse
from pprint import pprint 

def find_path_file(specific_file, search_directroy):
	"""
	result_path_filename
	"""
	result_path_filename = list()
	result_path_filename.extend([os.path.join(dirpath,filename) for dirpath, dirnames, filenames in os.walk(search_directroy) for filename in filenames if os.path.splitext(filename)[1]==('.'+specific_file)])
	return result_path_filename

def Decompression_rar(specific_file):
	"""
	Decompression_rar
	if you want use this function, you need install unrar, for ubuntu:
		sudo apt-get install unrar

		another decompression method is to use: rarfile, for help can visit:
		http://www.pythonclub.org/python-files/rar
	"""

	cmd = 'unrar x" '  + specific_file + '"' +' "' + os.path.split(specific_file)[0] + '"'
	os.system(cmd) 

def Decompression_zip(specific_file):
	"""
	Decompression_zip
	"""

	if zipfile.is_zipfile(specific_file):
		try:
			zipfile.ZipFile(specific_file).extractall(os.path.split(specific_file)[0])
		except Exception as e:
			traceback.print_ext()


if __name__ == '__main__':
	parser = argparse.ArgumentParse()
	parse.add_argument("-d", "--delsource", action='store_true', help="delete the source file(rar or zip)")
	args = parser.parse_args()

	path = os.path.abspath(os.path.dirname(__file__)) +"/../media/book_files"

	_rar = find_path_file('rar', path)
	for i in _rar:
		Decompression_rar(i)

	_zip = find_path_file('zip', path)
	for i in _zip:
		Decompression_zip(i)

	if args.delsource:
		_delete_rar = find_path_file('rar', path)
		_delete_zip = find_path_file('zip', path)
		for i in _delete_rar:
			os.remove(i)

		for i in _delete_zip:
			os.remove(i)