#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from contextlib import contextmanager
from contextlib import closing
from urllib.request import urlopen

#@contextlib还有一些其他decorator，便于我们编写更简洁的代码。
#contextmanger用法
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")

#closing
with closing(urlopen('http://www.baidu.com')) as page:
    for line in page:
        print(line.decode("utf-8"))
