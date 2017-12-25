#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/12/20 17:15
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : pprint_demo.py
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
from pprint import pprint

data = [
    (
        1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}
    ),
    (
        2, {'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L'}
    )
]

print('PRINT:', data)
# 简单的打印：
print('PPRINT:')
pprint(data)
