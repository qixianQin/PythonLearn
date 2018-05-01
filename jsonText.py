# -*- conding:utf-8 -*- 

###  JSON 文件存储 

import json 
import re
str = '''
[{
	'name':'Bob',
	'gender':'male',
	'biethday':'1992-12-12'
},
{
	'name':'Selina',
	'gender':'famale',
	'birthday':'1991-12-21'
}
]
'''
str = re.sub('\'', '\"', str)   #   JSON中  不能试单引号，负责会报错：json.decoder.JSONDecodeError
print(type(str))
data = json.loads(str)
print(data)
print(type(data))

# <class 'str'>
# [{'name': 'Bob', 'gender': 'male', 'biethday': '1992-12-12'}, {'name': 'Selina', 'gender': 'famale', 'birthday': '1991-12-21'}]
# <class 'list'>

print(data[0]['name'])   #  Bob
print(data[0].get('name'))   # Bob

print(data[0].get('age'))     #  None
print(data[0].get('age', 25))    #  25     25为默认值，如果取不到age,  则返回默认值



import json 
with open('data.json', 'r') as file:
	str = file.read()
	data = json.loads(str)
	print(data)

# [{'name': 'Bob', 'gender': 'male', 'biethday': '1992-12-12'},
#  {'name': 'Selina', 'gender': 'famale', 'birthday': '1991-12-21'}]


import json 
data = [
{
	'name':'Bod',
	'gender':'male',
	'birthday':'1991-12-21'
}]

with open('data2.json', 'w+') as file:
	file.write(json.dumps(data, indent=2))       ##  生成 data2.json 文件
###  参数indent，代表缩进字符个数


import json
data=[
{
	'name':'中国',
	'gender':'男',
	'birthday':'1949-10-01'
}]

with open('data2.json', 'a+') as file:
	file.write(json.dumps(data, indent=2))

# [
#   {
#     "name": "\u4e2d\u56fd",       中文转换成了Unicode编码了
#     "gender": "\u7537",
#     "birthday": "1949-10-01"
#   }
# ]

import json
data=[
{
	'name':'中国',
	'gender':'男',
	'birthday':'1949-10-01'
}]

with open('data2.json', 'a+', encoding='utf-8') as file:    #  指定编码格式
	file.write(json.dumps(data, indent=2, ensure_ascii=False))   # 中文需要设置ensure_ascii为False

# [
#   {
#     "name": "中国",
#     "gender": "男",
#     "birthday": "1949-10-01"
#   }
# ]


