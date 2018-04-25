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