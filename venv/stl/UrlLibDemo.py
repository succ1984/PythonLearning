#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#urllib学习

import urllib
import os
import time
import datetime
import sys
from urllib import request

urlAddr='http://www.cnblogs.com'
userAgent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

# with request.urlopen(urlAddr) as r:
#     data=r.read()
#     print("version：", r.version)
#     print("status:", r.status)
#     print("reason:",r.reason)
#     print("closed:",r.closed)
#     print("msg:",r.msg)
#     print("response headers:")
#     for k,v in r.getheaders():
#         print(f'{k}:{v}')
#     print("r.getheader(Content-Type):",r.getheader("Content-Type"))
#     print("Data:",data.decode("utf-8"))

req=request.Request(urlAddr)
req.add_header("Referer",'http://www.baidu.com')
with request.urlopen(req) as r:
    data=r.read()
    print("version：", r.version)
    print("status:", r.status)
    print("reason:",r.reason)
    print("closed:",r.closed)
    print("msg:",r.msg)
    print("response headers:")
    for k,v in r.getheaders():
        print(f'{k}:{v}')
    print("r.getheader(Content-Type):",r.getheader("Content-Type"))
    print("Data:",data.decode("utf-8"))
    print("request info:")
    print("url:",r.geturl())
    print("info:",r.info())
    print("getcode():",r.getcode())
    print("fullUrl:",req.full_url)
    print("type:",req.type)
    print("host:",req.host)
    print("selector",req.selector )
    print("data:",req.data)
    print("method:",req.get_method())
