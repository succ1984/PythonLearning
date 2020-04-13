#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests
import datetime,time,sys,os,io

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safri/537.36'
}


res=requests.get("http://www.eastmoney.com",headers=headers)
print(type(res))
print(res.status_code)
print(res.headers)
print(res.cookies)
print(res.content.decode("utf-8"))
