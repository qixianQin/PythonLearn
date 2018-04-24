# -*- coding:utf-8 -*-

#  通过指令安装：   pip3 install requests    该模块
import requests 

response = requests.get('https://www.baidu.com')
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)


# <class 'requests.models.Response'>
# 200
# <class 'str'>
# <!DOCTYPE html>
# <!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge><meta content=always name=referrer><link rel=stylesheet type=text/css href=https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/bdorz/baidu.min.css><title>ç¾åº¦ä¸ä¸ï¼ä½ å°±ç¥é</title></head> <body link=#0000cc> <div id=wrapper> <div id=head> <div class=head_wrapper> <div class=s_form> <div class=s_form_wrapper> <div id=lg> <img hidefocus=true src=//www.baidu.com/img/bd_logo1.png width=270 height=129> </div> <form id=form name=f action=//www.baidu.com/s class=fm> <input type=hidden name=bdorz_come value=1> <input type=hidden name=ie value=utf-8> <input type=hidden name=f value=8> <input type=hidden name=rsv_bp value=1> <input type=hidden name=rsv_idx value=1> <input type=hidden name=tn value=baidu><span class="bg s_ipt_wr"><input id=kw name=wd class=s_ipt value maxlength=255 autocomplete=off autofocus=autofocus></span><span class="bg s_btn_wr"><input type=submit id=su value=ç¾åº¦ä¸ä¸ class="bg s_btn" autofocus></span> </form> </div> </div> <div id=u1> <a href=http://news.baidu.com name=tj_trnews class=mnav>æ°é»</a> <a href=https://www.hao123.com name=tj_trhao123 class=mnav>hao123</a> <a href=http://map.baidu.com name=tj_trmap class=mnav>å°å¾</a> <a href=http://v.baidu.com name=tj_trvideo class=mnav>è§é¢</a> <a href=http://tieba.baidu.com name=tj_trtieba class=mnav>è´´å§</a> <noscript> <a href=http://www.baidu.com/bdorz/login.gif?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2f%3fbdorz_come%3d1 name=tj_login class=lb>ç»å½</a> </noscript> <script>document.write('<a href="http://www.baidu.com/bdorz/login.gif?login&tpl=mn&u='+ encodeURIComponent(window.location.href+ (window.location.search === "" ? "?" : "&")+ "bdorz_come=1")+ '" name="tj_login" class="lb">ç»å½</a>');
#                 </script> <a href=//www.baidu.com/more/ name=tj_briicon class=bri style="display: block;">æ´å¤äº§å</a> </div> </div> </div> <div id=ftCon> <div id=ftConw> <p id=lh> <a href=http://home.baidu.com>å³äºç¾åº¦</a> <a href=http://ir.baidu.com>About Baidu</a> </p> <p id=cp>&copy;2017&nbsp;Baidu&nbsp;<a href=http://www.baidu.com/duty/>ä½¿ç¨ç¾åº¦åå¿è¯»</a>&nbsp; <a href=http://jianyi.baidu.com/ class=cp-feedback>æè§åé¦</a>&nbsp;äº¬ICPè¯030173å·&nbsp; <img src=//www.baidu.com/img/gs.gif> </p> </div> </div> </div> </body> </html>

# <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>


import requests 
response = requests.get('http://httpbin.org/get')    #  get() 方法
print(response.text)

# {
#   "args": {}, 
#   "headers": {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Connection": "close", 
#     "Host": "httpbin.org", 
#     "User-Agent": "python-requests/2.18.4"
#   }, 
#   "origin": "121.34.53.82", 
#   "url": "http://httpbin.org/get"
# }

##  get() 带参数的
import requests 
response = requests.get('http://httpbin.org/get?name=germey&age=22')   #  直接将参数放入URL 后面
print(response.text)

# {
#   "args": {
#     "age": "22", 
#     "name": "germey"
#   }, 
#   "headers": {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Connection": "close", 
#     "Host": "httpbin.org", 
#     "User-Agent": "python-requests/2.18.4"
#   }, 
#   "origin": "121.34.53.82", 
#   "url": "http://httpbin.org/get?name=germey&age=22"
# }


import requests 
data={
	'name':'germey',
	'age':33
}
response = requests.get('http://httpbin.org/get', params=data)   #  直接将参数放入URL 后面
print(response.text)

