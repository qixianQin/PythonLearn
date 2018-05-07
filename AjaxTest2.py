# -*- conding:utf-8 -*-

import requests 

# headers = {
# 	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# 'Accept-Encoding': 'gzip, deflate, br',
# 'Accept-Language': 'zh-CN,zh;q=0.9',
# 'Cache-Control': 'max-age=0',
# 'Connection': 'keep-alive',
# 'Cookie': '_T_WM=3aea36b962d68623ae34e9da7a1ef9b1; MLOGIN=0; WEIBOCN_FROM=1110006030; M_WEIBOCN_PARAMS=fid%3D1076032830678474%26uicode%3D10000011',
# 'Host': 'm.weibo.cn',
# 'Upgrade-Insecure-Requests': '1',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
# }

# base_url = 'https://m.weibo.cn/u/2830678474'

# response = requests.get(base_url, headers=headers)
# print(type(response))
# print(response.text)




from urllib.parse import urlencode
import requests

base_url =  'https://m.weibo.cn/api/container/getIndex?' 
#    type=uid&value=2830678474&containerid=1076032830678474&page=4

headers = {
	'Accept': 'application/json, text/plain, */*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Cookie': '_T_WM=3aea36b962d68623ae34e9da7a1ef9b1; MLOGIN=0; WEIBOCN_FROM=1110006030; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D1076032830678474%26fid%3D1076032830678474%26uicode%3D10000011',
'Host': 'm.weibo.cn',
'Referer': 'https://m.weibo.cn/u/2830678474',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'
}


def get_page(page):
	params = {
		'type':'uid',
		'value':'2830678474',
		'containerid':'1076032830678474',
		'page':page
	}
	url = base_url+urlencode(params)
	try:
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			return response.json()
	except requests.ConnectionError as e:
		print('Error', e.args)

from pyquery import PyQuery as pq 
def parse_page(json):
	if json:
		items = json.get('data').get('cards')
		for item in items:
			item = item.get('mblog')
			weibo = {}
			weibo['id'] = item.get('id')
			weibo['text'] = pq(item.get('text')).text()
			weibo['attitudes'] = item.get('attitudes_count')
			weibo['comments'] = item.get('comments_count')
			weibo['reposts'] = item.get('reposts_count')
			yield weibo


if __name__ == '__main__':
	for page in range(1,11):
		json = get_page(page)
		results = parse_page(json)
		for result in results:
			print(result)





