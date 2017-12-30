#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/12/25 16:29
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : element.py
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

# Page elements
# 这个类包含页面上基础元素
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePageElement(object):
    """基础页面类 用于初始化每个 page 对象"""

    def __set__(self, instance, value):
        """设置文本到元素中"""
        driver = object.driver
        driver.find_element_by_name()
        WebDriverWait(driver, 100).until(
            lambda driver: webdriver.find_element_by_name(self.locator)
        )
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """获取对象的文本信息"""
        driver = object.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator)
        )
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")
