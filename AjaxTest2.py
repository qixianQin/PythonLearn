# -*- conding:utf-8 -*-

import requests 

# headers = {
# 	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# 'Accept-Encoding': 'gzip, deflate, br',
# 'Accept-Language': 'zh-CN,zh;q=0.9',
# 'Cache-Control': 'max-age=0',
# 'Connection': 'keep-alive',
# 'Cookie': '_T_WM=3aea36b962d68623ae34e9da7a1ef9b1; MLOGIN=0; WEIBOCN_FROM=1110006030; M_WEIBOCN_PARAMS=fid%3D1076032830678474%26uicode%3D10000011',
# 'Host': 'm.weibo.cn',
# 'Upgrade-Insecure-Requests': '1',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
# }

# base_url = 'https://m.weibo.cn/u/2830678474'

# response = requests.get(base_url, headers=headers)
# print(type(response))
# print(response.text)




from urllib.parse import urlencode
import requests

base_url =  'https://m.weibo.cn/api/container/getIndex?' 
#    type=uid&value=2830678474&containerid=1076032830678474&page=4

headers = {
	'Accept': 'application/json, text/plain, */*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Cookie': '_T_WM=3aea36b962d68623ae34e9da7a1ef9b1; MLOGIN=0; WEIBOCN_FROM=1110006030; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D1076032830678474%26fid%3D1076032830678474%26uicode%3D10000011',
'Host': 'm.weibo.cn',
'Referer': 'https://m.weibo.cn/u/2830678474',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'
}


def get_page(page):
	params = {
		'type':'uid',
		'value':'2830678474',
		'containerid':'1076032830678474',
		'page':page
	}
	url = base_url+urlencode(params)
	try:
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			return response.json()
	except requests.ConnectionError as e:
		print('Error', e.args)

from pyquery import PyQuery as pq 
def parse_page(json):
	if json:
		items = json.get('data').get('cards')
		for item in items:
			item = item.get('mblog')
			weibo = {}
			weibo['id'] = item.get('id')
			weibo['text'] = pq(item.get('text')).text()
			weibo['attitudes'] = item.get('attitudes_count')
			weibo['comments'] = item.get('comments_count')
			weibo['reposts'] = item.get('reposts_count')
			yield weibo


if __name__ == '__main__':
	for page in range(1,11):
		json = get_page(page)
		results = parse_page(json)
		for result in results:
			print(result)



