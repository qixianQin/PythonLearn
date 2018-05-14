# -*- coding:utf-8 -*-

###Selenium的使用   

# from selenium import webdriver 
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait


# headers = {
# 	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# 'Accept-Encoding': 'gzip, deflate, br',
# 'Accept-Language': 'zh-CN,zh;q=0.9',
# 'Cache-Control': 'max-age=0',
# 'Connection': 'keep-alive',
# 'Cookie': 'BAIDUID=617968D562428DF6155A5CCF02062292:FG=1; PSTM=1496675585; BIDUPSID=4A741335522EF4E208E37D09FA2A40C5; BDUSS=DVzeGdIUXZLVllQM1NKUmRhUGx0dHFFMnlWZTJzMUdVSklZeUxHZkg5RkN4NXRaSVFBQUFBJCQAAAAAAAAAAAEAAADQTuVyvsnDzsjnus7S5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEI6dFlCOnRZS; BD_UPN=12314753; MCITY=-%3A; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[mkUqnUt8juD]=mk3SLVN4HKm; BD_HOME=1; H_PS_PSSID=13701_1422_21083_20928',
# 'Host': 'www.baidu.com',
# 'Upgrade-Insecure-Requests': '1',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
# }

# browser = webdriver.Chrome()
# try:
# 	browser.get('https://www.baidu.com')
# 	input = browser.find_element_by_id('kw')
# 	input.send_keys('Python')
# 	input.send_keys(Keys.ENTER)
# 	wait = WebDriverWait(browser, 10)
# 	wait.until(EC.presence_of_element_located(By.ID, 'content_left'))
# 	print(browser.current_url)
# 	print(browser.get_cookies())
# 	print(browser.page_source())
# except Exception as e:
# 	print(e)
# finally:
# 	browser.close()



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
 
# browser = webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()


###   声明浏览器对象 
# from selenium import webdriver 

# browser = webdriver.Chrome()   ##  Chrome 浏览器
# browser = webdriver.Firefox()  ##  火狐浏览器
# browser = webdriver.Edge()     ##  微软浏览器
# browser = webdriver.PhantomJS()   ##  
# browser = webdriver.Safari()   ## 苹果



from selenium import webdriver 

browser = webdriver.Firefox()
browser.get('https://www.taobao.com')
print(browser.page_source)
