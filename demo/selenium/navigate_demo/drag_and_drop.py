#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/8/26 21:26
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : drag_and_drop.py
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
# 你可以使用 drag and drop 拖拽方法
# 不管是定距离移动元素，或者是将元素拖拽到另一个元素上
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
element = driver.find_element_by_name("source")
target = driver.find_element_by_name("target")

action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()
