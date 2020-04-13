#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import socket
import sys
import os
#一次只能处理一个客户端

# 创建 socket 对象
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
#获取主机名称
host = socket.gethostname()

port = 1234
#绑定端口号
serversocket.bind((host, port))
# 设置最大连接数，超过后排队
serversocket.listen(5)
print('启动socket服务，等待客户端连接...')
conn, address = serversocket.accept()     # 等待连接，此处自动阻塞
while True:     # 一个死循环，直到客户端发送‘exit’的信号，才关闭连接
    client_data = conn.recv(1024).decode()      # 接收信息
    if client_data == "exit":       # 判断是否退出连接
        exit("通信结束")
    print("来自%s的客户端向你发来信息：%s" % (address, client_data))
    conn.sendall('服务器已经收到你的信息'.encode())    # 回馈信息给客户端
conn.close()    # 关闭连接