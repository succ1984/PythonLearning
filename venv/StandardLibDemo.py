#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os

cwd=os.getcwd()
print(cwd)
# print(dir(os))
from datetime import date
now=date.today()
print(now)

#zlib
import zlib
s = b'witch which has which witches wrist watch'
print(len(s))
t=zlib.compress(s)
print(len(t))