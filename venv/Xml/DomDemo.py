#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import xml.dom.minidom
import os

currPath = os.getcwd()
filePath = os.path.join(currPath, "xml", 'movies.xml')
# 使用minidom解析器打开 XML 文档
domTree=xml.dom.minidom.parse(filePath)
root=domTree.documentElement
print("prettyXml:",domTree.toprettyxml())
if root.hasAttribute("shelf"):
    print("Root element : %s" % root.getAttribute("shelf"))
# 在集合中获取所有电影
movies = root.getElementsByTagName("movie")
print(f'共有{movies.length}部电影')
# 打印每部电影的详细信息
for item in movies:
    print("***********Movie*********")
    if(item.hasAttribute("title")):
        print("Title:",item.getAttribute("title"))
    nodeType=item.getElementsByTagName("type")[0]
    print("type:",nodeType.childNodes[0].nodeValue)
    nodeFormat=item.getElementsByTagName("format")[0]
    print("format:",nodeFormat.childNodes[0].nodeValue)
    nodeRating=item.getElementsByTagName("rating")[0]
    print("rating:",nodeRating.childNodes[0].nodeValue)
    nodeDesc=item.getElementsByTagName("description")[0]
    print("description:",nodeDesc.childNodes[0].data)



