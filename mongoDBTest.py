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



##  查询年龄大于 24的

result = collection.find({'age':{'$gt':24}})
print(type(result))
for res in result:
	print(res)

# <class 'pymongo.cursor.Cursor'>
# {'_id': ObjectId('5aec7e5d8c9e132f90354a2f'), 'id': '1000003', 'name': 'Simon2', 'age': 33, 'gender': 'male'}
# {'_id': ObjectId('5aec80188c9e1328e07b655a'), 'id': '1000003', 'name': 'Simon2', 'age': 33, 'gender': 'male'}


###   正则表达式  匹配查询 
result = collection.find({'name':{'$regex':'^S.*'}})
print("Regex:", type(result))
for res in result:
	print(res)

# Regex: <class 'pymongo.cursor.Cursor'>
# {'_id': ObjectId('5aec7d608c9e131180bbcffd'), 'id': '1000001', 'name': 'Simon', 'age': 21, 'gender': 'male'}
# {'_id': ObjectId('5aec7e5d8c9e132f90354a2e'), 'id': '1000002', 'name': 'Simon1', 'age': 22, 'gender': 'male'}
# {'_id': ObjectId('5aec7e5d8c9e132f90354a2f'), 'id': '1000003', 'name': 'Simon2', 'age': 33, 'gender': 'male'}
# {'_id': ObjectId('5aec80188c9e1328e07b6559'), 'id': '1000002', 'name': 'Simon1', 'age': 22, 'gender': 'male'}
# {'_id': ObjectId('5aec80188c9e1328e07b655a'), 'id': '1000003', 'name': 'Simon2', 'age': 33, 'gender': 'male'}



####     计数

##   统计所有的记录 
count = collection.find().count()
print("Count:", count)

#   Count: 8

##  统计符合某个条件的记录

count = collection.find({'age':24}).count()
print("Count:", count)

# Count: 3


####     排序

# 升序： pymongo.ASCENDING     降序：  pymongo.DESCENDING

results = collection.find().sort('name', pymongo.ASCENDING)
print("Sort ASC name:", [result['name'] for result in results]) 


# Sort name: ['Juize', 'Juize', 'Juize', 'Simon', 'Simon1', 'Simon1', 'Simon2', 'Simon2']

# 降序
results = collection.find().sort('name', pymongo.DESCENDING)
print("Sort DESC name:", [result['name'] for result in results]) 

# Sort DESC name: ['Simon2', 'Simon2', 'Simon1', 'Simon1', 'Simon', 'Juize', 'Juize', 'Juize']

##  默认做升序排序
results = collection.find().sort('name')
print("Sort default name:", [result['name'] for result in results]) 

# Sort default name: ['Juize', 'Juize', 'Juize', 'Simon', 'Simon1', 'Simon1', 'Simon2', 'Simon2']


####    偏移 skip（）     偏移2， 忽略前面两个， 从第三个开始输出
results = collection.find().sort('name').skip(2)
print("skip 2:", [result['name'] for result in results])

# skip 2: ['Juize', 'Simon', 'Simon1', 'Simon1', 'Simon2', 'Simon2']

##  不用排序也可以
results = collection.find().skip(2)
print("2skip 2:", [result['name'] for result in results])

# 2skip 2: ['Simon2', 'Juize', 'Juize', 'Juize', 'Simon1', 'Simon2']

##  在偏移2 的结果上， 使用 limit(2) 即只要结果中的2个
results = collection.find().skip(2).limit(2)
print("limit 2:", [result['name'] for result in results])

# limit 2: ['Simon2', 'Juize']


# 在数据库数量非常庞大的时候，如千万、亿级别，
# 最好不要使用大的偏移量来查询数据，因为这样很可能导致内存溢出

###   当数据量非常巨大的时候，可以使用下面的方法，但是需要记录上一次查询的_id

from bson.objectid import ObjectId 
results = collection.find({'_id':{'$gt':ObjectId('5aec7f848c9e133f00b12609')}})
for res in results:
	print("Big data query:",res)

