#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#第三方网络请求模块 requests 学习,  模拟用户登录

import os,time
import requests
import http.cookiejar as cookielib
import re

#获取动态隐藏的参数，为post做准备
def get_hiddenvalue(sourceCode):

    VIEWSTATE =re.findall(r'<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(.*?)" />', sourceCode,re.I)
    EVENTVALIDATION =re.findall(r'input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="(.*?)" />', sourceCode,re.I)
    VIEWSTATEGENERATOR=re.findall(r'input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="(.*?)" />', sourceCode,re.I)
    return VIEWSTATE[0],EVENTVALIDATION[0],VIEWSTATEGENERATOR[0]


getUrl="http://op.banmachewu.com/login.aspx"
postUrl='http://op.banmachewu.com/login.aspx'
imgUrl='http://op.banmachewu.com/Manage/CheckCode.aspx'
memberUrl='http://op.banmachewu.com/manage/order/orderList.aspx'
userName='scc'
pwd='asdasd'
cookieFileName='opCookier.txt'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    ,'Host':'op.banmachewu.com'
    ,'Referer': 'http://op.banmachewu.com/'

    }

session = requests.Session()
# session.cookies=cookielib.LWPCookieJar(filename=cookieFileName)
res1=session.get(getUrl,headers=headers)
resContent=res1.content.decode('utf-8')
VIEWSTATE,EVENTVALIDATION,VIEWSTATEGENERATOR=get_hiddenvalue(resContent)





res2=session.get(imgUrl)
with open('validatcode.jpg', 'wb') as f:
    f.write(res2.content)
validateCode=input("请输入验证码：")

print(session.cookies)
postData={
        "txtLoginName":userName
        ,"txtPassword":pwd
        , 'txtCode':validateCode
        ,'__VIEWSTATE':VIEWSTATE
        ,'__VIEWSTATEGENERATOR':VIEWSTATEGENERATOR
        ,'__EVENTVALIDATION':EVENTVALIDATION
        ,'btnServer':'登录'
}
# #
res=session.post(postUrl,data=postData)
# session.cookies.save(cookieFileName)
print(res.status_code)
print(res.content.decode('utf-8'))
print(session.cookies)

resMemberPage=session.post(memberUrl)
print(res.content.decode("utf-8"))
print(session.cookies)