# -*- coding:utf-8 -*-

# test for urlopen method
from urllib import request
response = request.urlopen('https://www.python.org')
#  输出整个页面的源码
print(response.read().decode('utf-8'))
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