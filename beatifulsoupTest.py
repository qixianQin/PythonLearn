# -*- coding:utf-8 -*- 

##   使用Beautiful Soup

from bs4 import BeautifulSoup
soup = BeautifulSoup('<p>Hello</p>', 'lxml')
print(soup.p.string)

#  Hello  


html ="""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

from bs4 import BeautifulSoup 
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
print(soup.title.string)

###  首先声明变量html，它是一个HTML字符串。但是需要注意的是，它并不是一个完整的HTML字符串，
### 因为body和html节点都没有闭合。接着，我们将它当作第一个参数传给BeautifulSoup对象，该对
### 象的第二个参数为解析器的类型（这里使用lxml），此时就完成了BeaufulSoup对象的初始化。
### 然后，将这个对象赋值给soup变量
### 调用prettify()方法。这个方法可以把要解析的字符串以标准的缩进格式输出。
# 这里需要注意的是，输出结果里面包含body和html节点，也就是说对于不标准的HTML字符串
# BeautifulSoup，可以自动更正格式。这一步不是由prettify()方法做的，而是在初始化BeautifulSoup
# 时就完成了

###   soup.title.string  获取 title的值

# <html>
#  <head>
#   <title>
#    The Dormouse's story
#   </title>
#  </head>
#  <body>
#   <p class="title" name="dromouse">
#    <b>
#     The Dormouse's story
#    </b>
#   </p>
#   <p class="story">
#    Once upon a time there were three little sisters; and their names were
#    <a class="sister" href="http://example.com/elsie" id="link1">
#     <!-- Elsie -->
#    </a>
#    ,
#    <a class="sister" href="http://example.com/lacie" id="link2">
#     Lacie
#    </a>
#    and
#    <a class="sister" href="http://example.com/tillie" id="link3">
#     Tillie
#    </a>
#    ;
# and they lived at the bottom of a well.
#   </p>
#   <p class="story">
#    ...
#   </p>
#  </body>
# </html>


from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.title)     ##  <title>The Dormouse's story</title>
print(type(soup.title))    ##  <class 'bs4.element.Tag'>
print(soup.title.string)    ##  The Dormouse's story
print(soup.head)   ### <head><title>The Dormouse's story</title></head>
print(soup.p)   ### (只会匹配到第一个P)<p class="title" name="dromouse"><b>The Dormouse's story</b></p>

#这里依然选用刚才的HTML代码，首先打印输出title节点的选择结果，输出结果正是title节点加里面
# 的文字内容。接下来，输出它的类型，是bs4.element.Tag类型，这是Beautiful Soup中一个重要的数
# 据结构。经过选择器选择后，选择结果都是这种Tag类型。Tag具有一些属性，比如string属性，调用
# 该属性，可以得到节点的文本内容，所以接下来的输出结果正是节点的文本内容

# 接下来，我们又尝试选择了head节点，结果也是节点加其内部的所有内容。最后，选择了p节点。
# 不过这次情况比较特殊，我们发现结果是第一个p节点的内容，后面的几个p节点并没有选到。
# 也就是说，当有多个节点时，这种选择方式只会选择到第一个匹配的节点，其他的后面节点都会
# 忽略


###    提取信息
from bs4 import BeautifulSoup 
soup = BeautifulSoup(html, 'lxml')
print(soup.title.name)   ###  提取名称
print(soup.p.attrs)    ###  提取属性
print(soup.p.attrs['name'])  ###  提取指定属性
print(soup.p['name'])   ###  提取属性   name属性的值是唯一的，返回的结果就是单个字符串
print(soup.p['class'])   ### 提取属性   对于class，一个节点元素可能有多个class，所以返回的是列表。在实际处理过程中，我们要注意判断类型。
print(soup.p.string)  ###   string属性获取节点元素包含的文本内容    如果有多个P， 则只返回第一个

# title
# {'class': ['title'], 'name': 'dromouse'}
# dromouse
# dromouse
# ['title']
# The Dormouse's story


###  嵌套选择

html2 = '''
<html><head><title>The Dormouse's story</title></head>
<body>
'''
from bs4 import BeautifulSoup 
soup = BeautifulSoup(html2, 'lxml')
print(soup.head.title)
print(type(soup.head.title))      ##  返回的类型 都是   bs4.element.Tag 
print(soup.head.title.string)


# <title>The Dormouse's story</title>
# <class 'bs4.element.Tag'>
# The Dormouse's story


html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

from bs4 import BeautifulSoup 
soup = BeautifulSoup(html, 'lxml')
print(soup.p)

# 	<p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a class="sister" href="http://example.com/elsie" id="link1">
# <span>Elsie</span>
# </a>
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> 
#             and
#             <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
#             and they lived at the bottom of a well.
#         </p>)

from bs4 import BeautifulSoup 
soup = BeautifulSoup(html, 'lxml')
print(soup.p.children)    ### <list_iterator object at 0x00000183AC2CC390>
for i, child in enumerate(soup.p.children):     ###  得到了子节点
	print(i, child)

# 0 
#             Once upon a time there were three little sisters; and their names were
            
# 1 <a class="sister" href="http://example.com/elsie" id="link1">
# <span>Elsie</span>
# </a>
# 2 

# 3 <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# 4  
#             and
            
# 5 <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
# 6 
#             and they lived at the bottom of a well.


####  如果要得到所有的子孙节点的话，可以调用descendants属性
from bs4 import BeautifulSoup 
soup = BeautifulSoup(html, 'lxml')
print(soup.p.descendants)    ### <generator object descendants at 0x0000021CA7721048>
for i, child in enumerate(soup.p.descendants):     ###  得到了所有子孙节点
	print(i, child)

# 0 
#             Once upon a time there were three little sisters; and their names were
            
# 1 <a class="sister" href="http://example.com/elsie" id="link1">
# <span>Elsie</span>
# </a>
# 2 

# 3 <span>Elsie</span>
# 4 Elsie
# 5 

# 6 

# 7 <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# 8 Lacie
# 9  
#             and
            
# 10 <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
# 11 Tillie
# 12 
            # and they lived at the bottom of a well.



html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
        </p>
        <p class="story">...</p>
"""