# {
#   "args": {
#     "age": "33", 
#     "name": "germey"
#   }, 
#   "headers": {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Connection": "close", 
#     "Host": "httpbin.org", 
#     "User-Agent": "python-requests/2.18.4"
#   }, 
#   "origin": "121.34.53.82", 
#   "url": "http://httpbin.org/get?name=germey&age=33"
# }

import requests 
from json.decoder import JSONDecodeError

try:
	respone = requests.get('http://httpbin.org/get')
	print(type(respone.text))    #   字符
	print(respone.json())
	print(type(respone.json()))   #  json 转成了  字典,  若不能转换成JSON， 则会抛出 JSONDecodeError异常
except JSONDecodeError as e:
	print(e)
else:
	pass
finally:
	pass

# <class 'str'>
# {'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'close', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.18.4'}, 'origin': '121.34.53.82', 'url': 'http://httpbin.org/get'}
# <class 'dict'>

import requests 
import re

# headers = {
# 	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
# }

# response = requests.get('https://github.com', headers=headers)
# print(type(response))
# print(response.text)
# pattern = re.compile('<a.*?>(.*?)</a>', re.S)
# title = re.findall(pattern, response.text)
# print(title)

###   通过requests.get（）  获取得到页面源码， 然后再通过 正则表达式 获取其中的信息


import requests 

# response = requests.get('https://github.com/favicon.ico')    #  获取图片， 输出了该图片的二进制流
# print(response.text)
# print(response.content)


# import requests 
# response = requests.get('http://github.com/favicon.ico')
# with open('favicon.ico', 'wb') as f:
# 	f.write(response.content)

##  保存图片




#### requests   post
import requests
data={
	'name':'germey',
	'age':99
}
response = requests.post('http://httpbin.org/post', data=data)
print(response.text)

# {
#   "args": {}, 
#   "data": "", 
#   "files": {}, 
#   "form": {
#     "age": "99", 
#     "name": "germey"
#   }, 
#   "headers": {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Connection": "close", 
#     "Content-Length": "18", 
#     "Content-Type": "application/x-www-form-urlencoded", 
#     "Host": "httpbin.org", 
#     "User-Agent": "python-requests/2.18.4"
#   }, 
#   "json": null, 
#   "origin": "121.34.53.82", 
#   "url": "http://httpbin.org/post"
# }


import requests 
response = requests.get('http://jianshu.com')
print(type(response.status_code), response.status_code)
print(type(response.headers), response.headers)
print(type(response.cookies), response.cookies)
print(type(response.url) , response.url)
print(type(response.history), response.history)

# <class 'int'> 403
# <class 'requests.structures.CaseInsensitiveDict'> {'Date': 'Sun, 22 Apr 2018 03:46:31 GMT', 'Server': 'Tengine', 'Content-Type': 'text/html', 'Transfer-Encoding': 'chunked', 'Strict-Transport-Security': 'max-age=31536000; includeSubDomains; preload', 'Content-Encoding': 'gzip', 'X-Via': '1.1 shx191:10 (Cdn Cache Server V2.0), 1.1 PSfjfzdx2mj93:9 (Cdn Cache Server V2.0), 1.1 zhuhaidianxin15:6 (Cdn Cache Server V2.0)', 'Connection': 'close'}
# <class 'requests.cookies.RequestsCookieJar'> <RequestsCookieJar[]>
# <class 'str'> https://www.jianshu.com/
# <class 'list'> [<Response [301]>, <Response [301]>]

import requests 

# response = requests.get('http://www.baidu.com')
# exit() if not response.status_code == requests.codes.ok else print('Requests Successfully')

#  Requests Successfully 

# # 信息性状态码
# 100: ('continue',),
# 101: ('switching_protocols',),
# 102: ('processing',),
# 103: ('checkpoint',),
# 122: ('uri_too_long', 'request_uri_too_long'),
 
# # 成功状态码
# 200: ('ok', 'okay', 'all_ok', 'all_okay', 'all_good', '\\o/', '✓'),
# 201: ('created',),
# 202: ('accepted',),
# 203: ('non_authoritative_info', 'non_authoritative_information'),
# 204: ('no_content',),
# 205: ('reset_content', 'reset'),
# 206: ('partial_content', 'partial'),
# 207: ('multi_status', 'multiple_status', 'multi_stati', 'multiple_stati'),
# 208: ('already_reported',),
# 226: ('im_used',),
 
