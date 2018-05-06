#  -*- conding:utf-8 -*- 

from urllib.parse import urlencode
import requests 
# https://m.weibo.cn/api/container/getIndex?type=uid&value=2830678474&containerid=1005052830678474
base_url = 'https://m.weibo.cn/api/container/getIndex?'   

headers = {
	# ':authority': 'm.weibo.cn',
# ':method': 'GET',
# ':path': '/api/container/getIndex?type=uid&value=2830678474&containerid=1005052830678474',
# ':scheme': 'https',
'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cookie': 'T_WM=3aea36b962d68623ae34e9da7a1ef9b1; WEIBOCN_FROM=1110006030; MLOGIN=0; M_WEIBOCN_PARAMS=fid%3D1005052830678474\%26uicode%3D10000011',
'referer': 'https://m.weibo.cn/u/2830678474',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
'x-requested-with': 'XMLHttpRequest'
}

def get_page(page):
	params = {
		'type':'uid',
		'value':'2830678474',
		'containerid':'1005052830678474',
		'page':page
	}
	url = base_url+urlencode(params)
	try:
		response = requests.get(url, headers=headers)
		print(response)
		print(type(response))
		print(response.json)
		if response.status_code == 200:
			return response.json
	except requests.ConnectionError as e:
		print('Error', e.args)

# 定义了base_url来表示请求的URL的前半部分。接下来，构造参数字典，其中type、value和
# containerid是固定参数，page是可变参数。接下来，调用urlencode()方法将参数转化为URL的
# GET请求参数，即类似于type=uid&value=2830678474&containerid=1076032830678474&page=2
# 这样的形式。随后，base_url与参数拼合形成一个新的URL。接着，我们用requests请求这个链接，
# 加入headers参数。然后判断响应的状态码，如果是200，则直接调用json()方法将内容解析为JSON
# 返回，否则不返回任何信息。如果出现异常，则捕获并输出其异常信息


from pyquery import PyQuery as pq 
def parse_page(Response.json):
	if Response.json:
		items = json.get('data').get('cards')
		# items = json.get('data')
		for item in items:
			item = item.get('mblog')
			weibo = {}
			weibo['id'] = item.get('id')
			weibo['text'] = pq(item.get('text')).text()
			weibo['attitudes'] = item.get('attitudes_count')
			weibo['comments'] = item.get('comments_count')
			weibo['reposts'] = item.get('reposts_count')
			yield weibo


# from pymongo import MongoClient
# client = MongoClient()
# db = client['weibo']
# collection = db['weibo']

# def save_to_mongo(result):
# 	if collection.insert(result):
# 		print('Save to MongoDB')

if __name__ == '__main__':
	for page in range(1,11):
		json = get_page(page)
		results = parse_page(json)
		for result in results:
			print(result)