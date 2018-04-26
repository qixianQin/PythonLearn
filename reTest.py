# -*- coding:utf-8 -*- 

# 正则表达式

import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))   #长度
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
print(result.group())
print(result.span())

# 41
# <_sre.SRE_Match object; span=(0, 25), match='Hello 123 4567 World_This'>
# Hello 123 4567 World_This
# (0, 25)

import re 

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWorld', content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())

# <_sre.SRE_Match object; span=(0, 19), match='Hello 1234567 World'>
# Hello 1234567 World
# 1234567
# (0, 19)

import re 
content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello.*Demo$', content)
print(result)
print(result.group())
print(result.span())

# <_sre.SRE_Match object; span=(0, 41), match='Hello 123 4567 World_This is a Regex Demo'>
# Hello 123 4567 World_This is a Regex Demo
# (0, 41)

## 贪婪匹配  
import re
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*(\d+).*Demo$', content)
print(result)
print(result.group(1))

# <_sre.SRE_Match object; span=(0, 40), match='Hello 1234567 World_This is a Regex Demo'>
# 7

##贪婪匹配：   .* (点星)会匹配尽可能多的字符。正则表达式中 .* 后面是 \d+，也就是至少一个数字， 并没有指定具体多少数字。因此， .* 就尽可能匹配多的字符，
##   这里就把 123456匹配了，  给 \d+ 留下一个可满足条件的数字 7 ，最后得到的内容只有数字 7 了

## 非贪婪匹配： 
import re
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*?(\d+).*Demo$', content)
print(result)
print(result.group(1))


# <_sre.SRE_Match object; span=(0, 40), match='Hello 1234567 World_This is a Regex Demo'>
# 1234567

## 非贪婪匹配：  .* 改成  .*?      贪婪匹配是尽可能匹配多的字符， 非贪婪匹配就是尽可能匹配少的字符
##  当.*?匹配到Hello后面的空白字符时，再往后的字符就是数字了，而\d+恰好可以匹配，那么这里.*?就不再进行匹配，
##  交给\d+去匹配后面的数字。所以这样.*?匹配了尽可能少的字符，\d+的结果就是1234567了
## 在做匹配的时候，字符串中间尽量使用非贪婪匹配，也就是用.*?来代替.*

## 匹配的结果在字符串结尾，.*?就有可能匹配不到任何内容了，因为它会匹配尽可能少的字符
import re
content = 'http://www.weibo.com/comment/KEraCN'
result1 = re.match('^http.*?comment/(.*?)', content)
result2 = re.match('^http.*comment/(.*)', content)
print(result1.group(1))    ###   无输出
print(result2.group(1))    ###   KEraCN




import re 
content = '''Hello 1234567 World_This
is a Regex Demo
'''
	
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
# result = re.match('^He.*?(\d+).*?Demo$', content)
print(result.group(1))

### 1234567      因为\.匹配的是除换行符之外的任意字符，当遇到换行符时，.*?就不能匹配了，所以导致匹配失败。这里只需加一个修饰符re.S
####   如果不加 re.S  则报异常    ：  result 为空的， 所以导致异常
# Traceback (most recent call last):
#   File "reTest.py", line 91, in <module>
#     print(result.group(1))
# AttributeError: 'NoneType' object has no attribute 'group'


###转义匹配
import re
content = '(百度)www.baidu.com'
result = re.match('\(百度\)www\.baidu\.com', content)
print(result)

### <_sre.SRE_Match object; span=(0, 17), match='(百度)www.baidu.com'>




import re 
content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.match('^Hello.*?(\d+).*?Demo$', content)
print(result)

# None
# match()方法是从字符串的开头开始匹配的，一旦开头不匹配，那么整个匹配就失败了

# 方法search()，它在匹配时会扫描整个字符串，然后返回第一个成功匹配的结果。
# 也就是说，正则表达式可以是字符串的一部分，在匹配时，search()方法会依次扫描字符串，
# 直到找到第一个符合规则的字符串，然后返回匹配内容，如果搜索完了还没有找到，就返回None

import re
content = 'Extra stings Hello 1234567 World_This is a Regex Demo'
result = re.search('Hello.*?(\d+).*?Demo$', content)
print(result)

# <_sre.SRE_Match object; span=(13, 53), match='Hello 1234567 World_This is a Regex Demo'>
###   如果  ^   以这个开头，则匹配不到， 因为这是开头的标志


import re
html =  '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>'''

# result = re.search('<li.*?active.*?singer="(.?*)">(.*?)</a>',html)
result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
print(result)
if result:
	print(result.group(0))
	print(result.group(1))  #齐秦
	print(result.group(2))  #往事随风


# <li data-view="2">一路上有你</li>
#         <li data-view="7">
#             <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
#         </li>
#         <li data-view="4" class="active">
#             <a href="/3.mp3" singer="齐秦">往事随风</a>

# 齐秦
# 往事随风


result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)
if result:
	print(result.group(1), result.group(2))    #任贤齐 沧海一声笑


###  因为去掉了 active  所以  search 方法 会匹配到第一个（任贤齐 沧海一声笑 ）  然后就返回了
###  re.S    是为了能够使  .*?  匹配进行换行

result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html)
if result:
	print(result.group(1), result.group(2))    ###  beyond 光辉岁月

### 当没有换行的参数（re.S） 是， 匹配到了 beyond 光辉岁月


result = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
print(result)
print(type(result))
for resu in result:
	print(resu)
	print(resu[0], resu[1], resu[2])

# [('/2.mp3', '任贤齐', '沧海一声笑'), ('/3.mp3', '齐秦', '往事随风'), ('/4.mp3', 'beyond', '光辉岁月'), ('/5.mp3', '陈慧琳', '记事本'), ('/6.mp3', '邓丽君', '<i class="fa fa-user"></i>但愿人长久')]
# <class 'list'>
# ('/2.mp3', '任贤齐', '沧海一声笑')
# /2.mp3 任贤齐 沧海一声笑
# ('/3.mp3', '齐秦', '往事随风')
# /3.mp3 齐秦 往事随风
# ('/4.mp3', 'beyond', '光辉岁月')
# /4.mp3 beyond 光辉岁月
# ('/5.mp3', '陈慧琳', '记事本')
# /5.mp3 陈慧琳 记事本
# ('/6.mp3', '邓丽君', '<i class="fa fa-user"></i>但愿人长久')
# /6.mp3 邓丽君 <i class="fa fa-user"></i>但愿人长久



import re 
content = '54aK54yr5oiR54ix5L2g'
content = re.sub('\d+', '', content)
print(content)    #aKyroiRixLg


### sub():   第一个参数传入\d+来匹配所有的数字，第二个参数为替换成的字符串（
###      如果去掉该参数的话，可以赋值为空），第三个参数是原字符串


import re 
result = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', html, re.S)
for resu in result:
	print(resu[1])

# 一路上有你
# 沧海一声笑
# 往事随风
# 光辉岁月
# 记事本
# 但愿人长久

html = re.sub('<a.*?>|</a>', '', html)
html = re.sub('<i.*?i>','', html)
print(html)
result = re.findall('<li.*?>(.*?)</li>', html, re.S)
for resu in result:
	print(resu.strip())

# 一路上有你
# 沧海一声笑
# 往事随风
# 光辉岁月
# 记事本
# 但愿人长久

import re 
content1 = '2016-12-12 12:00'
content2 = '2016-11-11 13:22'
content3 = '2016-10-10 02:21'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)

# 2016-12-12  2016-11-11  2016-10-10 
