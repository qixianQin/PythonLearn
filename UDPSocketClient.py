# -*- coding:utf-8 -*-

##  UDP  client 端
import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Hello', b'world']:
	s.sendto(data, ('127.0.0.1', 9999))
	print(s.recv(1024).decode('utf-8'))
s.close()