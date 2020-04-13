#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#队列学习demo

import os,sys,datetime,queue

q=queue.Queue(5)
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
# print(q.get(block=True,timeout=5))
print(q.maxsize)
print(q.empty())
print(q.full())

q1=queue.PriorityQueue(3)
q1.put((2,"111"))
q1.put((1,"2222"))
q1.put((3,'3333'))
print(q1.get())
print(q1.get())
print(q1.get())

q2=queue.LifoQueue(3)
q2.put("3")
q2.put("2")
q2.put("1")
print(q2.get())
print(q2.get())
print(q2.get())