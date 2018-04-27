# -*- coding:utf-8 -*- 

#### 测试提取信息的 正则表达式
####  提取信息包过： 
####  排名、图片、 名称、主演、发布时间、评分
import re

html = '''<dd><i class="board-index board-index-2">2</i>
    <a href="/films/1297" title="肖申克的救赎" class="image-link" data-act="boarditem-click" data-val="{movieId:1297}">
      <img src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="http://p0.meituan.net/movie/__40191813__4767047.jpg@160w_220h_1e_1c" alt="肖申克的救赎" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1297" title="肖申克的救赎" data-act="boarditem-click" data-val="{movieId:1297}">肖申克的救赎</a></p>
        <p class="star">
                主演：蒂姆·罗宾斯,摩根·弗里曼,鲍勃·冈顿
        </p>
<p class="releasetime">上映时间：1994-10-14(美国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
    </div>

      </div>
    </div>

                </dd>
'''

###  提取排名
result = re.match('<dd.*?board-index.*?>(.*?)</i>', html, re.S)
print(result.group(0))    ##  <dd><i class="board-index board-index-2">2</i>
print(result.group(1))    ##  2


###  提取图片
result = re.match('<dd.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)"', html, re.S)
print(result.group(1))
print(result.group(2))   ##http://p0.meituan.net/movie/__40191813__4767047.jpg@160w_220h_1e_1c

### 提取名称
result = re.match('<dd.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?title="(.*?)"', html, re.S)
print(result.group(3))    ## 肖申克的救赎

####提取主演

result = re.match('<dd.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?title="(.*?)".*?star">(.*?)</p>', html, re.S)
print(result.group(4))    ## 主演：蒂姆·罗宾斯,摩根·弗里曼,鲍勃·冈顿

####提取上映时间
result = re.match('<dd.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?title="(.*?)".*?star">(.*?)</p>.*?releasetime">(.*?)</p>', html, re.S)
print(result.group(5))    ## 上映时间：1994-10-14(美国)

####提取上映评分
result = re.match('<dd.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?title="(.*?)".*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', html, re.S)
print(result.group(6),result.group(7))    ## 9. 5  
