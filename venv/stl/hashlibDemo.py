#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import hashlib
import hmac

#计算md5值
m=hashlib.md5()
m.update(b"abcdefg")
m.update(b"hello")
print(m.digest())
print(m.hexdigest())

#计算sha1值
oSHA1=hashlib.sha256()
oSHA1.update("hello baby!".encode("utf-8"))
print("sha1值为："+oSHA1.hexdigest())


#hamc方式,即md5+salt格式的标准化方法
message=b"abcdefghijlmn"
key=b'hello'
hmac=hmac.new(key,message,digestmod="md5")
print("hmac算法结果："+hmac.hexdigest())


