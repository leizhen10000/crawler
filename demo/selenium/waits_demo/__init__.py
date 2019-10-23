#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/8/27 11:36
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
# 现在很多 web app 都使用了 AJAX 技术
# 当浏览器加载页面的时候，所有的元素都会在不同的时间点加载
# 这就导致了定位元素的困难：如果一个元素在DOM中还没有出现，定位元素的方法就会抛出 ElementNotVisibleException
#   异常
# 但是通过等待，我们能解决这类问题
# Waiting 在不同的操作中提供了时间的宽裕
# Selenium WebDriver 提供了两种不同的等待方式，隐晦式和确切式 implicit & explicit
# 隐晦式等待 implicit wait 会让 WebDriver 在继续执行下一步之前，等待确切的条件触发
# 确切式等待 explicit wait 会让 WebDriver 在定位元素时候会等待一个确切的时长
