#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/8/26 11:21
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : simple_usage.py
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
from selenium.webdriver.common.keys import Keys

# selenium.webdriver 模块提供了 WebDriver 所有的实现方法
# 包含 FireFox，Chrome，IE，以及远程调用
# Keys 类提供了键盘上的各种按键，包括 RETURN，F1，ALT等等

# Firefox WebDrivers 实习在这里被创建
driver = webdriver.Firefox()
# driver.get() 方法将会根据给定的 URL 跳转到页面
# **WebDriver 等待页面完全家在完才会返回控制权给测试代码或脚本**
# 值得注意的是，如果页面加载使用了大量的异步AJAX，那么web驱动将无法确定页面合适被加载完成
# 如果要确保页面被完全加载，可以添加 WebDriverWait 方法
driver.get("http://www.python.org")
# 断言并确认 Python 这个单词是否在其中
assert "Python" in driver.title
# WebDriver 提供了许多方式来查找元素，类似于 find_element_by_* 方法
# 比如，输入框元素可以通过名字属性来定位，则调用 find_element_by_name 方法
# 定位元素，将在后面的 Locating Elements 章节中讲述
elem = driver.find_element_by_name("q")
# 模拟键盘发送按键
# 为了安全期间，我们首先要清除所有预先填充的文本，比如"搜索"，这样就不会影响接下来的正常输入
elem.clear()
elem.send_keys('pycon')
elem.send_keys(Keys.RETURN)
# 在提交页面后，如果有返回结果应该获取，并且可以校验返回结果中是否有期望内容
# 同样通过断言来验证
assert "No results found." not in driver.page_source
# 最后，浏览器窗口将被关闭
# 同样可以使用quit方法来代替close
# quit 将会推出整个浏览器应用
# close 只是关闭当前的 tab 标签页，但是如果只有一个标签页被打开，默认的情况下，浏览器应用同样会退出
driver.close()
