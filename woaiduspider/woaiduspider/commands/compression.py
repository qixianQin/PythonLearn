# -*- coding:utf-8 -*- 
"""
compress all the zip and rar files in the specific directory 
"""

import os 
import zipfile 
import traceback 
import argparse
import shutil
from pprint import pprint

def Compress_zip(raw_dir):
	"""
		Compres_zip
	"""
	target_zipfile = raw_dir + ".zip"
	cmd = 'zip -r -j "' + target_zipfile + '" ' + ' "' + raw_dir +'"'
	os.system(cmd)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", "--delsource", action='store_true', help="delete the source dirctory")
	args = parse.parse_args()

	path = os.path.abspath(os.path.dirname(__file__)) + "/../media/book_files"
	compress_path = []
	for i in os.listdir(path):
		compress_path.extend([os.path.join(path,i,j) for j in os.listdir(os.path.join(path,i))])

	for i in compress_path:
		Compres_zip(i)
	if args.delsource:
		for i in compress_path:
			shutil.rmtree(i,True)