#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#Python 异常处理 学习Demo

while True:
    try:
        x = int(input("请输入一个数字: "))
        break
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！")