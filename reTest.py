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