#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#生产者、消费者模式学习

import time
import threading
import queue
import os

q = queue.Queue(10)     # 生成一个队列，用来保存“包子”，最大数量为10
def productor(i):
    while True:
        q.put("厨师 %s 做的包子" %i)
        time.sleep(2)
def consumer(j):
    while True:
        print("顾客%s吃了一个%s" %(j,q.get()),end='\n')

        time.sleep(1)

for i in range(30):
    t=threading.Thread(target=productor,args=(i,))
    t.start()
for i in range(10):
    t=threading.Thread(target=consumer,args=(i,))
    t.start()