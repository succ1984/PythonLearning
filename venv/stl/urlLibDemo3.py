#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#模拟登录学习

import urllib
from urllib import request
from urllib import parse
from urllib import error
from urllib import robotparser
import os,sys,time,http
import http.cookiejar
import requests


postUrl='http://op.banmachewu.com:80/login.aspx?a=1&b=2#abc'
userName=input("请输入用户名：")
pwd=input("请输入密码：")

if not userName:
    print("请输入用户名")
    sys.exit()
if not pwd:
    print("请输入密码")
    sys.exit()


req=request.Request(postUrl)
req.add_header("Referer",'http://www.baidu.com')
params=parse.urlencode({"txtLoginName":userName,"txtPassword":pwd,'txtCode':validateCode})
#构造cookie
cookie = http.cookiejar.CookieJar()

#由cookie构造opener
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

#发送登录请求，此后这个opener就携带了cookie，以证明自己登录过
resp = opener.open(req)
# with request.urlopen(req,params.encode('utf-8')) as r:
#     print(r.status)
#     print(r.reason)
#     headers=r.getheaders()
#     for k,v in headers:
#         print(f"{k}:{v}")
#     data=str(r.read().decode('utf-8'))
#     print(data)
data=str(resp.read().decode('utf-8'))
print(data)
validateImgUrl='http://op.banmachewu.com/Manage/CheckCode.aspx'

validateCode=input("请输入验证码:")




