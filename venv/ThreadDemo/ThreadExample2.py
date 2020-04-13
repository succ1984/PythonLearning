#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import  threading
import sys,os,time

# def show(arg):
#     time.sleep(1)
#     print('thread '+str(arg)+" running....")
#
# if __name__ == '__main__':
#     for i in range(10):
#         t = threading.Thread(target=show, args=(i,))
#         t.start()



# def doWaiting():
#     print('start waiting:', time.strftime('%H:%M:%S'))
#     time.sleep(3)
#     print('stop waiting', time.strftime('%H:%M:%S'))
#
# t = threading.Thread(target=doWaiting)
# t.start()
# # 确保线程t已经启动
# time.sleep(1)
# print('start job')
# #等待子线程(t)结束,再往下执行..
# t.join()
# print('end job')


def run():

    print(threading.current_thread().getName(), "开始工作")
    time.sleep(2)       # 子线程停2s
    print(f"{threading.current_thread().getName()}工作完毕"+os.linesep)
    print("当前活动线程数量："+str(threading.active_count())+os.linesep)

for i in range(3):
    t = threading.Thread(target=run,name=f"线程{i+1}")
    #t.setDaemon(True)   # 把子线程设置为守护线程，必须在start()之前设置
    t.start()
    # t.join()


time.sleep(1)     # 主线程停1秒
print("主线程结束了！")
print(threading.active_count())  # 输出活跃的线程数