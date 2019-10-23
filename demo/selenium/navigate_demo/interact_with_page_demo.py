#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/8/26 18:04
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : interact_with_page_demo.py
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
# 与页面的交互
# 通过网址进入界面，并没有太大用处，只是作为一个入口
# 我们真正需要做的是与页面交互，或者更为具体的说，是与页面中的HTML元素交互
from selenium import webdriver


def get_element():
    # <li id="news" class="tier-1 element-6  " aria-haspopup="true"/>
    driver = webdriver.Firefox()
    driver.get("http://www.python.org")
    element = driver.find_element_by_id("news")
    print(element.text)
    driver.close()


# find_element_by_id
# find_element_by_name
# find_element_by_xpath
# 同样可以通过 text 来查找元素，但是要注意，text文本要完全匹配
# 要注意的还有通过 XPATH 来查找元素，如果不止一个元素匹配，将只会返回第一个被匹配的元素
# 如果没有元素匹配，将会抛出 NoSuchElementException


# 针对文本框，可以做输入
# element.send_keys("some text")
# 可以模拟按键操作
# element.send_keys(" and some", Keys.ARROW_DOWN)
# 清除文本框内容
# element.clear()


if __name__ == '__main__':
    get_element()
