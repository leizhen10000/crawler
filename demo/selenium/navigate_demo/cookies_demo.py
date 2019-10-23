#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/8/27 10:08
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : cookies_demo.py
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
from selenium import webdriver


class CookiesDemo:
    pass

    driver = webdriver.Firefox()

    # Go to the correct domain
    driver.get("http://www.example.com")

    # Now set the cookie, This one's valid for the entire domain
    cookie = {'name': 'foo', 'value': 'bar'}
    driver.add_cookie(cookie)

    # And now output all the available cookies for current URL
    driver.get_cookies()

    driver.quit()
