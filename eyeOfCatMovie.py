# -*- coding:utf-8 -*- 

####  爬取猫眼电影 TOP100 
####  需要加上请求的头，headers  不然会被拦截

import requests 
import re
import json
import time 
from requests.exceptions import RequestException

###  请求打开每一页， 并返回页面源码
def get_one_page(url, headers):
	try:
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException as e:
		return None 
	
#####   正则表达式处理 每一页的信息， 提取需要的信息出来
def parse_one_page(html):
	pattern = re.compile('<dd.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?title="(.*?)".*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
	items = re.findall(pattern, html)
	for item in items:
		yield{
			'index':item[0],
			'image':item[1],
			'title':item[2].strip(),
			'actor':item[3].strip()[3:] ,
			'time':item[4].strip()[5:] ,
			'score':item[5].strip() + item[6].strip()
		}
	# print(items)	

####  将提取到的信息  写入文件
def write_to_json(content):
	with open('MovieResult.txt', 'a', encoding='utf-8') as f:
		# print(type(json.dumps(content)))
		f.write(json.dumps(content, ensure_ascii=False)+"\n")


def main(offset):
	url = 'http://maoyan.com/board/4?offset=' + str(offset)
	headers = {
		'Cookies':'uuid=1A6E888B4A4B29B16FBA1299108DBE9CB97C6757ABDCAA16811B266DFBAFFC7F; _csrf=311a27007890d9cdab74e1a956f516802f92fc1dd96315e12494d1815315b3c5; _lxsdk_cuid=1630797eb4dc8-0ddb919f9e5c34-3a614108-100200-1630797eb4dc8; _lxsdk=1A6E888B4A4B29B16FBA1299108DBE9CB97C6757ABDCAA16811B266DFBAFFC7F; __mta=110359994.1524840786871.1524840878550.1524841300835.4; _lxsdk_s=1630797eb4f-106-6e9-4fe%7C%7C8',
		'Host':'maoyan.com',
		'Referer': 'http://maoyan.com/board/4?offset=10',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
		'Upgrade-Insecure-Requests':'1',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh-CN,zh;q=0.9',
		'Cache-Control': 'max-age=0',
		'Connection': 'keep-alive'	
	}
	html = get_one_page(url, headers)
	for item in parse_one_page(html):
		print(item)
		write_to_json(item)



if __name__ == '__main__':
	for i in range(10):
		main(offset= i * 10)
		time.sleep(1)



