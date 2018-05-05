#  -*- coding:utf-8 -*-

####  Redis 测试

# from redis import StrictRedis 
# redis = StrictRedis(host='localhost', port=6379, password='')
# redis.set('name', 'Bod')
# print(redis.get('name'))

# b'Bod'      set()   get()  方法 正常

from redis import StrictRedis, ConnectionPool
pool = ConnectionPool(host='localhost', port=6379,db=0, password='')
redis = StrictRedis(connection_pool=pool)
redis.set('name', 'Bod')
print(redis.get('name'))

# b'Bod'
# 观察源码可以发现，StrictRedis内其实就是用host和port等参数又构造了一个ConnectionPool，
#  所以直接将ConnectionPool当作参数传给StrictRedis也一样

# ConnectionPool还支持通过URL来构建。URL的格式支持有如下3种

# redis://[:password]@host:port/db        Redis TCP连接
# rediss://[:password]@host:port/db       Redis TCP+SSL连接
# unix://[:password]@/path/to/socket.sock?db=db         Redis UNIX socket连接


from redis import StrictRedis, ConnectionPool 
url = 'redis://@localhost:6379/0'
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)
redis.set('age',12)
print(redis.get('age'))

# b'12'

# 首先，声明一个Redis连接字符串，然后调用from_url()方法创建ConnectionPool，
# 接着将其传给StrictRedis即可完成连接，所以使用URL的连接方式还是比较方便的
