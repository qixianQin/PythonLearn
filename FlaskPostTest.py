# -*- conding:utf-8 -*- 

###   使用  POST 方法获取数据

# from flask import Flask, request, render_template

# app = Flask(__name__)

# @app.route('/get/', methods=['GET', 'POST'])
# def index():
# 	if request.method == 'GET':
# 		return render_template('index2.html')
# 	if request.method == 'POST':
# 		name = request.form.get('name')
# 		age = request.form.get('age')
# 		print('POST method: \n name: %s \n age: %s' % (name, age))
# 		return 'get detail!'

# if __name__ == '__main__':
# 	app.run(host='127.0.0.1', port=8080, debug=True)

from flask import Flask, request, render_template, redirect,url_for
import time

app =  Flask(__name__)

users = []

@app.route('/say/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('index3.html', says=users)
	else :
		title = request.form.get('say_title')
		text = request.form.get('say')
		user = request.form.get('say_user')
		date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

		users.append({"title":title, "text":text, 'user':user, 'date':date})
		return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)