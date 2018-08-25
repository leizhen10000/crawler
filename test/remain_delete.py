#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/2 22:03
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : remain_delete.py
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
from collections import Iterable

from itertools import islice


def g():
    yield 1
    yield 2
    yield 3


print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
print('Iterable? "abc":', isinstance('abc', Iterable))
print('Iterable? 123:', isinstance(123, Iterable))
print('Iterable? g():', isinstance(g(), Iterable))


def triangles():
    a = [1]
    while True:
        yield a
        a = [1] + [a[i] + a[i + 1] for i in range(len(a) - 1)] + [1]


print(list(islice(triangles(), 10)))
