# -*- coding:utf-8 -*- 

###    TXT文本存储

import requests
# from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/'
headers = {
	'Cache-Control': 'private,no-store,max-age=0,no-cache,must-revalidate,post-check=0,pre-check=0',
	'Connection': 'keep-alive',
	'Content-Encoding': 'br',
'Content-Security-Policy': 'default-src * blob:;img-src * data: blob:;frame-src \'self\' *.zhihu.com getpocket.com note.youdao.com safari-extension://com.evernote.safari.clipper-Q79WDW8YH9 weixin: zhihujs: v.qq.com v.youku.com www.bilibili.com *.vzuu.com captcha.guard.qcloud.com;script-src \'self\' *.zhihu.com *.google-analytics.com zhstatic.zhihu.com res.wx.qq.com \'unsafe-eval\' unpkg.zhimg.com unicom.zhimg.com captcha.gtimg.com captcha.guard.qcloud.com blob:;style-src \'self\' *.zhihu.com unicom.zhimg.com \'unsafe-inline\' captcha.gtimg.com;connect-src * wss:',
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

html = requests.get(url, headers=headers).text()
print(html)
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
for item in items:
	question = item.find('h2').text()
	autour = item.find('.autour-link-line').text()
	answer = pq(item.find('.content').html()).text()
	file = open('explore.txt', 'a', encoding='utf-8')
	file = write('\n'.join([question, autour, answer]))
	file = write('\n' + '=' * 50 + '\n')
	file.close()



#  open()方法的第二个参数设置成了a，这样在每次写入文本时不会清空源文件，
# 而是在文件末尾写入新的内容，这是一种文件打开方式。关于文件的打开方式，
# 其实还有其他几种


# r：以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# rb：以二进制只读方式打开一个文件。文件指针将会放在文件的开头。
# r+：以读写方式打开一个文件。文件指针将会放在文件的开头。
# rb+：以二进制读写方式打开一个文件。文件指针将会放在文件的开头。
# w：以写入方式打开一个文件。如果该文件已存在，则将其覆盖。如果该文件不存在，则创建新文件。
# wb：以二进制写入方式打开一个文件。如果该文件已存在，则将其覆盖。如果该文件不存在，则创建新文件。
# w+：以读写方式打开一个文件。如果该文件已存在，则将其覆盖。如果该文件不存在，则创建新文件。
# wb+：以二进制读写格式打开一个文件。如果该文件已存在，则将其覆盖。如果该文件不存在，则创建新文件。
# a：以追加方式打开一个文件。如果该文件已存在，文件指针将会放在文件结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，则创建新文件来写入。
# ab：以二进制追加方式打开一个文件。如果该文件已存在，则文件指针将会放在文件结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，则创建新文件来写入。
# a+：以读写方式打开一个文件。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，则创建新文件来读写。
# ab+：以二进制追加方式打开一个文件。如果该文件已存在，则文件指针将会放在文件结尾。如果该文件不存在，则创建新文件用于读写。



html = requests.get(url, headers=headers).text()
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
for item in items:
	question = item.find('h2').text()
	autour = item.find('.autour-link-line').text()
	answer = pq(item.find('.content').html()).text()
	with open('explore.txt', 'a', encoding='utf-8') as file:
		file.write('\n'.join([question, autour, answer]))
		file.write('\n' + '=' * 50 + '\n')
		