#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#日志模块学习

import logging
import logging.config
import os
import json

# logging.basicConfig(filename=r"E:\sushee\python3\Learning\LearningDemo\venv\logs\logs.txt"
#                     ,filemode="a"
#                     ,level=logging.DEBUG
#                     ,format='%(asctime)s %(message)s'
#                     ,datefmt='%Y-%m-%d %H:%M:%S')
# logging.warning("warning1")
# logging.error("error")
# logging.critical("critical")

#高级用法

# #创建记录器
# loggerHelper=logging.getLogger("abc")
# loggerHelper.setLevel(logging.DEBUG)
# #创建一个控制台处理器，并将日志级别设为debug
# handler=logging.StreamHandler()
# handler.setLevel(logging.DEBUG)
# #创建formatter格式化器
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s'
#                               ' - %(message)s - %(processName)s -%(threadName)s %(module)s'
#                               ' 	%(lineno)d %(created)f 	%(filename)s %(pathname)s')
#
# # 将formatter添加到日志处理器
# handler.setFormatter(formatter)
# #将处理器添加到记录器
# loggerHelper.addHandler(handler)
#
# #调用
# loggerHelper.debug('debug message')
# loggerHelper.info('info message')
# loggerHelper.warning('warn message')
# loggerHelper.error('error message')
# loggerHelper.critical('critical message')


#logging配置文件的方式
curDir=os.getcwd()
configFilePath=os.path.join(curDir,'logs','logging.conf.json')
# logging.config.fileConfig(configFilePath) # 读取config文件
with open(configFilePath,'r') as f:
    config=json.load(f)
    logging.config.dictConfig(config)

# 创建logger记录器


# 使用日志功能
logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message')



