#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#内建模块 collection 学习Demo

from collections import namedtuple
from collections import deque
from collections import defaultdict
from _collections import OrderedDict
from collections import Counter


#声明一个命名元组类
point=namedtuple("Point",['x','y'])
#创建“类”的实例
p=point(1,2)
print(p.x)
print(p.y)

#验证类型
print(isinstance(p,point))
print(isinstance(p,tuple))
## namedtuple('名称', [属性list]):
Circle = namedtuple('Circle', ['x', 'y', 'r'])

#deque
q=deque([1,2,3])
q.append('a')
q.append('abc')
q.appendleft('first')
oFirst=q.pop()
print(oFirst)

#defaultdict
d=defaultdict(lambda:None)
d['key1']='abc'
print(d['key1'])
print(d['key2'])
#orderdict
od=OrderedDict([('b',1),('a',2),('c',3)])
print(od)
print(od.keys())

#Counter
c=Counter()
for ch in "programming":
    c[ch]=c[ch]+1
print(c)
print(c.elements())
print(c.most_common(3))
print(sum(c.values()))

c1=Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})
print(c1)
