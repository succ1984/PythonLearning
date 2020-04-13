#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import pickle

#pickle模块则是Python专用的持久化模块，可以持久化包括自定义类在内的各种数据，比较适合Python本身复杂数据的存贮
#只能用于Python环境，不能用作与其它语言进行数据交换，不通用。


data = {
    'a': [1, 2.0, 3, 4+6],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

with open("E:\\测试文件\\pickleTest.txt","wb") as f:
    pickle.dump(data,f)

with open("E:\\测试文件\\pickleTest.txt","rb") as f:
   oData= pickle.load(f)
   print(oData)


#自定义类

class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def show(self):
        print(self.name+"_"+str(self.age))

aa=Person("张三",36)
aa.show()
f=open("E:\\测试文件\\pickleTest.txt","wb")
pickle.dump(aa,f)
f.close()
# del Person        # 注意这行被注释了
f=open("E:\\测试文件\\pickleTest.txt","rb")
bb=pickle.load(f)
f.close()
bb.show()


