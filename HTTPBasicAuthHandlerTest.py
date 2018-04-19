# -*- coding:utf-8 -*-
from urllib.request import HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'username'
password = 'password'
url = 'http://localhost:5000/'
p = HTTPPassworkMgrDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
	result = opener.open(url)
	html = result.read().decode('utf-8')
	print(html)
except URLError as e:
	print(e.reason)



# # 代理
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener	

proxy_handler = ProxyHandler({
	'http':'http://127.0.0.1:9743',
	'https':'https://127.0.0.1:9743'
	})

opener = build_opener(proxy_handler)
try:
	response = opener.open('https://www.baidu.com')
	print(response.read().decode('utf-8'))
except URLError as e:
	print(e.reason)
else:
	pass
finally:
	pass




#  cookie  
from http import cookiejar
from urllib import request

cookie = cookiejar.CookieJar()
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
response = opener.open('https://www.baidu.com')
for item in cookie:
	print(item.name + "=" + item.value)

# BIDUPSID=2420AA527732C232F6AF9640A2EBEEF9
# PSTM=1524151892
# BD_NOT_HTTPS=1

filename = 'cookie.txt'
cookie = cookiejar.MozillaCookieJar(filename)
filename = 'cookie'
cookie = cookiejar.LWPCookieJar(filename)
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
response = opener.open('https://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

# 生成一个cookie.txt文件， 在同级目录文件下面
# 如果要生成一个 LWP格式， 则名字名 不可以有后缀 (.txt)

from http import cookiejar
from urllib import request

cookie = cookiejar.LWPCookieJar()
cookie.load('cookie', ignore_discard=True, ignore_expires=True)
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))