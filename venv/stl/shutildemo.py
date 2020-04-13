#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#shutil模块是对os模块的补充，主要针对文件的拷贝、删除、移动、压缩和解压操作。
import os
import shutil

#复制文件
s=open(r"E:\测试文件\test2.txt",'r')
d=open(r"E:\测试文件\testcopy2.txt","a")
shutil.copyfileobj(s,d,length=1024)

#拷贝整个文件
shutil.copyfile("E:\\测试文件\\test1.txt","E:\\测试文件\\test1copy.txt")
#同时复制文件的内容以及权限，也就是先copyfile()然后copymode()。
shutil.copy("E:\\测试文件\\test1.txt","E:\\测试文件\\test1copy2.txt")
#同时复制文件的内容以及文件的所有状态信息。先copyfile()后copystat()。
shutil.copy2("E:\\测试文件\\test1.txt","E:\\测试文件\\test1copy3.txt")

#递归地复制目录及其子目录的文件和状态信息
destPath="E:\测试文件\\视频副本3"
if(not os.path.exists(destPath)):
    shutil.copytree("E:\测试文件\\视频","E:\测试文件\\视频副本3")

#递归地删除目录及子目录内的文件。注意！该方法不会询问yes或no，被删除的文件也不会出现在回收站里，请务必小心！
delPath="E:\测试文件\\视频副本2"
if(os.path.exists(delPath)):
    shutil.rmtree(destPath)

#重命名文件
# s1="E:\测试文件\\视频副本3"
# t1="E:\测试文件\\视频副本3-1"
# if(os.path.exists(s1)):
#     shutil.move(s1,t1)

#文件压缩
shutil.make_archive(base_name="E:\\测试文件\\视频",format="zip",base_dir="E:\测试文件\\视频",root_dir="E:\测试文件\\视频")

#文件解压缩
shutil.unpack_archive("E:\\测试文件\\视频.zip","E:\\测试文件\\视频2",format="zip")