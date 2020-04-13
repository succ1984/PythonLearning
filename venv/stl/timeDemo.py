#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import time
#由于Python的time模块实现主要调用C库，所以各个平台可能有所不同。
# time模块目前只支持到2038年前。如果需要处理范围之外的日期，请使用datetime模块。

now=time.localtime()
print(now)
#
print(time.strftime('%Y-%m-%d %H:%M:%S.%U'))

#time.sleep(t)，用来睡眠或者暂停程序t秒，t可以是浮点数或整数。
print("暂停程序5秒")
time.sleep(.55)
print("程序恢复")
#time.time(),返回当前系统时间戳。时间戳可以做算术运算
print(time.time())

def func():
    time.sleep(1.14)
    pass

t1 = time.time()
func()
t2 = time.time()
print("t2 - t1为：",t2-t1)

#
print( time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))