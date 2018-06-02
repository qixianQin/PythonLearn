使用 Scrapy  爬取知乎网 

创建Scrapy 项目： 
D:\GitHub\PythonLearn>scrapy startproject zhihuspider  

进入项目所在目录之后，  只用命令行：  scrapy startproject 项目名  可以自动创建项目
创建后文件说明：

zhihuspider/
	     zhihuspider/         项目的python模块
		 	_pycache_/
		 	spiders/           放置spider代码的目录
		 			_pycache_/
		 			_init_.py
		 	_init_.py
		 	items.py            项目中的itemw文件
		 	middlewares.py     
		 	pipelines.py         项目中的pipelines 文件
		 	setting.py           项目的设置文件
		 scrapy.cfg     项目配置文件



最后可以通过命令：  scrapy crawl 项目中的名字  来运行