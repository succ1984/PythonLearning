#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#随机数 模块 demo

import random
import string

random.seed()

#随机整数
print(random.randint(0,9))

#随机选取0到100的偶数
print(random.randrange(0,100,2))

#随机浮点数
print(random.random())
print(random.uniform(10,20))

#随机序列
print(random.choice('abcdefg&#%^*f'))
print(random.choice(['a','b','c','d','e']))
#
print(random.sample(range(1000), k=5))
#洗牌
items = [1, 2, 3, 4, 5, 6]
print(random.shuffle(items))
for x in items:
    print(x)

#生成指定长度字母数字随机序列
def gen_random_string(length):
    # 数字的个数随机产生
    num_of_numeric = random.randint(1,length-1)
    # 剩下的都是字母
    num_of_letter = length - num_of_numeric
    # 随机生成数字
    numerics = [random.choice(string.digits) for i in range(num_of_numeric)]
    # 随机生成字母
    letters = [random.choice(string.ascii_letters) for i in range(num_of_letter)]
    # 结合两者
    all_chars = numerics + letters
    # 洗牌
    random.shuffle(all_chars)
    # 生成最终字符串
    result = ''.join([i for i in all_chars])
    return result

if __name__ == '__main__':
    print(gen_random_string(64))
