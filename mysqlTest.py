# -*- coding:utf-8 -*-


###  使用PyMySQL操作MySQL数据库的方法

import pymysql 
db = pymysql.connect(host='localhost', user='root', password='', port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database.version:', data)
cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')    ###  创建一个数据库 spiderrs
cursor.close()


# Database.version: ('5.6.30',)


# PyMySQL的connect()方法声明一个MySQL连接对象db，此时需要传入MySQL运行的host（即IP）
# 参数user即用户名，password即密码，port即端口（默认为3306）
# 连接成功后，需要再调用cursor()方法获得MySQL的操作游标，利用游标来执行SQL语句


###  创建表  students

# import pymysql 
# db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='spiders')
# cursor = db.cursor()
# sql = "CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))"
# cursor.execute(sql)
# db.close()

###  pymysql.connect(host, user, password, port, db)  
###  db 指定连接的数据库



import pymysql 
id = '1000004'
name = 'Bod'
age = 44

db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO students(id, name , age) values(%s, %s, %s)'
try:
	cursor.execute(sql, (id, name, age))
	db.commit()
except Exception as e:
	db.rollback()
db.close()


###  成功插入数据


import pymysql
db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='spiders')
cursor = db.cursor()
data = {
	'id':'1000002',
	'name':'Bod',
	'age':20
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) values ({values})'.format(table=table,keys=keys,values=values)
try:
	if cursor.execute(sql, tuple(data.values())):
		print('Successful!')
		db.commit()
except Exception as e:
	print('Failed!')
	db.rollback()
db.close()


# Successful!

#  ', '.join(data.keys())的结果就是id, name, age



###  更新数据 

import pymysql
db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='spiders')
cursor = db.cursor()
sql = 'UPDATE students set age = %s WHERE id = %s'	
try:
	cursor.execute(sql, (33, '1000001'))
	db.commit()
except Exception as e:
	db.rollback()
db.close()


##  更新成功


import pymysql 
db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='spiders')
cursor = db.cursor()

data = {
      'id':'1000001',
      'name':'Bod',
      'age':44
}

table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))

sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
update = ','.join([" {key} = %s".format(key=key) for key in data])
sql += update
try:
	print(sql)
	if cursor.execute(sql, tuple(data.values())*2):
		print('Successful')
		db.commit()
except Exception as e:
	print(e)
	print('Failed')
	db.rollback()
db.close()


####    写SQL 一定要注意 空格，  
# INSERT INTO students(id,name,age) VALUES (%s,%s,%s) ON DUPLICATE KEY UPDATE id = %s, name = %s, age = %s


####删除数据  

import pymysql 
db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='spiders')
cursor = db.cursor()

table = 'students'
condition = 'age > 20'
sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
try:
	cursor.execute(sql)
	db.commit()
	print('Successful')
except Exception as e:
	db.rollback()
	print('Failed')
db.close()

# Successful   成功删除数据




####   查询数据 

import pymysql 
db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='spiders')
cursor = db.cursor()

sql = 'SELECT * FROM students WHERE age >= 20'
# sql = 'SELECT VERSION()'
try:
	cursor.execute(sql)
	print('Count:', cursor.rowcount)
	one = cursor.fetchone()
	print('one:', one)
	results = cursor.fetchall()
	print('Result:', results)
	print('Result Type:', type(results))
	for row in results:
		print(row)
except Exception as e:
	print(e)
	print('Error')


# Count: 4
# one: ('1000001', 'Bod', 21)
# Result: (('1000002', 'Bod', 20), ('1000003', 'Bod', 33), ('1000004', 'Bod', 44))
# Result Type: <class 'tuple'>
# ('1000002', 'Bod', 20)
# ('1000003', 'Bod', 33)
# ('1000004', 'Bod', 44)



import pymysql 
db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='spiders')
cursor = db.cursor()

sql = 'SELECT * FROM students WHERE age >= 20'
try:
	cursor.execute(sql)
	print('Count:', cursor.rowcount)
	row = cursor.fetchone()
	while row:
		print("Row:", row)
		row = cursor.fetchone()
except Exception as e:
	print(e)
	print('Error')	


# Count: 4
# Row: ('1000001', 'Bod', 21)
# Row: ('1000002', 'Bod', 20)
# Row: ('1000003', 'Bod', 33)
# Row: ('1000004', 'Bod', 44)