# -*- conding:utf-8 -*- 

###   XPath   使用练习

from lxml import etree
text = '''
	<div>
		<ul>
			 <li class="item-0"><a href="link1.html">first item</a></li>
	         <li class="item-1"><a href="link2.html">second item</a></li>
	         <li class="item-inactive"><a href="link3.html">third item</a></li>
	         <li class="item-1"><a href="link4.html">fourth item</a></li>
	         <li class="item-0"><a href="link5.html">fifth item</a>
		</ul>
	</div> '''
html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))

### 先导入lxml库的etree模块，然后声明了一段HTML文本，调用HTML类进行初始化，这样就成功构造了一个XPath解析对象
### HTML文本中的最后一个li节点是没有闭合的，但是etree模块可以自动修正HTML文本

# <html><body><div>
# 		<ul>
# 			 <li class="item-0"><a href="link1.html">first item</a></li>
# 	         <li class="item-1"><a href="link2.html">second item</a></li>
# 	         <li class="item-inactive"><a href="link3.html">third item</a></li>
# 	         <li class="item-1"><a href="link4.html">fourth item</a></li>
# 	         <li class="item-0"><a href="link5.html">fifth item</a>
# 		</li></ul>
# 	</div> </body></html>


###  直接读取文件

from lxml import etree
html = etree.parse('./htmlModeTest.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))

####  输出多了  DOCTYPE 信息

# <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" "http://www.w3.org/TR/REC-html40/loose.dtd">
# <html><body><div>&#13;
#     <ul>&#13;
#          <li class="item-0"><a href="link1.html">first item</a></li>&#13;
#          <li class="item-1"><a href="link2.html">second item</a></li>&#13;
#          <li class="item-inactive"><a href="link3.html">third item</a></li>&#13;
#          <li class="item-1"><a href="link4.html">fourth item</a></li>&#13;
#          <li class="item-0"><a href="link5.html">fifth item</a>&#13;
#      </li></ul>&#13;
#  </div></body></html>


####   用//开头的XPath规则来选取所有符合要求的节点
from lxml import etree
html = etree.parse('./htmlModeTest.html', etree.HTMLParser())
result = html.xpath('//*')
print(result)

## 使用*代表匹配所有节点，也就是整个HTML文本中的所有节点都会被获取。可以看到，
## 返回形式是一个列表，每个元素是Element类型，其后跟了节点的名称，如html、
## body、div、ul、li、a等，所有节点都包含在列表中了


# [<Element html at 0x212ff3d4908>, <Element body at 0x212ff3d47c8>, 
# <Element div at 0x212ff3d4888>, <Element ul at 0x212ff3d4848>,
#  <Element li at 0x212ff3d4948>, <Element a at 0x212ff3d49c8>, 
#  <Element li at 0x212ff3d4a08>, <Element a at 0x212ff3d4a48>, 
#  <Element li at 0x212ff3d4a88>, <Element a at 0x212ff3d4988>, 
#  <Element li at 0x212ff3d4ac8>, <Element a at 0x212ff3d4b08>,
#   <Element li at 0x212ff3d4b48>, <Element a at 0x212ff3d4b88>]


## 匹配也可以指定节点名称
from lxml import etree
html = etree.parse('./htmlModeTest.html', etree.HTMLParser())
result = html.xpath('//li')
print(result)
print(result[0])

# [<Element li at 0x245e3994d48>, <Element li at 0x245e3994d88>, <Element li at 0x245e3994dc8>, <Element li at 0x245e3994e08>, <Element li at 0x245e3994e48>]
# <Element li at 0x245e3994d48>


###  通过/或//即可查找元素的子节点或子孙节点  
from lxml import etree
html = etree.parse('./htmlModeTest.html', etree.HTMLParser())
result = html.xpath('//li/a')
print(result)

### 这里通过追加/a即选择了所有li节点的所有直接a子节点。因为//li用于选中所有li节点，
### /a用于选中li节点的所有直接子节点a，二者组合在一起即获取所有li节点的所有直接a子节点。
# [<Element a at 0x1b18a4c4c08>, <Element a at 0x1b18a4c4c48>, 
# <Element a at 0x1b18a4c4888>, <Element a at 0x1b18a4c4848>, 
# <Element a at 0x1b18a4c4948>]

### 此处的/用于选取直接子节点，如果要获取所有子孙节点，就可以使用//。
###  例如，要获取ul节点下的所有子孙a节点

from lxml import etree
html = etree.parse('./htmlModeTest.html', etree.HTMLParser())
result = html.xpath('//ul//a')
print(result)

### 与从  li 下 取子节点 a 结果一样
# [<Element a at 0x1c4626a4908>, <Element a at 0x1c4626a47c8>, 
# <Element a at 0x1c4626a4d88>, <Element a at 0x1c4626a4dc8>,
#  <Element a at 0x1c4626a4e08>]

## 如果这里用//ul/a，就无法获取任何结果了。因为/用于获取直接子节点，
## 而在ul节点下没有直接的a子节点，只有li节点，所以无法获取任何匹配结果

from lxml import etree
html = etree.parse('./htmlModeTest.html', etree.HTMLParser())
result = html.xpath('//ul/a')
print(result)

## []    

##  因此，这里我们要注意/和//的区别，其中/用于获取直接子节点，//用于获取子孙节点


###  通过连续的/或//可以查找子节点或子孙节点    知道子节点可以通过 .. 来查找父节点
from  lxml import etree
html = etree.parse('./htmlModeTest.html', etree.HTMLParser())
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)


