#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/12/25 20:46
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : locators.py
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
from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """主页的定位器，主页中所有定位元素都应该放在这"""
    GO_BUTTON = (By.ID, 'submit')


class SearchResultPageLocators(object):
    """搜索结果类，所有的搜索结果都应该放在这"""
    pass
