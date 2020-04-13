#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import urllib
from urllib import request
from urllib import parse
from urllib import error
from urllib import robotparser
import os,sys,time


postUrl='http://op.banmachewu.com:80/user/login.aspx?a=1&b=2#abc'
# userName=input("请输入用户名：")
# pwd=input("请输入密码：")
#urlparse
oParse=parse.urlparse(postUrl)
print(oParse.geturl())
print(oParse)
print(oParse.port)

#urlunparse
urlParams=('http','op.banmachewu.com','login.aspx','','a=1&b=2','abc')
url=parse.urlunparse(urlParams)
print(url)

#urljoin,注意第2个参数带'/'与不带'/'之间的区别
joinUrl=parse.urljoin("http://op.banmachewu.com/user/login.aspx",'user1/abc/list.aspx')
print(joinUrl)

#urlsplit
oSplit=parse.urlsplit(postUrl)
#parse_qsl
dicParse=parse.urlparse(postUrl)
szQuery=dicParse.query
listQuery=parse.parse_qsl(szQuery)
dic2ListQuery=dict(listQuery)
dicQuery=parse.parse_qs(szQuery)
print(listQuery)
print(dic2ListQuery)
print(dicQuery)

#quote,unquote
quoteResult=parse.quote("a=我爱你&b=中国")
print(quoteResult)
print(parse.unquote(quoteResult))

#urlencode
szParams=parse.urlencode({'a':'我爱你中国','b':2})
print(szParams)
dicParams=parse.parse_qs(szParams)
print(dicParams)