## 原： <li class="item-1"><a href="link4.html">fourth item</a></li>
#['item-1']


###  也可以通过parent::来获取父节点
from lxml import etree
html = etree.parse('./htmlModeTest.html', etree.HTMLParser())
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)

##  ['item-1']     parent:: 后加了个 *    ：  
###   不加  * 号 报错：
# Traceback (most recent call last):
#   File "XPathTest.py", line 138, in <module>
#     result = html.xpath('//a[@href="link4.html"]/parent::/@class')
#   File "src\lxml\etree.pyx", line 2277, in lxml.etree._ElementTree.xpath
#   File "src\lxml\xpath.pxi", line 359, in lxml.etree.XPathDocumentEvaluator.__call__
#   File "src\lxml\xpath.pxi", line 227, in lxml.etree._XPathEvaluatorBase._handle_result
# lxml.etree.XPathEvalError: Invalid expression



###  属性匹配 
###  @ 符号 进行属性过滤 
from lxml import etree 
html = etree.parse('./htmlModeTest.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]')
print(result)

# <li class="item-0"><a href="link1.html">first item</a></li>
#  <li class="item-0"><a href="link5.html">fifth item</a>
### 有两个匹配：  [<Element li at 0x2360b6e49c8>, <Element li at 0x2360b6e47c8>]



####    文本获取
from lxml import etree
html = etree.parse('./htmlModeTest.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]/text()')
print(result) 

##   ['\r\n     ']
###  XPath中text()前面是/，而此处/的含义是选取直接子节点，很明显li的直接子节点都是a节点，
###  本都是在a节点内部的，所以这里匹配到的结果就是被修正的li节点内部的换行符，因为自动
### 修正的li节点的尾标签换行了
###  <li class="item-0"><a href="link1.html">first item</a></li>
#    <li class="item-0"><a href="link5.html">fifth item</a>
#    </li>   （etree.parse() 后自动修复）


from lxml import etree
html = etree.parse('./htmlModeTest.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result) 

### ['first item', 'fifth item']     从 a 节点里面获得 text（） 内容


from lxml import etree
html = etree.parse('./htmlModeTest.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]//text()')
print(result) 

####   ['first item', 'fifth item', '\r\n     ']       // ：  选取所有子孙节点的文本

### 属性获取

from lxml import etree
html = etree.parse('./htmlModeTest.html', etree.HTMLParser())
result = html.xpath('//li/a/@href')
print(result)


# ['link1.html', 'link2.html', 'link3.html', 'link4.html', 'link5.html']

##  此处和属性匹配的方法不同，属性匹配是中括号加属性名和值来限定某个属性，
##  如[@href="link1.html"]，而此处的@href指的是获取节点的某个属性


###   属性多值匹配：
from lxml import etree
text = '''
	<li class = "li li-first"><a href = "link.html">first item</a></li>
'''
html = etree.HTML(text)
# html = etree.parse(text, etree.HTMLParser())
result = html.xpath('//li[@class="li"]/a/text()')
print(result)
##  []     li节点的class属性有两个值li和li-first, 所以无法匹配



from lxml import etree
text = '''
	<li class = "li li-first"><a href = "link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)

#  ['first item']



###  根据多个属性确定一个节点，这时就需要同时匹配多个属性。此时可以使用运算符and来连接

from lxml import etree
text = '''
 <li class = "li li-first" name = "item"><a href = "link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result)

# ['first item']
# li节点又增加了一个属性name。要确定这个节点，需要同时根据class和name属性来选择，
# 一个条件是class属性里面包含li字符串，另一个条件是name属性为item字符串，
# 二者需要同时满足，需要用and操作符相连，相连之后置于中括号内进行条件筛选

