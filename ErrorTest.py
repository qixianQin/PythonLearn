# -*- coding:utf-8 -*- 

from urllib import error, request

try:
	response = request.urlopen('http://cuiqingcai.com/index.htm')
except error.URLError as e:
	print(e.reason)
else:
	pass
finally:
	pass

##  Not Found  


from urllib import error, request

try:
	response = request.urlopen('http://cuiqingcai.com/index.htm')
except error.HTTPError as e:
	print(e.reason, e.code, e.headers, sep='\n')
finally:
	pass


# Not Found
# 404
# Server: nginx/1.10.3 (Ubuntu)
# Date: Fri, 20 Apr 2018 15:02:19 GMT
# Content-Type: text/html; charset=UTF-8
# Transfer-Encoding: chunked
# Connection: close
# Vary: Cookie
# Expires: Wed, 11 Jan 1984 05:00:00 GMT
# Cache-Control: no-cache, must-revalidate, max-age=0
# Link: <https://cuiqingcai.com/wp-json/>; rel="https://api.w.org/"


from urllib import error, request

try:
	response = request.urlopen('http://cuiqingcai.com/index.htm')
except error.HTTPError as e:      #  先捕获子类的异常，再去捕获父类的错误
	print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:     #   父类的异常，  由于抛出的异常为HTTPError的， 所以这里不会再捕获了   
	print(e.reason)
else:
	print('Request successfully!')
finally:
	pass

# Not Found
# 404
# Server: nginx/1.10.3 (Ubuntu)
# Date: Fri, 20 Apr 2018 15:09:28 GMT
# Content-Type: text/html; charset=UTF-8
# Transfer-Encoding: chunked
# Connection: close
# Vary: Cookie
# Expires: Wed, 11 Jan 1984 05:00:00 GMT
# Cache-Control: no-cache, must-revalidate, max-age=0
# Link: <https://cuiqingcai.com/wp-json/>; rel="https://api.w.org/"


import socket
from urllib import request, error

try:
	response = request.urlopen('http://www.baidu.com', timeout=0.001)
except error.URLError as e:
	print(type(e.reason))
	if isinstance(e.reason, socket.timeout):
		print('TIME OUT')
else:
	pass
finally:
	pass


# <class 'socket.timeout'>
# TIME OUT