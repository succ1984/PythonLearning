#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#自定义线程类

import threading
import os,sys,random,time,datetime

class MyThreading(threading.Thread):
    def __init__(self,func,args):
        super(MyThreading,self).__init__()
        self.func=func
        self.args=args
    def run(self):
        self.func(self.args)
def my_func(args):
    """
    你可以把任何你想让线程做的事定义在这里
    """
    print("This is a custom threading class demo...")
    print(f"args:{args}")
    time.sleep(5)
    print("The end")

obj = MyThreading(my_func, 123)
obj.start()

