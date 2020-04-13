#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
import zipfile

oZipFile=zipfile.ZipFile(r"E:\测试文件\测试文件.zip")

oInfo=oZipFile.getinfo("small_guochan.jpg")
print(oInfo)

listInfo=oZipFile.infolist()
print(listInfo)

listName=oZipFile.namelist()
print(listName)

# f=oZipFile.open("small_guochan.jpg")
# ret=f.read()
# print(ret)

oZipFile.extract("small_nianjian.jpg","E:\\测试文件\\testzip")#解压单个
oZipFile.extractall("E:\\测试文件\\testzip")#解压多个

oZipFile.close()



