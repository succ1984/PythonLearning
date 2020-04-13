#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import json

dicData={"personName":"succ","age":36,"hobbies":["football","basketball","play game"]}
#dump
with open("E:\\测试文件\\testjson.txt","w",encoding="utf-8") as f:
    json.dump(dicData,f)
#dumps
jsonData=json.dumps(dicData)
print(jsonData)

#load
with open("E:\\测试文件\\testjson.txt","r",encoding="utf-8") as f:
    oDic=json.load(f)
    print(oDic)
#loads
oLoads=json.loads('{"personName":"succ","age":36,"hobbies":["football","basketball","play game"]}')
print("oLoads为：",oLoads)
