#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/8/27 14:50
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : custom_wait_conditions.py
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


# 你可以自己定义等待条件，如果没有任何一个预置的方法符合你的需求
# 只需类中包含 __call__ 方法，并且返回是否符合条件即可

class ElementHasCssClass(object):
    """
    An expectation for checking that an element has a particular css.

    locator - used to find the element
    returns the WebElement one it has the particular css class
    """

    def __init__(self, locator, css_class):
        self.locator = locator
        self.css_class = css_class

    def __call__(self, driver):
        element = driver.find_element(*self.locator)  # Finding the refrenced element
        if self.css_class in element.get_attribute("class"):
            return element
        else:
            return False
