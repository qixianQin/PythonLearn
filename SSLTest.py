# -*- coding:utf-8 -*-
# import requests 
# response = requests.get('https://www.12306.cn')
# print(response.status_code)

# 证书验证错误
# requests.exceptions.SSLError: HTTPSConnectionPool(host='www.12306.cn', port=443):
#  Max retries exceeded with url: / (Caused by SSLError(SSLError("bad handshake: 
# Error([('SSL routines', 'tls_process_server_certificate', 'certificate verify failed')],)",),))

import requests 
response = requests.get('https://www.12306.cn', verify= False)
print(response.status_code)

# D:\softInstall\Python\lib\site-packages\urllib3\connectionpool.py:858: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
#   InsecureRequestWarning)    警告
# 200


import requests 
from requests.packages import urllib3 

urllib3.disable_warnings()
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)

#   去掉警告
# 200   

#  通过捕获警告到日志的方式的警告
import logging 
import requests 
logging.captureWarnings(True) 
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)

# 200




###  代理 
import requests 
proxies = {
	'http':'http://10.10.1.10:3128',
	'https':'https://10.12.12.12:1090'
}

requests.get('https://www.baidu.com', proxies=proxies)


### 代理
import requests 
proxies = {
	'http':'http://user:password@10.10.1.10:3128'
}
reqeusts.get('https://www.taobao.com', proxies=proxies)