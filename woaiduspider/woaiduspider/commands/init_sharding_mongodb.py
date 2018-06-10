# -*- coding:utf-8 -*- 


"""
	This file is initiate mongodb situation 
	when you want to save book file in gridfs, then you need a sharding cluster,
	that the database design is:

	collections:
		book_detail
		book_file

	fields:
		book_detail:
			book_name:string
			alias_name: vector
			author:vector
			book_description:string
			book_covor_image_url:string
			book_covor_image_path:string
			book_download:vector
			book_file_id:gridfs_if
			book_file_url:string
			original_url:string
			update_time:datetime
		bood_file:
			book_file.chunks:
				_id
				files_id
				n
				data
			book_file.files:
				_id
				length
				chunkSize
				uploadDate
				md5
				filename
				contentType
				aliases
				metadata
		index:
			book_name
			alias_name
			author
		sharding key:
			update_time + book_name

		so what this do is to delete books_mongo if it has existed, and initiate the sharding cluster

		NOTE:
		for killall mongo procs after terminate the file process, you need use CTRL + C. 
		Befor you run this file, you need type this in a shell: sudo killall mongod.
		For check the info about all mongos, use the command: netstat -lntp|grep mongo

		ABOUT:
		This code mostly comes from:

"""

import os 
import sys
import shutil 
import pymongo
import types
import atexit

from socket import error, socket, AF_INET, SOCK_STREAM
from pymongo import ASCENDING, DESCENDING
from pymongo import MongoClient
from select import select 
from subprocess import Popen, PIPE, STDOUT
from threading import Thread
from time import sleep

try:
	#new pymongo
	from bson.son import SON
except ImportError:
	from pymongo.son import SON

ShardMONGODB_DB = "books_mongo"
GrifFs_Collection = "bool_file"

BASE_DATA_PATH = '/data/db/sharding/'
MONGO_PATH = os.getenv("MONGO_HOME", os.path.expanduser('~/10gen/mongo'))
N_SHARDS = 3
N_CONFIG = 1
N_MONGOS = 1
CHUNK_SIZE = 64
MONGOS_PORT = 27017
USE_SSL = False


CONFIG_ARGS = []
MONGOS_ARGS = []
MONGOD_ARGS = []

USE_VALGRIND = False
VALGRIND_ARGS  = ["valgrind", "--log-file=/tmp/mongos-%p.valgrind", "--leak-check=yes", ("--suppressions=" + MONGO_PATH + "valgrind.suppressions"), "--"]

