# -*- conding:utf-8  -*- 

####   测试多线程

from multiprocessing.pool import Pool
import datetime

def main(self):
	k = 0
	for i in range(1,200000):
		# print('i:', i)
		k = k + 1

GROUP_START = 1
GROUP_END = 1

if __name__ == '__main__':
	starttime = datetime.datetime.now()
	pool = Pool()
	groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
	pool.map(main, groups)
	pool.close()
	pool.join()
	endtime = datetime.datetime.now()
	print('time:', (endtime - starttime).microseconds)