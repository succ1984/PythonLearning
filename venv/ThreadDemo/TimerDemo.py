#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#定时器对象 学习

import  os,sys,time,datetime,threading

def printSayHi(words):
    global  t
    print("当前时间："+datetime.datetime.now().isoformat())
    t = threading.Timer(1, printSayHi, args=('world',))
    t.start()

t=threading.Timer(1,printSayHi,args=('world',))
t.start()