# # 重定向状态码
# 300: ('multiple_choices',),
# 301: ('moved_permanently', 'moved', '\\o-'),
# 302: ('found',),
# 303: ('see_other', 'other'),
# 304: ('not_modified',),
# 305: ('use_proxy',),
# 306: ('switch_proxy',),
# 307: ('temporary_redirect', 'temporary_moved', 'temporary'),
# 308: ('permanent_redirect',
#       'resume_incomplete', 'resume',), # These 2 to be removed in 3.0
 
# # 客户端错误状态码
# 400: ('bad_request', 'bad'),
# 401: ('unauthorized',),
# 402: ('payment_required', 'payment'),
# 403: ('forbidden',),
# 404: ('not_found', '-o-'),
# 405: ('method_not_allowed', 'not_allowed'),
# 406: ('not_acceptable',),
# 407: ('proxy_authentication_required', 'proxy_auth', 'proxy_authentication'),
# 408: ('request_timeout', 'timeout'),
# 409: ('conflict',),
# 410: ('gone',),
# 411: ('length_required',),
# 412: ('precondition_failed', 'precondition'),
# 413: ('request_entity_too_large',),
# 414: ('request_uri_too_large',),
# 415: ('unsupported_media_type', 'unsupported_media', 'media_type'),
# 416: ('requested_range_not_satisfiable', 'requested_range', 'range_not_satisfiable'),
# 417: ('expectation_failed',),
# 418: ('im_a_teapot', 'teapot', 'i_am_a_teapot'),
# 421: ('misdirected_request',),
# 422: ('unprocessable_entity', 'unprocessable'),
# 423: ('locked',),
# 424: ('failed_dependency', 'dependency'),
# 425: ('unordered_collection', 'unordered'),
# 426: ('upgrade_required', 'upgrade'),
# 428: ('precondition_required', 'precondition'),
# 429: ('too_many_requests', 'too_many'),
# 431: ('header_fields_too_large', 'fields_too_large'),
# 444: ('no_response', 'none'),
# 449: ('retry_with', 'retry'),
# 450: ('blocked_by_windows_parental_controls', 'parental_controls'),
# 451: ('unavailable_for_legal_reasons', 'legal_reasons'),
# 499: ('client_closed_request',),
 
# # 服务端错误状态码
# 500: ('internal_server_error', 'server_error', '/o\\', '✗'),
# 501: ('not_implemented',),
# 502: ('bad_gateway',),
# 503: ('service_unavailable', 'unavailable'),
# 504: ('gateway_timeout',),
# 505: ('http_version_not_supported', 'http_version'),
# 506: ('variant_also_negotiates',),
# 507: ('insufficient_storage',),
# 509: ('bandwidth_limit_exceeded', 'bandwidth'),
# 510: ('not_extended',),
# 511: ('network_authentication_required', 'network_auth', 'network_authentication')

###  文件上传   
import requests
files = {
	'file':open('favicon.ico', 'rb')
}
response = requests.post('http://httpbin.org/post', files = files)
print(response.text)

# {
#   "args": {}, 
#   "data": "", 
#   "files": {
#     "file": "data:application/octet-stream;base64,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AAAAAAAAKysrBhYWGUcWFhiVFRUYvxUVGNkWFhfzFhYX8xUVGNkVFRi/FhYYlRYWGUcrKysGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="
#   }, 
#   "form": {}, 
#   "headers": {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Connection": "close", 
#     "Content-Length": "6665", 
#     "Content-Type": "multipart/form-data; boundary=8bc536e7de1b4bd485b1dfd56697a668", 
#     "Host": "httpbin.org", 
#     "User-Agent": "python-requests/2.18.4"
#   }, 
#   "json": null, 
#   "origin": "121.34.53.82", 
#   "url": "http://httpbin.org/post"
# }



##  cookies  处理 
import requests 
response = requests.get('https://www.baidu.com')
print(response.cookies)
for key, value in response.cookies.items():
	print(key + ' = ' + value)

# <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
# BDORZ = 27315


###   利用 Cookies 登录 知乎

