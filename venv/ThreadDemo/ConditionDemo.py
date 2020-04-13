#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#条件多线程 学习

import os,threading,time

num = 0
con = threading.Condition()

class Foo(threading.Thread):

    def __init__(self, name, action):
        super(Foo, self).__init__()
        self.name = name
        self.action = action

    def run(self):
        global num
        con.acquire()
        print("%s开始执行..." % self.name)
        while True:
            if self.action == "add":
                num += 1
            elif self.action == 'reduce':
                num -= 1
            else:
                exit(1)
            print("num当前为：", num)
            time.sleep(1)
            if num == 5 or num == 0:
                print("暂停执行%s！" % self.name)
                con.notify()
                con.wait()
                print("%s开始执行..." % self.name)
        con.release()

if __name__ == '__main__':
    a = Foo("线程A", 'add')
    b = Foo("线程B", 'reduce')
    a.start()
    b.start()



