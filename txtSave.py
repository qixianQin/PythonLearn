# -*- coding:utf-8 -*- 

###    TXT文本存储

import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/'
headers = {
	'Cache-Control': 'private,no-store,max-age=0,no-cache,must-revalidate,post-check=0,pre-check=0',
	'Connection': 'keep-alive',
	'Content-Encoding': 'br',
'Content-Security-Policy': 'default-src * blob:;img-src * data: blob:;frame-src 'self' *.zhihu.com getpocket.com note.youdao.com safari-extension://com.evernote.safari.clipper-Q79WDW8YH9 weixin: zhihujs: v.qq.com v.youku.com www.bilibili.com *.vzuu.com captcha.guard.qcloud.com;script-src 'self' *.zhihu.com *.google-analytics.com zhstatic.zhihu.com res.wx.qq.com 'unsafe-eval' unpkg.zhimg.com unicom.zhimg.com captcha.gtimg.com captcha.guard.qcloud.com blob:;style-src 'self' *.zhihu.com unicom.zhimg.com 'unsafe-inline' captcha.gtimg.com;connect-src * wss:',
'Content-Type': 'text/html; charset=utf-8',
'Date': 'Mon, 30 Apr 2018 15:52:27 GMT',
'Expires': 'Fri, 02 Jan 2000 00:00:00 GMT',
'Pragma': 'no-cache',
'Server': 'ZWS',
'Transfer-Encoding': 'chunked',
'Vary': 'Accept-Encoding',
'X-Backend-Server': 'heifetz.heifetz.6b422007---10.2.74.2:31020[10.2.74.2:31020]',
'X-Frame-Options': 'DENY',
'X-Req-ID': '254A6A1F5AE73BBB',
'X-Req-SSL': 'proto=TLSv1.2,sni=api.zhihu.com,cipher=ECDHE-RSA-AES256-GCM-SHA384'
}

html = requests.get(url, headers=headers)
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
for item in items:
	