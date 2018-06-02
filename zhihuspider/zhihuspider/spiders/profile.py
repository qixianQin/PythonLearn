#  -*- conding：utf-8 -*- 

import os 
import re 
import json 

from urllib import urlencode 
from scrapy import log 
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request, FromReqeust

from zhihu.items import ZhihuPeopleItem, ZhihuRelationItem
from zhihu.constants import Gender, People, HEADER

class ZhihuSpider(CrawlSpider):
	"""docstring for ZhihuSpider"""

	name = "zhihu"

	base_url = ["www.zhihu.com"]
	start_url = "https://www.zhihu.com/people/weizhi-xiazhi"

	def __init__(self, *arg, **kwargs):
		super(ZhihuSpider, self).__init__(*arg, **kwargs)
		self.xsrf = ''
		# self.arg = arg

	def start_requests(self):
		"""
		登录页面， 获取xrsf
		"""
		return [Request("https://www.zhihu.com/#signin", meta={"cookiejar":1}, callback=self.post_login)]

	def post_login(self, response):
		"""
		解析登录页面， 发送登录表单
		"""
		self.xsrf = Selector(response).xpath('//input[@name="_xsrf"]/@value').extract()[0]

		return [FromReqeust('https://www.zhihu.com/login/email', method='POST', meta={'cookiejar':response.meta['cookiejar']}, formdata={'_xsrf':self.xsrf,'email':'XXXXX','password':'xxxx','remember_me':'true'}, callback=self.after_login)]

	