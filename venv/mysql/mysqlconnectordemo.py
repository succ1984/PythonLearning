#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="node",
    password="node",
    database="sakila"
)
print(mydb)

#创建数据库
mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE usertest")
#显示数据库
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)

#插入单条记录
# sql='INSERT INTO users(usernumber,username,sex,mobile) VALUES (%s,%s,%s,%s)'
# val=('8','小丽',2,'13436300386')
# mycursor.execute(sql,val)
# mydb.commit()    # 数据表内容有更新，必须使用到该语句
# print(mycursor.rowcount, "记录插入成功。")

#插入多条记录
# sql='INSERT INTO users(usernumber,username,sex,mobile) VALUES (%s,%s,%s,%s)'
# val=[
#      ('9','小丽2',2,'13436300387'),
#      ('109','小丽3',2,'13436300388')
#     ]
# mycursor.executemany(sql,val)
# mydb.commit()    # 数据表内容有更新，必须使用到该语句
# print(mycursor.rowcount, "记录插入成功。")
#更新记录
# sql='UPDATE users SET usernumber="10" WHERE userid=12'
#
# mycursor.execute(sql)
# mydb.commit()    # 数据表内容有更新，必须使用到该语句
# print(mycursor.rowcount, "记录更新成功。")

#查询记录
# sql='SELECT * FROM users where 1=1 limit 0,5'
#
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# #myresult=mycursor.fetchone()
# for x in myresult:
#     print(x)

#删除数据
sql='DELETE FROM users where 1=1 and userid=%s'
val=(8,)
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount, "条记录删除 ")