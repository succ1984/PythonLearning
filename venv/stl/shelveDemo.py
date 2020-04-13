#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import shelve

filename='E:\\测试文件\\shelvetest.txt'
d = shelve.open(filename)
d["one"]="hello world!!!"
d["two"]="hi baby"
d["three"]="hi sushee"

klist=list(d.keys())
for x in klist:
    print(f"{x}:{d[x]}")
d.close()


