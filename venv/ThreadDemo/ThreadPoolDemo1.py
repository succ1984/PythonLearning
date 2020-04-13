#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#线程池 学习demo1

import queue
import time
import threading
import os,datetime

class MyThreadPool:
    def __init__(self,maxSize=5):
        self.maxSize=maxSize
        self.pool=queue.Queue(5)
        for _ in range(5):
            self.pool.put(threading.Thread)
    def getThread(self):
        return self.pool.get()
    def addThread(self):
        self.pool.put(threading.Thread)

def run(i,pool):
    print('执行任务',i)
    time.sleep(1)
    pool.addThread()
if __name__=='__main__':
    pool=MyThreadPool(5) # 设定线程池中最多只能有5个线程类
    for i in range(20):
        t=pool.getThread()
        oThread=t(target=run,args=(i,pool))
        oThread.start()
print("当前活动的子线程数为：",threading.active_count())



