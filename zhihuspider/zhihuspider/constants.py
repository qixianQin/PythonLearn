# -*- coding:utf-8 -*- 

"""
常量定义
"""

from zhihuspider.settings import USER_AGENT

class Gender(object):
	"""docstring for Gender"""
	
	"""
	性别定义
	"""
	MALE = 1
	FEMALE = 2

class People(object):
    """
    人员类型
    """		
    Followee = 1
    Follower = 2


HEADER = {

'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cache-control': 'max-age=0',
'cookie': 'd_c0="AFAA7JKAwQmPThoxN5nN2BhBHWynl49NW4Q=|1460384539"; q_c1=962ff655c163401d87cf449f327500bf|1508034178000|1448896073000; _zap=da857144-ab77-43b3-a83c-4119d443a6f9; z_c0="2|1:0|10:1521036654|4:z_c0|92:Mi4xVF9xM0FBQUFBQUFBVUFEc2tvREJDU1lBQUFCZ0FsVk5ibnVXV3dCMFgtUU14cERERE1rLThIVUtYUmluLVhBTTln|250a65a2539b1db1d6473e152aeef93594f64e637ade6b69fe8bfbadbc26d045"; __DAYU_PP=yayiifbQnbjy2nRA2JfZ211caaa4632a; __utmz=51854390.1521474560.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.100-1|2=registration_date=20141228=1^3=entry_date=20141228=1; __utma=51854390.1363499149.1448896119.1524364788.1524366741.5; tgw_l7_route=23ddf1acd85bb5988efef95d7382daa0; _xsrf=b32dbe43-67ec-4cf4-ae76-2544e28c6309; q_c1=962ff655c163401d87cf449f327500bf|1528211960000|1448896073000',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'	
}		