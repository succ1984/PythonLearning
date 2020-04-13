#!/usr/bin/env python 
# -*- coding:utf-8 -*-

'''
Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数
itertools 是python的迭代器模块，itertools提供的工具相当高效且节省内存。
使用这些工具，你将能够创建自己定制的迭代器用于高效率的循环。
'''

import itertools
from itertools import count
import time


#count
for i in  count(10):
    if(i>20):
        break
    else:
        print(i)
    time.sleep(.1)

#cycle
iterCycle=itertools.cycle(['a','b','c','d','e'])
nCount=5
for item in iterCycle:
    print(item)
    time.sleep(.1)
    nCount-=1
    if(nCount<=0):
        break

#repeat,repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：

iterRepeat=itertools.repeat('abc',5)
for i in iterRepeat:
    print(i)
    time.sleep(.1)

#takewhile
iterTakeWhile=itertools.takewhile(lambda x:(x<10),itertools.count(1,1))
for x in iterTakeWhile:
    print(x)
    time.sleep(.5)

#chain
for x in itertools.chain('abc','def'):
    print(x)

#group

for x in itertools.groupby('abcdefeffffabc'):
    print(x)





