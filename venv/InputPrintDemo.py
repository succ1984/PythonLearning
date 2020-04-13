#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#Python3 输入和输出 学习Demo
for x in range(1, 11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),end=' ')
    print(repr(x*x*x).rjust(4))

# str = input("请输入：");
# print ("你输入的内容是: ", str)

#文件读写
#写文件
filePath=r'E:\sushee\python3\Learning\LearningDemo\venv\abc.txt'
file=open(filePath,mode='a+')
file.write("abc---end")
file.close()

#读取文件内容
fOpen=open(filePath,mode='r') # 打开一个文件
# content=fOpen.read()
#content=fOpen.readline()
content=fOpen.readlines()
print(content)
#关闭打开的文件
fOpen.close()

#
# 打开一个文件
f = open(filePath, "r")

for line in f:
    print(line, end='')

# 关闭打开的文件
f.close()

#文件写入
fWrite=open(filePath,mode='a+')
num=fWrite.write('"Python 是一个非常好的语言。\n是的，的确非常好!!\n')
print(f"\\n写入了{num}个字符")
print(f"文件对象当前所处的位置{fWrite.tell()}")
print("文件名称为："+fWrite.name)
fWrite.close()

#pickle 模块 ,python的pickle模块实现了基本的数据序列和反序列化。


