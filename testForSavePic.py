# -*- conding:utf-8 -*-

### 测试下载并保持图片

import os
import requests
from hashlib import md5

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
def save_image(item):
	print(item.get('title'))
	if not os.path.exists(item.get('title')):
		os.mkdir(item.get('title'))
	try:
		print('image' ,item.get('image'))
		if None == item.get('image'):
			return
		pic_url = 'http:' + item.get('image').replace('list', 'origin')
		response = requests.get(pic_url, headers=headers)
		if response.status_code == 200:
			file_path = '{0}/{1}{2}'.format(item.get('title'), md5(response.content).hexdigest(), '.jpg')
			if not os.path.exists(file_path):
				with open(file_path, 'wb') as f:
					f.write(response.content)
				print('Success save Image!')
			else:
				print('Already Download:', file_path)
	except requests.ConnectionError as e:
		print('Failed to save image.', e.args)

item = {'image': '//p1.pstatp.com/list/1bf5001368e91956ca5c', 'title': '街拍：看外国小姐姐街拍，性感吸引人'}

if __name__ == '__main__':
	save_image(item)

