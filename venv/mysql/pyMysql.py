#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import pymysql
import sys

#打开数据库连接
db=pymysql.connect(
    host="localhost",
    user="node",
    password="node",
    db="sakila",
    charset='utf8'
)
# 使用 cursor() 方法创建一个游标对象 cursor
cursor=db.cursor()
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("select VERSION()")
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
# print("Database version : %s " % data)
# # 关闭数据库连接
# db.close()

#插入数据


#删除数据
# sqldel='DELETE FROM users where userid=%s'
# cursor.execute(sqldel,(16,))
# db.commit()
# cursor.close()
# db.close()
# print("删除数据成功")
#查询数据
sqlSelect='select * from users where username like "小丽%"'
cursor.execute(sqlSelect)

data=cursor.fetchall()
for x in data:
    print(x)
cursor.close()
db.close()