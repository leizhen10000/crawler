#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/1/20 20:05
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : mongodb_demo.py
# @Software: PyCharm
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓   ┏┓
            ┏┛┻━━━┛┻┓
            ┃  ☃    ┃
            ┃ ┳┛  ┗┳ ┃
            ┃      ┻  ┃
            ┗━┓     ┏━┛
              ┃     ┗━━━┓
              ┃ 神兽保佑 ┣┓
              ┃ 永无BUG┏┛
              ┗┓┓┏━┳┓┏┛
               ┃┫┫ ┃┫┫
               ┗┻┛ ┗┻┛
"""
from pymongo import MongoClient

# 通过直接传入默认的 host 和 port 就可以连接
client = MongoClient('localhost', 27017)
print(client.address)
client.close()
print('第一种方式连接成功')

# 或者使用 URI 格式
client1 = MongoClient('mongodb://localhost:27017')
print(client1.address)
client1.close()
print('第二种方式连接成功')

# 配置文件格式也可以
db_info = {'host': 'localhost', 'port': 27017}
client2 = MongoClient(db_info)
print(client2.HOST)
print(client2.arbiters)
client2.close()
print('第三种方式连接成功')

# 连接固定需要密码的数据库
