#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import xml.sax
import time,datetime,os,sys

class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData=''
        self.type=''
        self.format=''
        self.year=''
        self.rating=''
        self.stars=''
        self.description=''

    # 元素开始调用
    def startElement(self,tag,attributes):
        self.CurrentData=tag
        if(tag=='movie'):
            print("*******Movie********")
            title=attributes['title']
            print("Title:",title)
    #元素结束调用
    def endElement(self,tag):
        data=self.CurrentData
        if data=='type':
            print("type:",self.type)
        elif data=='format':
            print("format:",self.format)
        elif data=='year':
            print("year:",self.year)
        elif data=='rating':
            print("rating:",self.rating)
        elif data=='stars':
            print("stars:",self.stars)
        elif data=='description':
            print("description:",self.description)
        self.CurrentData=''
    def characters(self,content):
        data=self.CurrentData
        if data == 'type':
            self.type=content
        elif data == 'format':
            self.format=content
        elif data == 'year':
            self.year=content
        elif data == 'rating':
           self.rating=content
        elif data == 'stars':
            self.stars=content
        elif data == 'description':
            self.description=content



if ( __name__ == "__main__"):
    # # 创建一个 XMLReader
    # parser = xml.sax.make_parser()
    # # 关闭命名空间
    # parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    #
    # # 重写 ContextHandler
    # Handler = MovieHandler()
    # parser.setContentHandler(Handler)
    # currPath=os.getcwd()
    # filePath=os.path.join(currPath,"xml",'movies.xml')
    # parser.parse(filePath)

    currPath=os.getcwd()
    filePath=os.path.join(currPath,"xml",'movies.xml')

    handler=MovieHandler()
    xml.sax.parse(filePath,handler)