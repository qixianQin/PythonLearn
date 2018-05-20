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
		return soup.find_all(attrs={"id":"content-left"})
	else:
		return None


def get_host_detail(text):
	pass

if __name__ == '__main__':
	response_html = get_page(1)
	if response_html != None:
		print(response_html)
	else:
		print('can\'t catch any thing')

