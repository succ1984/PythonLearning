#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#For循环学习Demo ，Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
languages=['C#','Java','Python','Php','Asp','Nodejs','C','C++']
for x in languages:
    print(x,end=',')

sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

#range()函数, 如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列
for i in range(5):
    print(i)
for i in range(5,9):
    print(i)

for i in range(0, 10, 3) :
    print(i)

a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
   print(i, a[i],end=',')

set1={'a','b','c','d','e','f'}
for item in set1:
    if item=='e':
        break
    elif item=='c':
        continue
    else:
        print(item)
print("循环结束")

for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")


