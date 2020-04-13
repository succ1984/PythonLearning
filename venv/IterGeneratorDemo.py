#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#Python 迭代器与生成器学习Demo
import sys

list1=[1,2,3,4,'a','b','c']
iter1=iter(list1)
# for x in iter1:
#     print(x)


# while True:
#     try:
#         print (next(iter1))
#     except StopIteration:
#         sys.exit()


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 30:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)


#生成器 generator,在 Python 中，使用了 yield 的函数被称为生成器（generator）。

def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(100)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()


