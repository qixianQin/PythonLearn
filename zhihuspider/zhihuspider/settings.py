# -*- coding: utf-8 -*-

# Scrapy settings for zhihuspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import os
BOT_NAME = 'zhihuspider'

SPIDER_MODULES = ['zhihuspider.spiders']
NEWSPIDER_MODULE = 'zhihuspider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cache-control': 'max-age=0',
# 'cookie': 'd_c0="AFAA7JKAwQmPThoxN5nN2BhBHWynl49NW4Q=|1460384539"; q_c1=962ff655c163401d87cf449f327500bf|1508034178000|1448896073000; _zap=da857144-ab77-43b3-a83c-4119d443a6f9; z_c0="2|1:0|10:1521036654|4:z_c0|92:Mi4xVF9xM0FBQUFBQUFBVUFEc2tvREJDU1lBQUFCZ0FsVk5ibnVXV3dCMFgtUU14cERERE1rLThIVUtYUmluLVhBTTln|250a65a2539b1db1d6473e152aeef93594f64e637ade6b69fe8bfbadbc26d045"; __DAYU_PP=yayiifbQnbjy2nRA2JfZ211caaa4632a; __utmz=51854390.1521474560.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.100-1|2=registration_date=20141228=1^3=entry_date=20141228=1; __utma=51854390.1363499149.1448896119.1524364788.1524366741.5; tgw_l7_route=23ddf1acd85bb5988efef95d7382daa0; _xsrf=b32dbe43-67ec-4cf4-ae76-2544e28c6309; q_c1=962ff655c163401d87cf449f327500bf|1528211960000|1448896073000',
# 'upgrade-insecure-requests': '1',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihuspider.middlewares.ZhihuspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhihuspider.middlewares.ZhihuspiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'zhihuspider.pipelines.ZhihuspiderPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 广度优先
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'

# 项目路径
PROJECT_DIR = os.path.dirname(os.path.abspath(os.path.curdir))

# mongodb配置
MONGO_URI = 'mongodb://localhost:27017'

# pipeline设置
ITEM_PIPELINES = {
    'zhihuspider.pipelines.ZhihuPipeline': 500,
}

# 异步任务队列
BROKER_URL = 'amqp://guest:guest@localhost:5672//'