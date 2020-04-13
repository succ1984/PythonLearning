#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#元组学习demo
tuple1=(1,2,3)
print(tuple1)
tuple2=('a','b',['hi','hello'])
print(tuple2)
tupleEmpty=()
print(tupleEmpty)
tupleOneEle=('oneElement',)
print(tupleOneEle)
print(tuple1[2])
print(tuple1+tuple2)
del tuple1
#print(tuple1)

for x in tuple2:
    print(x)