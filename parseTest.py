# -*- coding:utf-8 -*- 

from urllib.parse import urlparse

result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')
print(type(result), '\n', result)

# <class 'urllib.parse.ParseResult'> 
#  ParseResult(scheme='https', netloc='www.baidu.com', path='/index.html', 
#              params='user', query='id=5', fragment='comment')


from urllib.parse import urlparse 

result = urlparse('www.baidu.com/index.html; user?id=5#comment', scheme='http')
print(result)

#ParseResult(scheme='http', netloc='', path='www.baidu.com/index.html', 
#    params=' user', query='id=5', fragment='comment')

#  如果 url 中没有协议类型， 则取 scheme中的默认值，  如果scheme也没有值， 返回的协议类型为空的
#   如果 url 中有协议类型， scheme中也有值，  则取url 中的值 ；   即url 中不存在协议的时候，scheme才会生效


from urllib.parse import urlparse 
result = urlparse('https://www.baidu.com/index.html; user?id=5#comment', allow_fragments=False)
print(result)

#ParseResult(scheme='https', netloc='www.baidu.com', path='/index.html', 
#  params=' user', query='id=5#comment', fragment='')
#   allow_fragments=False  ==>   fragment=''    fragment 变成了 query的一部分

from urllib.parse import urlparse 
result = urlparse('https://www.baidu.com/index.html#comment', allow_fragments=False)
print(result)

# ParseResult(scheme='https', netloc='www.baidu.com', path='/index.html#comment',
#  params='', query='', fragment='')

# URL中params 和query 也没有了       allow_fragments=False   ==>  只剩下 path


from urllib.parse import urlparse

result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')
print(result)
print(result.scheme, result[0], result.netloc, result[1], sep='\n')

# ParseResult(scheme='https', netloc='www.baidu.com', path='/index.html', 
#              params='user', query='id=5', fragment='comment')
# https
# https
# www.baidu.com
# www.baidu.com

#  ParseResult实际上是一个元组，我们可以用索引顺序来获取，也可以用属性名获取


from urllib.parse import urlunparse
data = ['https', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))

#https://www.baidu.com/index.html;user?a=6#comment


from urllib.parse import urlsplit
result = urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
print(result)
print(result.scheme, result[0])

# SplitResult(scheme='https', netloc='www.baidu.com', path='/index.html;user', 
# 	query='id=5', fragment='comment')
#   https https

#  SplitResult 也是一个元组类型，既可以用属性获取值，也可以用索引来获取

from urllib.parse import urlunsplit
data = ['https', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data))

#https://www.baidu.com/index.html?a=6#comment


from urllib.parse import urljoin
print(urljoin('https://www.baidu.com', 'FAQ.html'))
print(urljoin('https://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
print(urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
print(urljoin('http://www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com#comment', '?category=2'))

# https://www.baidu.com/index.html?a=6#comment
# https://www.baidu.com/FAQ.html
# https://cuiqingcai.com/FAQ.html
# https://cuiqingcai.com/FAQ.html
# https://cuiqingcai.com/FAQ.html?question=2
# https://cuiqingcai.com/index.php
# http://www.baidu.com?category=2#comment
# www.baidu.com?category=2#comment
# www.baidu.com?category=2


from urllib.parse import urlencode 
params={
	'name':'germey',
	'age': 22
}
base_url = 'https://www.baidu.com?'
url = base_url + urlencode(params)
print(url)

#  https://www.baidu.com?name=germey&age=22


from urllib.parse import parse_qs
query='name=germey&age=22'
print(parse_qs(query))

#  {'name': ['germey'], 'age': ['22']}

from urllib.parse import parse_qsl
query='name=germey&age=22'
print(parse_qsl(query))

# [('name', 'germey'), ('age', '22')]


from urllib.parse import quote
keyword = '中国'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)

#https://www.baidu.com/s?wd=%E4%B8%AD%E5%9B%BD   
###   URL 编码 

from urllib.parse import unquote 
url='https://www.baidu.com/s?wd=%E4%B8%AD%E5%9B%BD'
print(unquote(url))

#  https://www.baidu.com/s?wd=中国        URL 解码
