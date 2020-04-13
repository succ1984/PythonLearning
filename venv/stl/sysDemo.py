#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#内置模块sys的用法,sys模块主要是针对与Python解释器相关的变量和方法，不是主机操作系统。

import sys
from sys import stdin
from sys import stdout
from sys import stderr
from tqdm import tqdm  #进度条模块
import time

#获取命令行参数列表，第一个元素是程序本身
print(sys.argv)
#退出Python程序，exit(0)表示正常退出。当参数非0时，会引发一个SystemExit异常，可以在程序中捕获该异常
# sys.exit(0)
#获取Python解释程器的版本信息
print(sys.version)
#最大的Int值，64位平台是2**63 - 1
print(sys.maxsize)
#返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
print(sys.path)
#返回操作系统平台名称
print(sys.platform)
#输入相关
print(sys.stdin)
#	输出相关
print(sys.stdout)
#错误相关
print(sys.stderr)

#stdin
# print("what is your name?")
# name=stdin.readline()
# print("Your name is %s " % name)
#stdout
# for i in tqdm(range(100)):
#     time.sleep(.1)
# for i in range(100):
#     a = (i + 1) / 5
#     b = 20 - a
#     # sys.stdout.write('\r>>convert image %d/%d'%(i,b))
#
#     sys.stdout.write('\r|%s%s|%d%%' % (a * '▇', b * ' ', i + 1))
#     sys.stdout.flush()
#     time.sleep(.1)

#返回异常信息三元元组
print(sys.exc_info())
#获取系统当前编码，默认为utf-8
print(sys.getdefaultencoding())
#获取文件系统使用编码方式，默认是utf-8
print(sys.getfilesystemencoding())
#以字典的形式返回所有当前Python环境中已经导入的模块
# print(sys.modules)
#	返回一个列表，包含所有已经编译到Python解释器里的模块的名字
print(sys.builtin_module_names)
#当前Python的版权信息
print(sys.copyright)

#返回对象的大小
listPersons=["a","b","c"]
print(sys.getsizeof(listPersons))
#返回线程切换时间间隔，默认0.005秒
print(sys.getswitchinterval())
#设置线程切换的时间间隔，单位秒
sys.setswitchinterval(1)
print(sys.getswitchinterval())
#返回当前windwos系统的版本信息
print(sys.getwindowsversion())
#返回Python默认的哈希方法的参数
print(sys.hash_info)
#当前正在运行的Python解释器的具体实现，比如CPython
print(sys.implementation)
#当前线程信息
print(sys.thread_info)

#进度条功能
def bar(num, total):
    rate = num / total
    rate_num = int(rate * 100)
    r = '\r[%s%s]%d%%' % ("="*num, " "*(100-num), rate_num, )
    sys.stdout.write(r)
    sys.stdout.flush()


if __name__ == '__main__':
    for i in range(0, 101):
        time.sleep(0.1)
        bar(i, 100)