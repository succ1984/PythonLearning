#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import os

#指示你正在使用的工作平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'。查看当前操作系统的名称
print("当前操作系统名称 %s" % os.name)

#当前平台的路径分隔符
print(os.sep)
#可替代的路径分隔符，在Windows中为‘/’。
print(os.altsep)
print("文件名和文件扩展名之间的分隔符为：%s" % os.extsep)
print("PATH环境变量中的分隔符 %s" % os.pathsep)
print("行结束符 %s " % os.linesep)
print("os.defpath %s " % os.defpath)
print("在不同的系统上null设备的路径 %s " % os.devnull)



'''
文件和目录操作
'''
newDirPath='E:/testdir'
subDirPath='E:/testdir/subdir'
listDirPath='E:\\测试文件'
print("获取当前工作目录，即当前python脚本工作的目录路径 %s" % os.getcwd())
#改变当前脚本工作目录；相当于shell下cd
cwdPath="E:/"
os.chdir(cwdPath)
print("获取当前工作目录，即当前python脚本工作的目录路径 %s" % os.getcwd())
#返回当前目录
print("返回当前目录 %s" % os.curdir)
#获取当前目录的父目录字符串名
print("获取当前目录的父目录字符串名 %s" % os.pardir)

#创建单级目录,当文件已存在时，无法创建该文件
#os.mkdir(newDirPath)
#创建多级目录
if(os.path.isdir(subDirPath)):
    os.removedirs(subDirPath)
os.makedirs(subDirPath)
#列出目录下文件
files=os.listdir(listDirPath)
for x in files:
    if os.path.isdir(x):
        print("目录：%s" % x)
    elif os.path.isfile(x):
       print("aa")
    else:
        pass
#重命名文件、目录
# os.renames("E:/testdirNew","E:/testdir")
#获取文件、目录信息
os.stat(newDirPath)
#	返回path规范化的绝对路径
print(os.path.abspath(newDirPath))
#将path分割成目录和文件名二元组返回
print(os.path.split(newDirPath))
#返回path的目录。其实就是os.path.split(path)的第一个元素
print(os.path.dirname(subDirPath))
#	返回path最后的文件名,如果path以／或\结尾，那么就会返回空值。
print(os.path.basename(subDirPath))
#如果path存在，返回True；如果path不存在，返回False
print(os.path.exists(subDirPath))
#如果path是绝对路径，返回True
print(os.path.isabs(subDirPath))
#如果path是一个存在的文件，返回True。否则返回False
print(os.path.isfile("E:/测试文件/ynzx-top.jpg"))
#如果path是一个存在的目录，则返回True。否则返回False
print(os.path.isdir(subDirPath))
#将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
joinPath=os.path.normpath(os.path.join("E:/","abc","def"))
print(joinPath)
if not os.path.exists(joinPath):
    os.makedirs(joinPath)
#	规范path字符串形式
print(os.path.normpath("E:/abc/def/cde"))
#返回文件 path 创建时间
print(os.path.getctime(joinPath))
#返回最近访问时间（浮点型秒数）
print(os.path.getatime(joinPath))
#返回最近文件修改时间
print(os.path.getmtime(joinPath))
#返回文件包含的字节数量
print(os.path.getsize("E:/测试文件/ynzx-top.jpg"))

#os.walk() 方法可以创建一个生成器，用以生成所要查找的目录及其子目录下的所有文件。
walkDir="E:/测试文件"
for root,dirs,files in os.walk(walkDir,topdown=True):
    print("根目录为："+root)
    for name in files:
        print("文件:"+os.path.normpath(os.path.join(root, name)))
    for name in dirs:
        print("目录："+os.path.normpath(os.path.join(root, name)))











