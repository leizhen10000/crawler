#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/1/11 10:43
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : read_ini.py
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
import configparser

import os

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('db_config.ini')

    print(config.sections())

    # os.path.join(os.)
    print(os.getcwd())
