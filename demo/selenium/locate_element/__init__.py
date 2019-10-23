#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/8/27 10:13
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : __init__.py.py
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
# 有很多中策略来定位页面中的元素，你在测试用例中可以使用最合适的方式
# Selenium 提供了以下的方法来定位元素
# find_element_by_id
# find_element_by_name
# find_element_by_xpath
# find_element_by_link_text
# find_element_by_partial_link_text
# find_element_by_tag_name
# find_element_by_class_name
# find_element_by_css_selector
# 上面都是查找单一的结果，要查找所有结果，改为 elements 就可以了
# find_elements_by_id
# find_elements_by_name
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector
#
# 除了以上狗狗你哟给你的方法，还有两个私有方法可以有效的定位页面中的对象
# 分别为：find_element 和 find_elements
# driver.find_element(By.XPATH, '//button[text()="Some text"]')
# driver.find_elements(By,XPATH, '//button')
# By 类中共有以下的不同属性
# ID = "id"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = 'partial link text'
# NAME = 'name'
# TAG_NAME = 'tag name'
# CLASS_NAME = 'class name'
# CSS_SELECTOR = 'css selector'
from selenium import webdriver


def locating_by_x():
    driver = webdriver.Firefox()
    driver.find_element_by_xpath()
    # XPath 是一个用来定位 XML 文档中节点的语言
    # XPath 扩展包含通过 id 和 name 属性来查找元素，并且可以解锁很多可能性，比如获取页面中第三个复选框

    # 使用 XPath 来定位的主要原因是，不需要一个确定的 id 或者 name 属性来定位元素
    # 可以使用绝对的位置（不建议使用）或者关联一个有id或者name属性的元素。
    # XPath 定位器可以找到特殊的元素通过其他属性，而不仅仅是 id 和 name 属性

    # 通过找到一个附近的元素，二者元素可以通过 id 和 name 属性定位到（一般来说是父级元素），然后再通过与该元素的层级关系，来定位需要的元素。
    # 这看起来会大大方便，而且使得测试脚本更加健壮
