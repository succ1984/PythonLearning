#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#getpass模块只能用于命令行界面！^_^

import getpass

pwd=getpass.getpass("请输入密码：")
print("密码输入成功！")
print("你的密码是：%s" % pwd)