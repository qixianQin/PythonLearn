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

	def after_login(self, response):
		"""
		登录完成后，从第一个用户数据爬取数据
		"""
		return [Request(self.start_url, meta={'cookiejar':response.meta['cookiejar']}, callback=self.parse_people, errback=parse_err)]

	def parse_people(self, response):
		"""
		解析用户主页
		"""
		selector = Selector(response)
		nickname = selector.xpath('div[@class="title-section ellipsis"]/span[@class="name"]/text()').extract_first()
		zhihu_id = os.path.split(response.url)[-1]
		location = selector.xpath('//span[@class="location item"]/@title').extract_first()
		business = selector.xpath('//span[@class="business item"]/@title').extract_first()
		gender = selector.xpath('//span[@class="item gender"]/i/@class').extract_first()
		if gender is not None:
			gender = Gender.FEMALE if u'female' in gender else Gender.MALE
		employment = selector.xpath('//span[@class="employment item"]/@title').extract_first()
		position = selector.xpath('//span[@class="position item"]/@title').extract_first()
		education = selector.xpath('//span[@class="education-extra item"]/@title').extract_first()
		followee_count, follower_count = tuple(selector.xpath('//div[@class="zm-profile-side-following zg-cleaar"]/a[@class="item"]/strong/text()')).extract()
		followee_count, follower_count = int(followee_count), int(follower_count)
		image_url - selector.xpath('//div[@class="body clearfix"]/img/@srcset').extract_first('')[0:-3]

		follow_urls = selector.xpath('//div[@class="zm-profile-side-following zg-clear"]/a[@class="item"]/@href').extract()
		for url in follow_urls:
			complete_url = 'https://{}{}'.format(self.allowed_domains[0], url)
			yield Request(complete_url, meta={'cookiejar':response.meta['cookiejar']}, callback=self.parse_follow, errback=self.parse_err)

		item = ZhihuPeopleItem(
			nickname = nickname,
			zhihu_id = zhihu_id,
			location = location,
			business = business,
			gender = gender,
			employment = employment,
			position = position,
			education = education,
			followee_count = followee_count,
			follower_count = follower_count,
			image_url = image_url,
			)
		yield item