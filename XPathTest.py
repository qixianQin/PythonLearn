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