#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import re

print(re.match("www","www.runoob.com"))
print(re.match('com', 'www.runoob.com'))

line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")

#search
import re

print(re.search('www', 'www.runoob.com'))  # 在起始位置匹配
print(re.search('com', 'www.runoob.com'))  # 不在起始位置匹配

#
import re

line = "Cats are smarter than dogs"

searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
    print("searchObj.start(0) : ", searchObj.start(0))
    print("searchObj.end(0) : ", searchObj.end(0))
else:
    print("Nothing found!!")
#match与search区别，match只匹配字符串开始位置，而seach则搜索整个字符串

import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print("search --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

#替换
phone = "2004-959-559 # 这是一个电话号码"

# 删除注释
num = re.sub(r'#.*$', "", phone)
print("电话号码 : ", num)

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码 : ", num)

#match返回对象包含方法
szContent='hello world, hello web!!!'
patt1=re.compile('([a-z]+) ([a-z]+)')
m=patt1.match(szContent)
print(m)
print(m.group(0)) #返回匹配成功的整个子串
print(m.span(0)) #返回匹配成功的整个子串的索引
print(m.group(1))#返回第1个分组匹配成功的子串
print(m.span(1))#返回第1个分组匹配成功的子串索引
print(m.group(2))#返回第2个分组匹配成功的子串
print(m.span(2))#返回第2个分组匹配成功的子串索引
print(m.groups())#等价于(m.group(0),m.group(1))

#findall方法，在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
#注意： match 和 search 是匹配一次 findall 匹配所有。
toSearch="I'm 123 sushee,how are you? 456"
patt2=re.compile("\d+")#查找数字
res1=patt2.findall(toSearch)
res2=patt2.findall(toSearch,0,20)
print(res1)
print(res2)
#finditer ,和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
res3=patt2.finditer(toSearch,0)
for x in res3:
    print(x.group())

#split 方法按照能够匹配的子串将字符串分割后返回列表
lst1=re.split('\W+', 'runoob, runoob, runoob.')
print(lst1)
lst2=re.split(' ','Hello world! baby')
print(lst2)