####   取某个节点元素的父节点，可以调用parent属性
from bs4 import BeautifulSoup 
soup = BeautifulSoup(html, 'lxml')
print(soup.a.parent) 

# <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a class="sister" href="http://example.com/elsie" id="link1">
# <span>Elsie</span>
# </a>
# </p>          



html = """
<html>
    <body>
        <p class="story">
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
        </p>
"""

####   获取所有的祖先节点，可以调用parents属性：    prent:  获取直接的父节点（一个）
from bs4 import BeautifulSoup 
soup = BeautifulSoup(html, 'lxml')
print(type(soup.a.parents))     ###  <class 'generator'>
print(list(enumerate(soup.a.parents)))

# [(0, <p class="story">
# <a class="sister" href="http://example.com/elsie" id="link1">
# <span>Elsie</span>
# </a>
# </p>), (1, <body>
# <p class="story">
# <a class="sister" href="http://example.com/elsie" id="link1">
# <span>Elsie</span>
# </a>
# </p>
# </body>), (2, <html>
# <body>
# <p class="story">
# <a class="sister" href="http://example.com/elsie" id="link1">
# <span>Elsie</span>
# </a>
# </p>
# </body></html>), (3, <html>
# <body>
# <p class="story">
# <a class="sister" href="http://example.com/elsie" id="link1">
# <span>Elsie</span>
# </a>
# </p>
# </body></html>)]



####  获取兄弟节点
html = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            Hello
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
"""

### 提取兄弟节点信息
### 其中next_sibling和previous_sibling分别获取节点的下一个和上一个兄弟元素，
###  next_siblings和previous_siblings则分别返回所有前面和后面的兄弟节点的生成器
from bs4 import BeautifulSoup 
soup = BeautifulSoup(html, 'lxml')
print('Next Sibling', soup.a.next_sibling)
print('Prev Sibling', soup.a.previous_sibling)
print('Next Siblings', list(enumerate(soup.a.next_siblings)))
print('Prev Siblings', list(enumerate(soup.a.previous_siblings)))


# Next Sibling 
#             Hello
            
# Prev Sibling 
#             Once upon a time there were three little sisters; and their names were
            
# Next Siblings [(0, '\n            Hello\n            '), (1, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>), (2, ' \n            and\n            '), (3, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>), (4, '\n            and they lived at the bottom of a well.\n        ')]
# Prev Siblings [(0, '\n            Once upon a time there were three little sisters; and their names were\n            ')]



html = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">Bob</a><a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
        </p>
"""

####  提取节点信息
##  可以直接调用string、attrs等属性获得其文本和属性
## 如果返回结果是多个节点的生成器，则可以转为列表后取出某个元素，
## 然后再调用string、attrs等属性获取其对应节点的文本和属性
from bs4 import BeautifulSoup 
soup = BeautifulSoup(html, 'lxml')
print('Next Sibling:')
print(type(soup.a.next_sibling))     #  bs4.element.Tag
print(soup.a.next_sibling)
print(soup.a.next_sibling.string)
print('Parent:')
print(type(soup.a.parents))
print(list(soup.a.parents)[0])
print(list(soup.a.parents)[0].attrs['class'])


# Next Sibling:
# <class 'bs4.element.Tag'>
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# Lacie
# Parent:
# <class 'generator'>
# <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a class="sister" href="http://example.com/elsie" id="link1">Bob</a><a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# </p>
# ['story']



###  find_all，顾名思义，就是查询所有符合条件的元素。给它传入一些属性或文本，
###  就可以得到符合条件的元素，它的功能十分强大。

	
##  find_all(name , attrs , recursive , text , **kwargs)


html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name='elements'>
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

##  name 参数：
from bs4 import BeautifulSoup 
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(name='ul'))
print(type(soup.find_all(name='ul')[0]))    #  <class 'bs4.element.Tag'>

