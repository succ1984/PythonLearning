#!/usr/bin/env python 
# -*- coding:utf-8 -*-

age=int(input())
output=''
if age<=12:
    output='小学生'
elif age<=15:
    output='初中生'
elif age<=18:
    output='高中生'
else:
    output='大学生'
print(f'You are {output}')
