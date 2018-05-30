#  -*- conding:utf-8 -*- 

## 多线程  
##  有两种方式： 1、 os模块中的fork (仅适用于 Unix/Linux 操作系统)   运行失败
#               2、multiprocessing 模块

import  os
from multiprocessing import Process

def run_proc(name):
	print('Child process %s (%s) Running...' % (name, os.getpid()))

# def main():
# 	print('current process %s start ...' % os.getpid())
# 	pid = os.fork()
# 	if pid < 0:
# 		print('error in fork')
# 	elif pid == 0:
# 		print('I am child process %s and my parent process is %s' % (os.getpid(), os.getppid()))
# 	else:
# 		print('I %s created a child process %s' % (os.getpid(), pid))
if __name__ == '__main__':
	print('Parent process %s. ' % os.getpid())
	for i in range(5):
		p = Process(target = run_proc, args=(str(i),))
		print('Process will start.')
		p.start()
	p.join()
	print('Process end.')
	def main():