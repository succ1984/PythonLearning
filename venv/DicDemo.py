#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#字典数据结构学习Demo ,字典是另一种可变容器模型，且可存储任意类型对象。键必须是唯一的，但值则不必。
#值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。

d1={'name':'succ','age':36}
print(d1['name'])

d1['name']='sushee'  #更新元素信息
print(d1)
d1['school']='nyist' #向字典添加信息
d1['class']=2003
print(d1)
del d1['class'] #删除字典元素
print(d1)
d2=d1.copy()
del d1    #删除整个字典
print(d2)
d3=d2.copy()
d2.clear()   #清空字典，清空后字典长度为0
print(d2)
print(len(d2))
print(d3)

#Python 字典 fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。
#dict.fromkeys(seq[, value])
seq=(1,2,3)
dic1=dict.fromkeys(seq,'abc')
print(dic1)
#Python 字典 get() 函数返回指定键的值，如果值不在字典中返回默认值。 字典查找方法
print(d3.get('name'))
print(d3.get('name1','none'))

#Python 字典 items() 方法以列表返回可遍历的(键, 值) 元组数组。
for k,v in d3.items():
    print("key:",k)
    print("value:",v)

print(list(d3.keys()))
print(list(d3.values()))
#Python 字典 setdefault() 方法和 get()方法 类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值。
dict.setdefault(d3,'number','001')
print(d3)
#Python 字典 update() 函数把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里。
d3.update({'abc':'123'})
print(d3)
#pop(key[,default]),删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
popValue=d3.pop('abc','001')
print(popValue)
#Python 字典 popitem() 方法随机返回并删除字典中的最后一对键和值。
#如果字典已经为空，却调用了此方法，就报出KeyError异常。
print(d3.popitem())





    









