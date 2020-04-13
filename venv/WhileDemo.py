#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#利用while计算从1+2+3+...+100的数值
sum=0
i=1;
while i<=100:
    sum+=i
    i+=1
print("1+2+3+...+100=",sum)

#无限循环
# while 1==1:
#     num=int(input("请输入一个数字"))
#     print("你输入的数字是：",num)
#
# print('good bye!')

#while 循环使用 else 语句
i=0
while i<5:
    print(i,"小于5")
    i+=1
else:
    if 2>1:
        print(i,"大于等于5")
#简单语句组,类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中
# while True:print("hi ,how are you?")