# Big data query: {'_id': ObjectId('5aec7f948c9e1327e85e3982'), 'id': '1000004', 'name': 'Juize', 'age': 24, 'gender': 'male'}
# Big data query: {'_id': ObjectId('5aec80188c9e1328e07b6558'), 'id': '1000004', 'name': 'Juize', 'age': 24, 'gender': 'male'}
# Big data query: {'_id': ObjectId('5aec80188c9e1328e07b6559'), 'id': '1000002', 'name': 'Simon1', 'age': 22, 'gender': 'male'}
# Big data query: {'_id': ObjectId('5aec80188c9e1328e07b655a'), 'id': '1000003', 'name': 'Simon2', 'age': 33, 'gender': 'male'}



####   更新数据   update()

condition = {'name':'Simon1'}
student4 = collection.find_one(condition)
student4['age'] = 44
result = collection.update(condition, student4)
print(type(result))
print("update: ", result)

# 首先指定查询条件，然后将数据查询出来，修改年龄后调用update()方法将原条件和
# 修改后的数据传入

# <class 'dict'>
# update:  {'n': 1, 'nModified': 1, 'ok': 1.0, 'updatedExisting': True}
# ok代表执行成功，nModified代表影响的数据条数


# 也可以使用$set操作符对数据进行更新
condition = {'name':'Simon1'}
student4 = collection.find_one(condition)
student4['age'] = 54
result = collection.update(condition, {'$set':student4})
print(type(result))
print("update $set: ", result)


# <class 'dict'>
# update $set:  {'n': 1, 'nModified': 1, 'ok': 1.0, 'updatedExisting': True}

# 这样可以只更新student字典内存在的字段。如果原先还有其他字段，则不会更新，也不会删除。
# 而如果不用$set的话，则会把之前的数据全部用student字典替换；如果原本存在其他字段，
# 则会被删除

# update()方法其实也是官方不推荐使用的方法。这里也分为update_one()方法和update_many()方法，
# 用法更加严格，它们的第二个参数需要使用$类型操作符作为字典的键名

condition = {'name':'Simon1'}
student4 = collection.find_one(condition)
student4['age'] = 64
result = collection.update_one(condition, {'$set':student4})
print(type(result))
print("update_one $set: ", result)
print(result.matched_count, result.modified_count)

# 调用了update_one()方法，第二个参数不能再直接传入修改后的字典，而是需要使用
# {'$set': student}这样的形式，其返回结果是UpdateResult类型。
# 然后分别调用matched_count和modified_count属性，可以获得匹配的数据条数和影响的数据条数。

# <class 'pymongo.results.UpdateResult'>
# update_one $set:  <pymongo.results.UpdateResult object at 0x00000254B0F15748>
# 1 1


condition = {'age': {'$gt': 24}}
result = collection.update_one(condition, {'$inc':{'age':1}})
print(type(result))
print(result)
print(result.matched_count, result.modified_count)

# 指定查询条件为年龄大于24，然后更新条件为{'$inc': {'age': 1}}，也就是年龄加1，
# 执行之后会将第一条符合条件的数据年龄加1

# <class 'pymongo.results.UpdateResult'>
# <pymongo.results.UpdateResult object at 0x00000198CB691888>
# 1 1

condition = {'age': {'$gt': 24}}
result = collection.update_many(condition, {'$inc':{'age':1}})
print(type(result))
print(result)
print(result.matched_count, result.modified_count)

#  update_many 更新多条数据

# <class 'pymongo.results.UpdateResult'>
# <pymongo.results.UpdateResult object at 0x00000169F56157C8>
# 3 3


###  删除  remove()

result = collection.remove({'name':'Simon1'})
print(type(result))
print("remove: ",result)

# <class 'dict'>
# remove:  {'n': 1, 'ok': 1.0}

# 推荐方法——delete_one()和delete_many()

result = collection.remove_one({'name':'Simon1'})
print(result)
pirnt("remove_one:",result.delected_count)

result = collection.remove_many({'age':{'$lt':23}})
print(result)
print("remove_many:", result.delected_count)

# delete_one()即删除第一条符合条件的数据，delete_many()即删除所有符合条件的数据。
# 它们的返回结果都是DeleteResult类型，可以调用deleted_count属性获取删除的数据条数


# PyMongo还提供了一些组合方法，如find_one_and_delete()、find_one_and_replace()和
# find_one_and_update()，它们是查找后删除、替换和更新操作，其用法与上述方法基本一致
# 还可以对索引进行操作，相关方法有create_index()、create_indexes()和drop_index()等