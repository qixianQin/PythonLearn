# -*- conding:utf-8 -*-

##  爬取今日头条街拍美女图片
# https://www.toutiao.com/search_content/?
# offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D
# &autoload=true&count=20&cur_tab=1&from=search_tab

import requests 
import os
from hashlib import md5
from urllib.parse import urlencode
from multiprocessing.pool import Pool

base_url = 'https://www.toutiao.com/search_content/?'

def get_page(offset):

	headers = {
	'accept': 'application/json, text/javascript',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'zh-CN,zh;q=0.9',
	'content-type': 'application/x-www-form-urlencoded',
	'cookie': 'uuid="w:ea7b0e867fbd49669709c597e4ed6883"; _ga=GA1.2.623855010.1468030233; tt_webid=6553215287167682062; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=1634021abe3eb-01aa68cbf0fcfd-3a614108-100200-1634021abe448a; CNZZDATA1259612802=1654205141-1525785189-%7C1525785189; tt_webid=6553215287167682062; __tasessionId=kh14wxpd71525789338829',
	# 'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
	'x-requested-with': 'XMLHttpRequest'
	}

	params = {
		'offset':offset,
		'format':'json',
		'keyword':'街拍',
		'autoload':'true',
		'count':'20',
		'cur_tab':'3',
		'from':'search_tab'
	}

	url = base_url + urlencode(params)
	try:
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			return response.json()
	except requests.ConnectionError as e:
		print('Error:', e.args)

def get_image(json):
	if json.get('data'):
		for item in json.get('data'):
			title = item.get('title')
			images = item.get('image_list')
			for image in images:
				yield{
					'image':image.get('url'),
					'title':title
				}

def save_image(item):
	if not os.path.exists(item.get('title')):
		os.mkdir(item.get('title'))
	try:
		if None == item.get('iamge'):
			return
		response = requests.get(item.get('iamge'))
		if response.status_code == 200:
			file_path = '{0}/{1}{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
			if not os.path.exists(file_path):
				with open(file_path, 'wb') as f:
					f.write(response.content)
			else:
				print('Already Download:', file_path)
	except requests.ConnectionError as e:
		print('Failed to save image.', e.args)


# def main(offset):
# 	json = get_page(offset)
# 	for item in get_image(json):
# 		print(item)
# 		save_image(item)

# GROUP_START = 1
# GROUP_END = 20

if __name__ == '__main__':
	# pool = Pool()
	# groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
	# print('groups:', groups)
	# pool.map(main, groups)
	# pool.close()
	# pool.join()
	for i in range(1, 20):
		offset = i * 20
		json = get_page(offset)
		for item in get_image(json):
			print(item)
			save_image(item)