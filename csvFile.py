# -*- conding:utf-8 -*- 

###   CSV文件存储  

### 写入
import csv 
with open('data.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['id', 'name', 'age'])
	writer.writerow(['10001', 'Mike', 20])
	writer.writerow(['10002', 'Bod', 22])
	writer.writerow(['10003', 'Jordan', 23])

# id,name,age

# 10001,Mike,20

# 10002,Bod,22

# 10003,Jordan,23

# 首先，打开data.csv文件，然后指定打开的模式为w（即写入），获得文件句柄，
# 随后调用csv库的writer()方法初始化写入对象，传入该句柄，
# 然后调用writerow()方法传入每行的数据即可完成写入


import csv 
with open('data.csv', 'a+') as csvfile:
	writer = csv.writer(csvfile, delimiter='\t')
	writer.writerow(['id', 'name', 'age'])
	writer.writerow(['10001', 'Mike', 20])
	writer.writerow(['10002', 'Bod', 22])
	writer.writerow(['10003', 'Jordan', 23])

# id	name	age

# 10001	Mike	20

# 10002	Bod	22

# 10003	Jordan	23


import csv 
with open('data.csv', 'a+') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['id', 'name', 'age'])
	writer.writerows([['10001','Mike',22],['10002','BOd',23],['10003','Jordan', 33]])

# id,name,age

# 10001,Mike,22

# 10002,BOd,23

# 10003,Jordan,33

import csv 
with open('data.csv', 'a+') as csvfile:
	fieldnames = ['id', 'name', 'age']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	writer.writerow({'id':'10001','name':'Mike','age':12})
	writer.writerow({'id':'10002','name':'Bod', 'age':12})
	writer.writerow({'id':'10003','name':'Jordan','age':12})

# id,name,age

# 10001,Mike,12

# 10002,Bod,12

# 10003,Jordan,12

