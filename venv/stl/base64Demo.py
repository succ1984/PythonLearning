#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#base64 demo
'''
Base64是一种用64个字符来表示任意二进制数据的方法。

'''

import base64

print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode('abcd--__'))