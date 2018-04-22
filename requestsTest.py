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

response = requests.get('http://www.baidu.com')
exit() if not response.status_code == requests.codes.ok else print('Requests Successfully')

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