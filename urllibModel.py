# -*- coding:utf-8 -*-

# test for urlopen method
from urllib import request
response = request.urlopen('https://www.python.org')
#  输出整个页面的源码
#print(response.read().decode('utf-8'))
#    type()   响应的类型   <class 'http.client.HTTPResponse'>
print(type(response))
# 方法： read（）、readinto（）、getheader(name)|getheaders()|fileno()
# 属性： msg|version|status|debuglevel|closed
#print(response.readinto(5))     #    Reads up to the next len(b) bytes of the response body into the buffer b. Returns the number of bytes read.
print(response.getheaders())      #[('Server', 'nginx'), ('Content-Type', 'text/html; charset=utf-8'), ('X-Frame-Options', 'SAMEORIGIN'), ('x-xss-protection', '1; mode=block'), ('X-Clacks-Overhead', 'GNU Terry Pratchett'), ('Via', '1.1 varnish'), ('Content-Length', '49285'), ('Accept-Ranges', 'bytes'), ('Date', 'Tue, 17 Apr 2018 15:31:37 GMT'), ('Via', '1.1 varnish'), ('Age', '995'), ('Connection', 'close'), ('X-Served-By', 'cache-iad2142-IAD, cache-hnd18724-HND'), ('X-Cache', 'HIT, HIT'), ('X-Cache-Hits', '4, 5'), ('X-Timer', 'S1523979097.386329,VS0,VE0'), ('Vary', 'Cookie'), ('Strict-Transport-Security', 'max-age=63072000; includeSubDomains')]
print(response.getheader('Server'))      #   nginx
print(response.fileno())      # 764
print(response.msg)           #OK
print(response.status)        #200
print(response.version)       #11     10 for HTTP/1.0, 11 for HTTP/1.1.
print(response.debuglevel)    #0
print(response.reason)        #OK
#print(readinto.closed)       # 


#  测试  urlopen() 中的 data 参数
from urllib import parse
from urllib import request
#传递一个参数 word: python     使用 bytes() 方法转换成字节流， 该方法第一个参数需要是str(字符串类型)
# 需要使用 urlencode() 转换成字符串  ，  第二个参数指定编码格式
data = bytes(parse.urlencode({'word':'python'}), encoding='utf-8')
#	http://httpbin.org/post  提供HTTP请求测试
response = request.urlopen('http://httpbin.org/post', data=data)
print(response.read())


#b'{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {\n    
#"word": "python"\n  }, \n  "headers": {\n    "Accept-Encoding": "identity", \n    "Connection": "close", \n    "Content-Length": "11", \n    "Content-Type": "application/x-www-form-urlencoded", \n    "Host": "httpbin.org", \n    "User-Agent": "Python-urllib/3.6"\n  }, \n  "json": null, \n  "origin": "121.34.54.62", \n  "url": "http://httpbin.org/post"\n}\n'


# 测试  urlopen() 中timeout 参数     单位： 秒
from urllib import request
response = request.urlopen('http://httpbin.org/get', timeout=1)
print(response.read())

#During handling of the above exception, another exception occurred:  
#urllib.error.URLError: <urlopen error timed out>   

# 如果不超时，则返回：  b'{\n  "args": {}, \n  "headers": {\n    "Accept-Encoding": "identity", \n    "Connection": "close", \n    "Host": "httpbin.org", \n    "User-Agent": "Python-urllib/3.6"\n  }, \n  "origin": "121.34.54.62", \n  "url": "http://httpbin.org/get"\n}\n'

import socket
from urllib import request
from urllib import error

try:
	response = request.urlopen('http://httpbin.org/get', timeout=0.1)
except error.URLError as e:
	if isinstance(e.reason, socket.timeout):
		print('TIME OUT')

# TIME OUT   


