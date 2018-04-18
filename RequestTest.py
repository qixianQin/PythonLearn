# -*- coding:utf-8 -*-
from urllib import request
req = request.Request('http://python.org')
response = request.urlopen(req)
# print(response.read().decode('utf-8'))

#   返回 python.org 页面 的源码

from urllib import parse
from urllib import request

data = bytes(parse.urlencode({'word':'python'}), encoding='utf-8')
req = request.Request('http://httpbin.org/post', data=data)
response = request.urlopen(req)
print(response.read())

#b'{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {\n    "word": "python"\n  }, \n  "headers": {\n    "Accept-Encoding": "identity", \n    "Connection": "close", \n    "Content-Length": "11", \n    "Content-Type": "application/x-www-form-urlencoded", \n    "Host": "httpbin.org", \n    "User-Agent": "Python-urllib/3.6"\n  }, \n  "json": null, \n  "origin": "121.34.54.62", \n  "url": "http://httpbin.org/post"\n}\n'



from urllib import request, parse
url = 'http://httpbin.org/post'
# headers = {
# 	'User-Agent':'Mozilla/4/0(compatible; MSIE 5.5; windows NT)',
# 	'Host':'httpbin.org'
# }
dict = {
	'name':'Germey'
}
data=bytes(parse.urlencode(dict), encoding='utf-8')
# req = request.Request(url=url, data=data, headers=headers,method='POST')
req = request.Request(url=url, data=data, method='POST')
req.add_header('User-Agent','Mozilla/4/0(compatible; MSIE 5.5; windows NT)')
req.add_header('Host','httpbin.org')
response = request.urlopen(req)
print(response.read().decode('utf-8'))

# {
#   "args": {}, 
#   "data": "", 
#   "files": {}, 
#   "form": {
#     "name": "Germey"
#   }, 
#   "headers": {
#     "Accept-Encoding": "identity", 
#     "Connection": "close", 
#     "Content-Length": "11", 
#     "Content-Type": "application/x-www-form-urlencoded", 
#     "Host": "httpbin.org", 
#     "User-Agent": "Mozilla/4/0(compatible; MSIE 5.5; windows NT)"
#   }, 
#   "json": null, 
#   "origin": "121.34.54.62", 
#   "url": "http://httpbin.org/post"
# }