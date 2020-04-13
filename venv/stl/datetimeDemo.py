#!/usr/bin/env python 
# -*- coding:utf-8 -*-

'''datetime 模块学习'''
import time
import datetime
from datetime import date
from datetime import time

from datetime import timedelta

#
# print(datetime)
# print(datetime.MAXYEAR)

# #date类方法
# print(date.max)
# print(date.min)
# print(date.resolution)
# # print(date.fromtimestamp(time.time()))
#
# #date实例方法
# d=date.today()
# print(d.year)
# print(d.month)
# print(d.day)
# print(d.toordinal())
# print(d.weekday())
# print(d.isoweekday())
# print(d.isocalendar())
# print(d.isoformat())
# print(d.strftime("%Y%m%d"))

#datetime.time类

# print(time.min)
# print(time.max)
# print(time.resolution)
# oTime=time(12,25,36,1555)
# print(oTime.hour)
# print(oTime.minute)
# print(oTime.second)
# print(oTime.microsecond)
# print(oTime.tzinfo)
# print(oTime.isoformat())
# print(oTime.strftime("%H%M%S.%f"))

#datetime.datetime类

# print(datetime.datetime.now())
# oDateTime=datetime.datetime.today()
# print(oDateTime)
# print(oDateTime.year)
# print(oDateTime.month)
# print(oDateTime.day)
# print(oDateTime.hour)
# print(oDateTime.minute)
# print(oDateTime.second)
# print(oDateTime.microsecond)
# print(oDateTime.date())
# print(oDateTime.time())
# print(oDateTime.timetz())
# print(oDateTime.utcnow())
# print(oDateTime.timetuple())
# print(oDateTime.utctimetuple())
# print(oDateTime.toordinal())
# print(oDateTime.weekday())
# print(oDateTime.isocalendar())
# print(oDateTime.isoformat())
# print(oDateTime.ctime())
# print(oDateTime.strftime("%Y-%m-%d %H:%M:%S.%f"))


#datetime.timedelta类
# oDT1=datetime.datetime(2020,3,29,14,15,28)
# # oDT2=datetime.datetime(2020,1,19,23,0,0)
# # oTimeDelta=timedelta(days=365)
# # print(oTimeDelta.total_seconds())
# # print(timedelta.min)
# # print(timedelta.max)
# # print(timedelta.resolution)
# # print(oTimeDelta.days)
# # print(oTimeDelta.seconds)
# # print(oTimeDelta.microseconds)
# # oInterval=oDT1-oDT2
# # print(oInterval.days)
# # print(oInterval.seconds)
# # print(datetime.datetime.now().timestamp())

t=1429417200.12346465
print(datetime.datetime.utcfromtimestamp(t))
cday = datetime.datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
nowTime=datetime.datetime.now().strftime("%X")
print(nowTime)








