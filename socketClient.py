# -*- coding:utf-8 -*- 

##  socket 客户端

import socket 

# 初始化客户端
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接目标的IP 和端口
s.connect(('127.0.0.1', 9999))
#接收消息
print('--->>' + s.recv(1024).decode('utf-8'))
#发送消息
s.send(b'Hello, I am Client.')
print('---->>' + s.recv(1024).decode('utf-8'))
s.send(b'exit')
#关闭Socket 
s.close()

