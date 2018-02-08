#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/2/8 11:49
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : using_list.py
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


def using_pop():
    """list 的 pop 用法"""
    # pop 函数一般用于移除列表中最后一个元素，并且返回该元素的值
    a_list = [123, 'xyz', 'zara', 'abc', 12.12]

    print('pos first one : ', a_list.pop(0))
    print('now A List is : ', a_list)

    print("A List : ", a_list.pop())
    print('now A List is : ', a_list)

    print("B List : ", a_list.pop(2))
    print('now A List is : ', a_list)

    pass


if __name__ == '__main__':
    using_pop()
