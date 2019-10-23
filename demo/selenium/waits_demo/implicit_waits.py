#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/8/27 14:56
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : implicit_waits.py
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
# 隐晦式等待 (implicit wait) 告知 WebDriver 保持 DOM 一段时间，直到元素存在并找到
# 默认值是指，一旦时间被设定，在整个 WebDriver对象的生命周期内，都保持值不变
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10)  # seconds
driver.get("http://somedomain/url_that_delays_loading")
myDynamicElement = driver.find_element_by_id("myDynamicElement")
