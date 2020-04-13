#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#线程锁 学习demo ,即threading.Lock

import threading,os,sys,time,datetime

number=0
lock=threading.Lock()

def plus(lk):
    global number
    # with lk:
    #     for _ in range(0,1000000):
    #         number+=1
    # print("子线程%s运算结束后，number = %s" % (threading.current_thread().getName(), number))
    bGetLock= lk.acquire()
    if(bGetLock):
        print("获取锁成功")
    for _ in range(0,1000000):
        number+=1
    print("子线程%s运算结束后，number = %s" % (threading.current_thread().getName(), number))
    lk.release()

for i in range(2):      # 用2个子线程，就可以观察到脏数据
    t = threading.Thread(target=plus,args=(lock,))
    t.start()
    #t.join()#这样就变成单线程操作


time.sleep(2)       # 等待2秒，确保2个子线程都已经结束运算。
print("主线程执行完毕后，number = ", number)