import requests
headers = {
	'Cookies':'AFAA7JKAwQmPThoxN5nN2BhBHWynl49NW4Q=|1460384539"; _ga=GA1.2.1363499149.1448896119; q_c1=962ff655c163401d87cf449f327500bf|1508034178000|1448896073000; _zap=da857144-ab77-43b3-a83c-4119d443a6f9; z_c0="2|1:0|10:1521036654|4:z_c0|92:Mi4xVF9xM0FBQUFBQUFBVUFEc2tvREJDU1lBQUFCZ0FsVk5ibnVXV3dCMFgtUU14cERERE1rLThIVUtYUmluLVhBTTln|250a65a2539b1db1d6473e152aeef93594f64e637ade6b69fe8bfbadbc26d045"; __DAYU_PP=yayiifbQnbjy2nRA2JfZ211caaa4632a; __utmz=51854390.1521474560.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.100-1|2=registration_date=20141228=1^3=entry_date=20141228=1; q_c1=962ff655c163401d87cf449f327500bf|1524327443000|1448896073000; _xsrf=c7cdfeaa085c68b5b5a985840f642c54; aliyungf_tc=AQAAABYfrFu05g0AUjUieUy2UacwJ9Wj; __utmc=51854390; __utma=51854390.1363499149.1448896119.1524364788.1524366741.5',
	'Host':'www.zhihu.com',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
	'Upgrade-Insecure-Requests':'1',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive'	
}

response = requests.get('http://www.zhihu.com', headers=headers)
# print(response.text)     #   直接输出有乱码，需要编码处理（还未找到方法）



import requests 
Cookies = 'AFAA7JKAwQmPThoxN5nN2BhBHWynl49NW4Q=|1460384539"; _ga=GA1.2.1363499149.1448896119; q_c1=962ff655c163401d87cf449f327500bf|1508034178000|1448896073000; _zap=da857144-ab77-43b3-a83c-4119d443a6f9; z_c0="2|1:0|10:1521036654|4:z_c0|92:Mi4xVF9xM0FBQUFBQUFBVUFEc2tvREJDU1lBQUFCZ0FsVk5ibnVXV3dCMFgtUU14cERERE1rLThIVUtYUmluLVhBTTln|250a65a2539b1db1d6473e152aeef93594f64e637ade6b69fe8bfbadbc26d045"; __DAYU_PP=yayiifbQnbjy2nRA2JfZ211caaa4632a; __utmz=51854390.1521474560.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.100-1|2=registration_date=20141228=1^3=entry_date=20141228=1; q_c1=962ff655c163401d87cf449f327500bf|1524327443000|1448896073000; _xsrf=c7cdfeaa085c68b5b5a985840f642c54; aliyungf_tc=AQAAABYfrFu05g0AUjUieUy2UacwJ9Wj; __utmc=51854390; __utma=51854390.1363499149.1448896119.1524364788.1524366741.5'
jar = requests.cookies.RequestsCookieJar()
headers = {
	'Host':'www.zhihu.com',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
	'Upgrade-Insecure-Requests':'1',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive'	
}

for cookie in Cookies.split(';'):
	key, value = cookie.split('=',1)
	jar.set(key, value)
response = requests.get('http://www.zhihu.com', cookies=jar, headers=headers)
# print(response.text)




import requests 
requests.get('http://httpbin.org/cookies/set/number/123456789')
response = requests.get('http://httpbin.org/cookies')
print(response.text)


# {
#   "cookies": {
#     "number": "123456789"
#   }
# }


import requests 
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
response = s.get('http://httpbin.org/cookies')
print(response.text)

# {
#   "cookies": {
#     "number": "123456789"
#   }
# }



from requests import Request, Session 
url = 'http://httpbin.org/post'
data = {
	'name':'germey'
}
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
}

session = Session()
req = Request('POST', url, data=data, headers =headers)
prepped = session.prepare_request(req)
response = session.send(prepped)
print(response.text)


# {
#   "args": {}, 
#   "data": "", 
#   "files": {}, 
#   "form": {
#     "name": "germey"
#   }, 
#   "headers": {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Connection": "close", 
#     "Content-Length": "11", 
#     "Content-Type": "application/x-www-form-urlencoded", 
#     "Host": "httpbin.org", 
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"
#   }, 
#   "json": null, 
#   "origin": "113.91.188.47", 
#   "url": "http://httpbin.org/post"
# }