# {'id': '4236412457436086', 'text': '//@不吃胡萝卜的兔子李：他不认识这个字，是怎么打出来的', 'attitudes': 0, 'comments': 2, 'reposts': 0}
# {'id': '4236047347549333', 'text': '这是你们心心念念的Python网络爬虫秘籍，这文案值一百万！😂这是你们心心念念的Python网络爬虫秘籍', 'attitudes': 13, 'comments': 4, 'reposts': 1}
# {'id': '4235932129554169', 'text': '@请叫我汪二 @wonderly321 @FindHaoX86', 'attitudes': 0, 'comments': 2, 'reposts': 3}
# {'id': '4235930993055500', 'text': '【转发抽奖赠书】《Python3网络爬虫开发实战》来了！文末另有抽奖送书及优惠券福利！活动链接: 《Python3网络爬虫开发实战》来了！文末另有抽奖送书及优惠券福利！ 另外转发本微博并艾特三位好友，5.15抽奖再送三本！', 'attitudes': 13, 'comments': 30, 'reposts': 145}
# {'id': '4235244779504608', 'text': '可以说非常用心了！', 'attitudes': 3, 'comments': 6, 'reposts': 1}
# {'id': '4233711535096892', 'text': '', 'attitudes': 4, 'comments': 0, 'reposts': 5}
# {'id': '4233470869992736', 'text': 'Python操作Redis，你要的都在这了！ Python操作Redis，你要的都在这了！', 'attitudes': 4, 'comments': 2, 'reposts': 21}
# {'id': '4233365407947785', 'text': 'ICLR 2018最佳论文AMSGrad能够取代Adam吗网页链接', 'attitudes': 2, 'comments': 0, 'reposts': 0}
# {'id': '4232795331191333', 'text': 'Python操作MySQL存储，这些你都会了吗？ Python操作MySQL存储，这些你都会了吗？', 'attitudes': 3, 'comments': 1, 'reposts': 5}
# {'id': '4232466967536307', 'text': '如何改进梯度下降算法 如何改进梯度下降算法', 'attitudes': 3, 'comments': 0, 'reposts': 2}
# {'id': '4232022740813057', 'text': 'Python操作MongoDB看这一篇就够了 Python操作MongoDB看这一篇就够了', 'attitudes': 10, 'comments': 1, 'reposts': 11}
# {'id': '4231380046999320', 'text': '给力！//@梁斌penny:6月份计划在北京召开人类历史上第二次爬虫大会，谢谢//@蚁工厂://@图灵教育:感谢 @梁斌penny 老师的推荐，首发上市的签名版已经售空，大批书籍已经在路上啦！期待～', 'attitudes': 7, 'comments': 2, 'reposts': 0}
# {'id': '4231378289738604', 'text': '求帮投下70号，谢谢！', 'attitudes': 0, 'comments': 0, 'reposts': 0}
# {'id': '4231378159274473', 'text': '3个关键点，把你的TensorFlow代码重构为分布式！网页链接', 'attitudes': 1, 'comments': 0, 'reposts': 1}
# {'id': '4231378067071372', 'text': 'Splash压力过大？来试试负载均衡吧！ Splash压力过大？来试试负载均衡吧！', 'attitudes': 0, 'comments': 0, 'reposts': 0}
# {'id': '4230984784339627', 'text': '哎呦不错哦', 'attitudes': 7, 'comments': 10, 'reposts': 0}
# {'id': '4230983370192151', 'text': '大佬们求帮投下70号，其他的几组随便投少的几个就好啦，谢谢！🙏🙏🙏爱读摄影大赛 | 开始投票啦！你的作品入围了吗？', 'attitudes': 2, 'comments': 1, 'reposts': 1}
# {'id': '4230089727551510', 'text': '', 'attitudes': 1, 'comments': 1, 'reposts': 1}
# {'id': '4230075035874699', 'text': 'Scrapy对接Docker网页链接', 'attitudes': 3, 'comments': 1, 'reposts': 0}
# {'id': '4230074364576785', 'text': '正品，有需要的吗？', 'attitudes': 0, 'comments': 3, 'reposts': 0}
# {'id': '4229064983585072', 'text': '求大家给一号投一下票谢谢！！', 'attitudes': 0, 'comments': 1, 'reposts': 0}
# {'id': '4229062484907660', 'text': '只会用Selenium爬网页？Appium爬App了解一下只会用Selenium爬网页？Appium爬App了解一下', 'attitudes': 0, 'comments': 3, 'reposts': 8}
# {'id': '4229006842768161', 'text': '《Python3网络爬虫开发实战》签名版发售了！只在京东、天猫旗舰店销售，这两个旗舰店各有150本的签名本。 链接如下： 人民邮电出版社京东官方旗舰店：网页链接 人民邮电出版社天猫官方旗舰店：宝贝详情 非签名本的店铺推荐如下： 京东自营店：网页链接 当当自营店： ...全文', 'attitudes': 10, 'comments': 19, 'reposts': 10}
# {'id': '4228882045259874', 'text': '麻烦大家给1号投一票，谢谢！校庆40周年系列活动 | 拍出最美果壳投票开始啦！~ 北京·知春路', 'attitudes': 5, 'comments': 1, 'reposts': 1}
# {'id': '4227717089666111', 'text': '滑动宫格验证码都给碰上了？没事儿，看完此文分分钟拿下！滑动宫格验证码都给碰上了？没事儿，看完此文分分钟拿下！', 'attitudes': 4, 'comments': 0, 'reposts': 2}
# {'id': '4227643290727223', 'text': '我的《Python3网络爬虫开发实战》等了好久今天终于拿到实体书了😊，印刷质量超赞！首印四千，签了六百，接下来就坐等发货啦🤗 廊坊', 'attitudes': 47, 'comments': 16, 'reposts': 4}
# {'id': '4227285433350553', 'text': '独立循环神经网络（IndRNN）：打造更长更深的RNN网页链接', 'attitudes': 0, 'comments': 1, 'reposts': 0}
# {'id': '4226949347438739', 'text': '妈妈再也不用担心爬虫被封号了！手把手教你搭建Cookies池妈妈再也不用担心爬虫被封号了！手把手教你搭建Cookies池', 'attitudes': 6, 'comments': 3, 'reposts': 2}
# {'id': '4226665733689358', 'text': '设计得超级棒！大赞！', 'attitudes': 7, 'comments': 2, 'reposts': 1}
# {'id': '4226297821389730', 'text': 'App爬虫神器mitmproxy和mitmdump的使用App爬虫神器mitmproxy和mitmdump的使用', 'attitudes': 4, 'comments': 0, 'reposts': 6}
# {'id': '4226114446621032', 'text': '熊猫守护者 我刚刚加入了“熊猫守护者”，据说会在陕西秦岭种下真实的竹子哦! 你也快来加入我们，一起为萌萌的熊猫种竹子吧！ 熊猫守护者', 'attitudes': 1, 'comments': 0, 'reposts': 0}
# {'id': '4224885469391821', 'text': '轻松获得海量稳定代理！ADSL拨号代理的搭建轻松获得海量稳定代理！ADSL拨号代理的搭建', 'attitudes': 5, 'comments': 0, 'reposts': 2}
# {'id': '4224112706612136', 'text': '付费代理的使用付费代理的使用', 'attitudes': 1, 'comments': 0, 'reposts': 3}
# {'id': '4223799942095803', 'text': '持续集成服务 Travis CI 教程持续集成服务 Travis CI 教程', 'attitudes': 1, 'comments': 0, 'reposts': 0}
# {'id': '4223438950038134', 'text': '美美美！！', 'attitudes': 3, 'comments': 0, 'reposts': 0}
# {'id': '4223334327499469', 'text': '用Flask+Aiohttp+Redis维护动态代理池用Flask+Aiohttp+Redis维护动态代理池', 'attitudes': 3, 'comments': 0, 'reposts': 2}
# {'id': '4223224894120947', 'text': '突然感觉买的苹果表有用了！', 'attitudes': 0, 'comments': 1, 'reposts': 0}
# {'id': '4223224256387116', 'text': '头条早晚凉凉', 'attitudes': 0, 'comments': 2, 'reposts': 0}
# {'id': '4222697791867332', 'text': 'Bash 脚本 set 命令教程网页链接', 'attitudes': 2, 'comments': 0, 'reposts': 0}
# {'id': '4222670113217333', 'text': 'Bash 脚本 set 命令教程', 'attitudes': 2, 'comments': 4, 'reposts': 0}
# {'id': '4222313945848883', 'text': 'Attention原理及TensorFlow AttentionWrapper源码解析网页链接', 'attitudes': 1, 'comments': 0, 'reposts': 0}
# {'id': '4221960638210673', 'text': '中文分词原理及常用Python中文分词库介绍中文分词原理及常用Python中文分词库介绍', 'attitudes': 5, 'comments': 1, 'reposts': 5}
# {'id': '4221247317933474', 'text': '', 'attitudes': 1, 'comments': 0, 'reposts': 0}
# {'id': '4220850825831849', 'text': 'Javascript - 事件顺序Javascript - 事件顺序', 'attitudes': 0, 'comments': 0, 'reposts': 0}
# {'id': '4220850728898019', 'text': 'MySQL 枚举类型的“八宗罪”MySQL 枚举类型的“八宗罪”', 'attitudes': 2, 'comments': 0, 'reposts': 2}
# {'id': '4220850469681687', 'text': '牛比牛比，惹不起惹不起', 'attitudes': 0, 'comments': 1, 'reposts': 0}
# {'id': '4218687471143291', 'text': '比特币入门教程比特币入门教程', 'attitudes': 4, 'comments': 1, 'reposts': 3}
# {'id': '4218332213712845', 'text': 'Session和Cookies的基本原理Session和Cookies的基本原理', 'attitudes': 8, 'comments': 4, 'reposts': 43}
# {'id': '4218160682589564', 'text': '京东，今天重新定义售假京东，今天重新定义售假', 'attitudes': 1, 'comments': 0, 'reposts': 1}
# {'id': '4217953869821404', 'text': '区块链入门教程区块链入门教程', 'attitudes': 3, 'comments': 1, 'reposts': 4}
# {'id': '4217644351337069', 'text': '使用requests+正则表达式爬取猫眼电影排行网页链接', 'attitudes': 3, 'comments': 1, 'reposts': 6}
# {'id': '4217204461680319', 'text': 'RESTful API 设计最佳实践RESTful API 设计最佳实践', 'attitudes': 0, 'comments': 0, 'reposts': 6}
# {'id': '4216169990645121', 'text': 'GAN的数学原理GAN的数学原理', 'attitudes': 0, 'comments': 0, 'reposts': 0}
# {'id': '4215833867434089', 'text': 'Scrapy爬虫去重效率优化之Bloom Filter的算法的对接Scrapy爬虫去重效率优化之Bloom Filter的算法的对接', 'attitudes': 4, 'comments': 0, 'reposts': 9}
# {'id': '4215428047561220', 'text': 'Scrapy-Redis分布式爬虫源码解析Scrapy-Redis分布式爬虫源码解析', 'attitudes': 5, 'comments': 0, 'reposts': 2}
# {'id': '4214250039762254', 'text': '正则表达式中零宽断言的用法正则表达式中零宽断言的用法', 'attitudes': 4, 'comments': 2, 'reposts': 0}
# {'id': '4213478929214632', 'text': '今天我升级为VIP2了', 'attitudes': 0, 'comments': 0, 'reposts': 0}
# {'id': '4212213085068020', 'text': '云上贵州的速度果然快，之前就没见进度条到一半过，就放弃了', 'attitudes': 0, 'comments': 4, 'reposts': 0}
# {'id': '4212184911166855', 'text': 'Requests库作者Kenneth Reitz的另一神作！虚拟环境及包管理工具Pipenv！Requests库作者Kenneth Reitz的另一神作！虚拟环境及包管理工具Pipenv！', 'attitudes': 3, 'comments': 3, 'reposts': 5}
# {'id': '4210435923915181', 'text': '用TensorFlow快速搭建模型！超详细的TensorFlow layers模块用法来袭！网页链接', 'attitudes': 5, 'comments': 3, 'reposts': 1}
# {'id': '4210416375052418', 'text': '玄觞王子！一开口我就跪了！太棒了！有哪些翻唱比原唱版本好听的歌曲？ - 回答作者: 九寨沟段子手 网页链接 (想看更多？下载 @知乎 App：知乎 )', 'attitudes': 0, 'comments': 2, 'reposts': 0}
# {'id': '4210307205571570', 'text': '牛逼！！！！！', 'attitudes': 3, 'comments': 0, 'reposts': 0}
# {'id': '4209894632401362', 'text': 'TensorFlow验证码识别网页链接', 'attitudes': 5, 'comments': 4, 'reposts': 1}
# {'id': '4209894448624936', 'text': '有哪些让你拍案叫绝或亮瞎狗眼的神翻译？ - 回答作者: 木马牛 网页链接 (想看更多？下载 @知乎 App：知乎 )', 'attitudes': 0, 'comments': 0, 'reposts': 0}
# {'id': '4209662045524586', 'text': '', 'attitudes': 1, 'comments': 2, 'reposts': 0}
# {'id': '4209653594716181', 'text': 'B站律师函了解一下？这也是个大事啊', 'attitudes': 0, 'comments': 1, 'reposts': 1}
# {'id': '4208983478142580', 'text': '预测个毛？先把JJ Nodick调查清楚了再说！！', 'attitudes': 1, 'comments': 1, 'reposts': 0}
# {'id': '4207661249618505', 'text': '#FindHaoX86的红包#哇！好运来袭！我抽中了@FindHaoX86 的现金红包，你也快来试试手气吧，比比谁抢得多！FindHaoX86 的红包', 'attitudes': 0, 'comments': 0, 'reposts': 0}
# {'id': '4205493654172173', 'text': '理解 Python 迭代对象、迭代器、生成器理解 Python 迭代对象、迭代器、生成器', 'attitudes': 6, 'comments': 1, 'reposts': 9}
# {'id': '4203545907477125', 'text': '爬虫代理哪家强？十大付费代理详细对比评测出炉！ 吐血之作，把所有套餐都买了测了一遍，前前后后花了将近三天才出了这篇文章，希望对大家有帮助。网页链接', 'attitudes': 40, 'comments': 11, 'reposts': 107}
# {'id': '4203178788285054', 'text': '做个代理测评真是个细活快做完的时候发现评价标准不对，全部推倒重来明天出炉详细报告', 'attitudes': 10, 'comments': 2, 'reposts': 0}
# {'id': '4203069691006792', 'text': '代码这样写不止于优雅(Python版)代码这样写不止于优雅(Python版)', 'attitudes': 2, 'comments': 0, 'reposts': 2}
# {'id': '4202623571511928', 'text': '代码这样写更优雅(Python版)网页链接', 'attitudes': 4, 'comments': 0, 'reposts': 6}
# {'id': '4201997907077988', 'text': 'HTTP基本原理HTTP基本原理', 'attitudes': 8, 'comments': 0, 'reposts': 10}
# {'id': '4201299652142610', 'text': 'Javascript调试命令——你只会Console.log() ?Javascript调试命令——你只会Console.log() ?', 'attitudes': 9, 'comments': 1, 'reposts': 3}
# {'id': '4200390871848376', 'text': '中国有哪些在外国人看来难以完成的事？ - 回答作者：「瞎说什么大实话」中国有哪些在外国人看来难以完成的事？（想看更多？下载 @知乎 App：知乎 ）', 'attitudes': 0, 'comments': 0, 'reposts': 0}
# {'id': '4200257564816468', 'text': 'JavaScript加密逻辑分析与Python模拟执行实现数据爬取JavaScript加密逻辑分析与Python模拟执行实现数据爬取', 'attitudes': 8, 'comments': 4, 'reposts': 3}
# {'id': '4198823863705401', 'text': 'TensorFlow Bi-LSTM实现文本分词网页链接', 'attitudes': 7, 'comments': 4, 'reposts': 1}
# {'id': '4198598377726018', 'text': '666', 'attitudes': 3, 'comments': 0, 'reposts': 0}
# {'id': '4198448586155364', 'text': '我第一眼居然看成了吴恩达//@有时右逝:吴承恩捉妖记。', 'attitudes': 2, 'comments': 2, 'reposts': 1}
# {'id': '4198446552510097', 'text': 'TensorFlow RNN Cell源码解析网页链接', 'attitudes': 4, 'comments': 3, 'reposts': 1}
# {'id': '4198132528833403', 'text': '跟繁琐的命令行说拜拜！Gerapy分布式爬虫管理框架来袭！跟繁琐的命令行说拜拜！Gerapy分布式爬虫管理框架来袭！', 'attitudes': 25, 'comments': 8, 'reposts': 77}
# {'id': '4197856074028588', 'text': '', 'attitudes': 0, 'comments': 0, 'reposts': 0}
# {'id': '4196266798040888', 'text': '实验效果不行无非是因为自己太菜了，继续努力吧，特么我就不信搞不出来！', 'attitudes': 9, 'comments': 5, 'reposts': 0}
# {'id': '4195145865490917', 'text': '棒极了！！！', 'attitudes': 5, 'comments': 1, 'reposts': 1}
# {'id': '4195119567034112', 'text': '//@回忆专用小马甲://@段子楼:hhhhhh//@糗事大百科://@黄濑濑濑濑: ？//@水晶男孩鸡大帅:别人的人生：———— 我的：-/\\—～v^v^_—//@夏正正:不是我不想向前……', 'attitudes': 4, 'comments': 0, 'reposts': 2}
# {'id': '4184886966921259', 'text': '特朗普亲自传授 Tensorflow Eager Execution 上海·长风新村街区', 'attitudes': 9, 'comments': 1, 'reposts': 0}
# {'id': '4184579579418282', 'text': '花天酒地 上海·长风新村街区', 'attitudes': 10, 'comments': 3, 'reposts': 0}
# {'id': '4184447412720422', 'text': 'GDD！ 上海·长风新村街区', 'attitudes': 13, 'comments': 3, 'reposts': 1}
# {'id': '4184062375580570', 'text': ': 我觉得这个芯挺好吃的，你要吃挞吗？这一刻的时光 北京·鼎好电子商城', 'attitudes': 6, 'comments': 16, 'reposts': 0}
# {'id': '4183368163235686', 'text': '由于12月9日我的博客由阿里云迁移至腾讯云并做了HTTPS升级，因为之前备案在阿里云，现在尚未接入在腾讯云的备案，所以现在网站HTTP服务无法访问，不过目前HTTPS是可以访问的，请在网站链接前面添加 https://，主页为 网页链接，我会尽快接入腾讯云的备案，在此给大家带来的不便还望谅解。', 'attitudes': 13, 'comments': 6, 'reposts': 0}
