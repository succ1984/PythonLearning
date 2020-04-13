#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#Python 函数学习Demo

def helloFunc(name):
    print('hello',name)
helloFunc('sushee')

#
def area(width,height):
    return width*height
a=area(5,4)
print('area is',a)

#python 传不可变对象实例
def ChangeInt(a):
    a = 10
b = 2
ChangeInt(b)
print(b)  # 结果是 2
#传可变对象实例
mylist = [10,20,30]
def changeList(mylist):
    mylist.append([1,2,3,4])
    print("函数内取值: ", mylist)
    return
changeList( mylist )
print ("函数外取值: ", mylist)
#命名参数
def printInfo(name,age):
    print("name:",name)
    print("age:",age)
printInfo(age=36,name='succ')
#默认参数
def printMe(name,age=36):
    print("name is ",name)
    print("age is ",age)
printMe("shshee")

#不定长参数         加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。如果单独出现星号 * 后的参数必须用关键字传入。
#加了两个星号 ** 的参数会以字典的形式导入。
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)


# 调用printinfo 函数
printinfo(70, 60, 50)


def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)


# 调用printinfo 函数
printinfo(1, a=2, b=3)

#匿名函数
sum = lambda arg1, arg2: arg1 + arg2
print(sum(1,2))

#return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。
# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total


# 调用sum函数
total = sum(10, 20)
print("函数外 : ", total)

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]
print(freshfruit)


# 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)

printinfo('succ',1,2,3,4)

#加了两个星号 ** 的参数会以字典的形式导入。
def printinfo( arg1, **vardict ):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)
printinfo(1, a=2,b=3)




    




