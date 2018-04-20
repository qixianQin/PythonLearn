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