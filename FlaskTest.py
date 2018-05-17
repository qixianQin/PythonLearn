# -*- coding:utf-8 -*- 

##   利用Flask来写一个简单的Web应用

# from flask import Flask   # 导入 flask

## Flask需要一个参数，这个参数通常是主模块或是包的名字。所以通常会传入 __name__
## Flask用这个参数来决定程序的根目录，以便以后找到资源文件，比如网页中的图片，视频，音频等
# app = Flask(__name__)   ##  创建一个应用

##  可以通过使用app.config类来修改配置，开启调试模式  
# app.config['DEBUG'] = True    ##  配置较少的时候，可以直接在这里配置

## 使用app.route()装饰器会将URL和执行的视图函数(函数 index )的关系保存在app.url_map属性上。当你访问指定的URL时，
## 就会调用这个函数。当遇到第一个return时，就会结束。其中的return就是你的response
# @app.route('/')   ##  定义路由（View）, 可以理解为定义页面的URL
# def index():
# 	return "This is using Python and Flask make it."    ##  渲染页面

## 执行app.run来启动服务器。默认的Flask会监听的地址是127.0.0.1:5000。我们指定host和port参数，
# 就修改了监听地址。 服务启动后，会先判断参数host以及port是否为None，如果为None，
# 就会将host和port修改为默认值。然后会判断debug。然后就会调用werkzeug.serving.run_simple
# 来启动Web服务，默认会使用单进程的werkzeug.serving_BaseWSGIServer来处理客户端的请求
# if __name__ == '__main__':
# 	app.run(host='127.0.0.1', port=8080)    ##  debug 参数：  开启debug 模式，可以修改不用停止程序





# from flask import Flask, render_template    #   新导入了一个 render_template 函数 

# #  在 Flask(__name__) 修改代码为 Flask(__name__,template_folder=”存放模板文件夹名称”)
# app = Flask(__name__)
# app.config['DEBUG'] = True

#  # 调用render_template，传入的第一个参数是模板的文件名称，它会在主程序的同级目录下去寻找一个名为
#  # templates的文件夹，在这个文件下去寻找模板。第二个传入的参数，会在模板中显示，html代码中有
#   # {{ name }} 这样的一个写法。这里的 name就是你在主程序中传入的参数

# @app.route('/')
# def index():
# 	return render_template("index.html", name="Stronger")

# if __name__ == '__main__':
# 	app.run(host='127.0.0.1', port=8080)


# from flask import Flask, url_for

# app = Flask(__name__)
# app.config['DEBUG'] = True

# @app.route('/user/')
# def index():
# 	print(url_for('index', id=10, name='Test', age=18))
# 	return 'Test'

# if __name__ == '__main__':
# 	app.run(host='127.0.0.1', port=8080)


# from flask import Flask,url_for,redirect
 
# app = Flask(__name__)
 
# @app.route('/')
# def index():
#     return redirect(url_for('user'))
 
# @app.route('/user/')
# def user():
#     return 'This is User'
 
# if __name__ == '__main__':
#     app.run(host='127.0.0.1',debug=True)




# from flask import Flask, request

# app = Flask(__name__)
# app.config["DEBUG"] = True    ###   第一种方式
# # app.config.update(DEBUG=True)

# @app.route('/', methods=['GET'])
# def index():
# 	# name = request.args.get('name')
# 	# age = request.args.get('age')
# 	# print('name: %s  \nage: %s' % (name, age))
# 	return 'OK'


# if __name__ == '__main__':
# 	app.run(host='127.0.0.1', port=8080)


### 开启debug模式的方式
###  1、  在 app.run（）  方法中添加  debug=True 参数
###  2、 app.config['DEBUG'] = True
###  3、 app.config.update(DEBUG=True)
###  4、引入对象  ： 在 config.py中 新增一个类  Main_Config
### 5、引用  配置文件

from flask import Flask
from config import Main_Config

app = Flask(__name__)
# app.config['DEBUG'] = True
# app.config.update(DEBUG=True)
# app.config.from_object(Main_Config) 
app.config.from_pyfile("config.conf", silent=True)    # config.conf 为文件名， 
##   silent =True , 当文件不存在的时候，不报错， 只返回False

@app.route('/')
def index():
	return 'ok!!!!dddaaaa'

if __name__ == '__main__':
	app.run()
	# app.run(debug=True)