# [<ul class="list" id="list-1">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# <li class="element">Jay</li>
# </ul>, <ul class="list list-small" id="list-2">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# </ul>]
# <class 'bs4.element.Tag'>

from bs4 import BeautifulSoup 
soup = BeautifulSoup(html, 'lxml')
for ul in soup.find_all(name='ul'):
	print(ul.find_all(name='li'))
	for li in ul.find_all(name='li'):
		print(li.string)

# [<li class="element">Foo</li>, <li class="element">Bar</li>, <li class="element">Jay</li>]
# Foo
# Bar
# Jay
# [<li class="element">Foo</li>, <li class="element">Bar</li>]
# Foo
# Bar



####  attrs  参数：  参数的类型是字典类型
from bs4 import BeautifulSoup 
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(attrs={'id':'list-1'}))
print(soup.find_all(attrs={'name':'elements'}))

# [<ul class="list" id="list-1" name="elements">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# <li class="element">Jay</li>
# </ul>]
# [<ul class="list" id="list-1" name="elements">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# <li class="element">Jay</li>
# </ul>]


####对于一些常用的属性，比如id和class等，我们可以不用attrs来传递

from bs4 import BeautifulSoup 
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(id='list-1'))
print('name attr:', soup.find_all(class_='element'))

##  由于class在Python里是一个关键字，所以后面需要加一个下划线，即class_='element'，
##  返回的结果依然还是Tag组成的列表

# [<ul class="list" id="list-1" name="elements">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# <li class="element">Jay</li>
# </ul>]
# name attr: [<li class="element">Foo</li>, <li class="element">Bar</li>, 
# <li class="element">Jay</li>, <li class="element">Foo</li>, 
# <li class="element">Bar</li>]



###   text参数可用来匹配节点的文本，传入的形式可以是字符串，可以是正则表达式对象

import re 
from bs4 import BeautifulSoup 

html3 = '''
<div class='panel'>
	<div class='panel-body'>
		<a> Hello, this is a link</a>
		<a> Hello, this is a link, too</a>
	</div>
</div>
'''
soup = BeautifulSoup(html3, 'lxml')
print(soup.find_all(text=re.compile('link')))

##  [' Hello, this is a link', ' Hello, this is a link, too']


###  find_all()方法，还有find()方法，只不过后者返回的是单个元素，也就是第一个匹配的元素，
###  而前者返回的是所有匹配的元素组成的列表

html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

from bs4 import BeautifulSoup 
soup = BeautifulSoup(html, 'lxml')
print(soup.find(name='ul'))
print(type(soup.find(name='ul')))   ##  <class 'bs4.element.Tag'>
print(soup.find(class_='list'))

# <ul class="list" id="list-1">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# <li class="element">Jay</li>
# </ul>
# <class 'bs4.element.Tag'>
# <ul class="list" id="list-1">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# <li class="element">Jay</li>
# </ul>



##   find*  方法：
# find_parents()和find_parent()：前者返回所有祖先节点，后者返回直接父节点。
# find_next_siblings()和find_next_sibling()：前者返回后面所有的兄弟节点，后者返回后面第一个兄弟节点。
# find_previous_siblings()和find_previous_sibling()：前者返回前面所有的兄弟节点，后者返回前面第一个兄弟节点。
# find_all_next()和find_next()：前者返回节点后所有符合条件的节点，后者返回第一个符合条件的节点。
# find_all_previous()和find_previous()：前者返回节点后所有符合条件的节点，后者返回第一个符合条件的节点



###   使用CSS选择器时，只需要调用select()方法，传入相应的CSS选择器即可

html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

from bs4 import BeautifulSoup 
soup = BeautifulSoup(html, 'lxml')
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))     ##  <class 'bs4.element.Tag'>


# [<div class="panel-heading">
# <h4>Hello</h4>
# </div>]
# [<li class="element">Foo</li>, <li class="element">Bar</li>, <li class="element">Jay</li>, <li class="element">Foo</li>, <li class="element">Bar</li>]
# [<li class="element">Foo</li>, <li class="element">Bar</li>]
# <class 'bs4.element.Tag'>



from bs4 import BeautifulSoup 
soup = BeautifulSoup(html, 'lxml')
for ul in soup.select('ul'):
	print(ul.select('li'))


# [<li class="element">Foo</li>, <li class="element">Bar</li>, <li class="element">Jay</li>]
# [<li class="element">Foo</li>, <li class="element">Bar</li>]


from bs4 import BeautifulSoup 
soup = BeautifulSoup(html, 'lxml')
for ul in soup.select('ul'):
	print(ul['id'])
	print(ul.attrs['id'])

# list-1
# list-1
# list-2
# list-2


from bs4 import BeautifulSoup 
soup = BeautifulSoup(html, 'lxml')
for li in soup.select('li'):
	print('Get text:', li.get_text())
	print('string:', li.string)


# Get text: Foo
# string: Foo
# Get text: Bar
# string: Bar
# Get text: Jay
# string: Jay
# Get text: Foo
# string: Foo
# Get text: Bar
# string: Bar