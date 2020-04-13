#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import subprocess

#subprocess.run() 方法
ret=subprocess.run("dir E:\\",shell=True,stdout=subprocess.PIPE)
print(ret)
print(ret.stdout.decode("gbk"))
ret1=subprocess.run("ipconfig",shell=True,stdout=subprocess.PIPE)
print(ret1)
print(ret1.stdout.decode("gbk"))

#subprocess.Popen()方法
result=subprocess.Popen("python",stdout=subprocess.PIPE,stdin=subprocess.PIPE,shell=True)
result.stdin.write(b"import os\n")
result.stdin.write(b"print(os.getcwd())")
result.stdin.close()
out=result.stdout.read().decode("gbk")
result.stdout.close()
print(out)
