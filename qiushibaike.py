# -*- coding:utf-8 -*- 

###   爬取糗事百科 热门段子

import requests 
from bs4 import BeautifulSoup

base_url = 'https://www.qiushibaike.com/8hr/page/'
def get_page(index):
	url = base_url + str(index) 
	response = requests.get(base_url)
	if response.status_code == 200:
		soup = BeautifulSoup(response.text, 'lxml')
		# print("soup:", type(soup))
		# print("content-left: ",type(soup.find_all(class_='content')))
		# print(soup.find_all(attrs={"id":"content-left"}).find(class_='content'))
		# for div_child in soup.find_all(attrs={"id":"content-left"}):

		# return soup.find_all(attrs={"id":"content-left"})
		result = []
		for div_child in soup.find_all(class_='article block untagged mb15 typs_hot'):
			result.extend(div_child.find_all(name='span'))
		# print('result len:', len(result))
		# print('result:', result)
		result_span = []
		for span in result:
			# print('Span:', span)
			# print('get:', type(span.string))
			# print(type(span))
			span_str = str(span)
			# print('span_str:', span_str)
			# print('startswith:', span_str.startswith('<span>'))
			if span_str.startswith('<span>'):
			# if span.find(' <span>'):
				# print('add result_span to []:')
				print(span_str, '\n')
				result_span.append(span_str)
		# print('span_len:', len(result_span))
		# print('span:', result_span)


		# return soup.find_all(class_='article block untagged mb15 typs_hot')
	else:
		return None


def get_host_detail(text):
	pass

if __name__ == '__main__':
	response_html = get_page(2)
	print(type(response_html))
	if response_html != None:
		# print(response_html.find(class_='content'))
		print(response_html)
		# for div_child in response_html.find_all(attrs={"class":"content"}):
		# 	print(div_child)
	else:
		print('can\'t catch any thing')

