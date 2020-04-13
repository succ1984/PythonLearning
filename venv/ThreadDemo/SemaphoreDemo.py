#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#信号量学习

import threading,time,os

oSemaphoe=threading.Semaphore(value=3)

def thread_semaphore(index):
    # 信号量计数器减1
    oSemaphoe.acquire()
    time.sleep(2)
    print('thread_%s is running...' % index+os.linesep)
    # 信号量计数器加1
    oSemaphoe.release()

def main():
    # 虽然会有9个线程运行，但是通过信号量控制同时只能有3个线程运行
    # 第4个线程启动时，调用acquire发现计数器为0了，所以就会阻塞等待计数器大于0的时候
    for index in range(9):
       t= threading.Thread(target=thread_semaphore, args=(index,))
       t.start()

main()