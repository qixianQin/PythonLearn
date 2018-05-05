# -*- coding:utf-8 -*-
import requests 
import re

headers = {
	'User-Agnet':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.9',
	'Cache-Control':'max-age=0',
	'Connection':'keep-alive',
	'Cookie':'d_c0="AFAA7JKAwQmPThoxN5nN2BhBHWynl49NW4Q=|1460384539"; _ga=GA1.2.1363499149.1448896119; q_c1=962ff655c163401d87cf449f327500bf|1508034178000|1448896073000; _zap=da857144-ab77-43b3-a83c-4119d443a6f9; z_c0="2|1:0|10:1521036654|4:z_c0|92:Mi4xVF9xM0FBQUFBQUFBVUFEc2tvREJDU1lBQUFCZ0FsVk5ibnVXV3dCMFgtUU14cERERE1rLThIVUtYUmluLVhBTTln|250a65a2539b1db1d6473e152aeef93594f64e637ade6b69fe8bfbadbc26d045"; __DAYU_PP=yayiifbQnbjy2nRA2JfZ211caaa4632a; __utmz=51854390.1521474560.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.100-1|2=registration_date=20141228=1^3=entry_date=20141228=1; q_c1=962ff655c163401d87cf449f327500bf|1524327443000|1448896073000; _xsrf=c7cdfeaa085c68b5b5a985840f642c54; aliyungf_tc=AQAAABYfrFu05g0AUjUieUy2UacwJ9Wj; __utmc=51854390; __utma=51854390.1363499149.1448896119.1524362369.1524364788.4',
	'Host':'www.zhihu.com',
	'Upgrade-Insecure-Requests':'1'
}

response = requests.get('https://www.zhihu.com', headers=headers)
print(response.text)   #  输出为空
pattern = re.compile('<h2><a.*?>(.*?)</a></h2>', re.S)
titles = re.findall(pattern, response.text)
print(titles)