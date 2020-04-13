#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import fileinput

with fileinput.input(r"E:\测试文件\test1.txt",mode="rU") as f:
    for line in f:
        line=line.rstrip()
        num=f.lineno()
        print("#%d\t%s" % (num,line))

