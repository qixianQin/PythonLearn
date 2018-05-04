# -*- conding:utf-8 -*- 

###   MongoDB   链接测试
import pymongo
client	= pymongo.MongoClient(host='localhost', port=27017)
##   client = MongoClient('mongodb://localhost:27017/')
db = client['local']       #  指定数据库
# db = client.local         #  指定数据库
collection = db.students    # 指定集合
# collection = db['students'] #  指定集合

# student = {
# 	'id': '1000001',
# 	'name':'Simon',
# 	'age':21,
# 	'gender':'male'
# }

# result = collection.insert(student)
# print(result)

##   5aec7d608c9e131180bbcffd  （ObjectId）    成功插入数据库 
# 在MongoDB中，每条数据其实都有一个_id属性来唯一标识。如果没有显式指明该属性，
# MongoDB会自动产生一个ObjectId类型的_id属性。insert()方法会在执行后返回_id值



##  同时插入多条数据 

# student1 = {
# 	'id': '1000002',
# 	'name':'Simon1',
# 	'age':22,
# 	'gender':'male'
# }

# student2 = {
# 	'id': '1000003',
# 	'name':'Simon2',
# 	'age':33,
# 	'gender':'male'
# }

# result = collection.insert([student1, student2])
# print(result)


#  结果返回一个集合：[ObjectId('5aec7e5d8c9e132f90354a2e'), ObjectId('5aec7e5d8c9e132f90354a2f')]


## 在PyMongo 3.x版本中，官方已经不推荐使用insert()方法  
## 官方推荐使用insert_one()和insert_many()方法来分别插入单条记录和多条记录

# student3 = {
# 	'id': '1000004',
# 	'name':'Juize',
# 	'age':24,
# 	'gender':'male'
# }

# result = collection.insert_one(student3)
# print(type(result))
# print(result)
# print(result.inserted_id)     #返回的是InsertOneResult对象，我们可以调用其inserted_id属性获取_id

# <pymongo.results.InsertOneResult object at 0x000001CD6286EE48>
# 5aec7f948c9e1327e85e3982



# student1 = {
# 	'id': '1000002',
# 	'name':'Simon1',
# 	'age':22,
# 	'gender':'male'
# }

# student2 = {
# 	'id': '1000003',
# 	'name':'Simon2',
# 	'age':33,
# 	'gender':'male'
# }

# result = collection.insert_many([student1, student2])
# print(type(result))
# print(result)
# print(result.inserted_ids)


# <class 'pymongo.results.InsertManyResult'>
# <pymongo.results.InsertManyResult object at 0x000002AD23A5F0C8>
# [ObjectId('5aec80188c9e1328e07b6559'), ObjectId('5aec80188c9e1328e07b655a')]



###   查询  用find_one()或find()方法进行查询，其中find_one()查询得到的是单个结果，find()则返回一个生成器对象


result = collection.find_one({'name':'Simon'})     #  数据库中只有一个 名字为  Simon 的
print(type(result))
print(result)

# <class 'dict'>
# {'_id': ObjectId('5aec7d608c9e131180bbcffd'), 'id': '1000001', 'name': 'Simon', 'age': 21, 'gender': 'male'}


result = collection.find_one({'name':'Simon1'})    ##  有两条记录，但是也只会返回一个结果
print(type(result))
print(result)

# <class 'dict'>
# {'_id': ObjectId('5aec7e5d8c9e132f90354a2e'), 'id': '1000002', 'name': 'Simon1', 'age': 22, 'gender': 'male'}



##   可以根据ObjectId来查询，此时需要使用bson库里面的objectid

from bson.objectid import ObjectId 
result = collection.find_one({'_id':ObjectId('5aec80188c9e1328e07b6559')})
print(type(result))
print(result)

# <class 'dict'>
# {'_id': ObjectId('5aec80188c9e1328e07b6559'), 'id': '1000002', 'name': 'Simon1', 'age': 22, 'gender': 'male'}


###  查询多条记录的

result = collection.find({'age':24})
print(type(result))
print(result)

# <class 'pymongo.cursor.Cursor'>
# <pymongo.cursor.Cursor object at 0x00000257C1419CC0>

result = collection.find({'age':24})
print(type(result))    #  <class 'pymongo.cursor.Cursor'>
for res in result:
	print(res)

# <class 'pymongo.cursor.Cursor'>
# {'_id': ObjectId('5aec7f848c9e133f00b12609'), 'id': '1000004', 'name': 'Juize', 'age': 24, 'gender': 'male'}
# {'_id': ObjectId('5aec7f948c9e1327e85e3982'), 'id': '1000004', 'name': 'Juize', 'age': 24, 'gender': 'male'}
# {'_id': ObjectId('5aec80188c9e1328e07b6558'), 'id': '1000004', 'name': 'Juize', 'age': 24, 'gender': 'male'}



##  