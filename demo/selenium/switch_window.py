#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/2/8 15:54
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : switch_window.py
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
import time
from selenium import webdriver

driver = webdriver.Chrome()
# 打开某网站的主页 -- 第一个窗口
driver.get('http://www.kgc.cn/')
driver.maximize_window()  # 最大化窗口

# 点击全部课程 -- 第二个窗口
driver.find_element_by_link_text('全部课程').click()
time.sleep(3)

# 1. 来回切换打开的所有窗口
handles = driver.window_handles
for handle in handles:
    # 这个方法已经不建议采用，看源码也知道调用过程
    # driver.switch_to_window(handle)
    driver.switch_to.window(handle)
    time.sleep(1.5)
# 2. 直接切换到第二个窗口
driver.switch_to.window(handles[1])
# 由于只有两个窗口，当成list就好
driver.switch_to.window(handles[-1])
time.sleep(3)
# 3. 特定场景，切换到第二个窗口
cur_handle = driver.current_window_handle  # 当前句柄
for handle in handles:
    if handle != cur_handle:
        driver.switch_to.window(handle)
time.sleep(3)
# 点击第二页中某个链接
# 通过 Xpath 也可以找到该元素
# driver.find_element_by_xpath('//*[@id="leftContent"]/dl/dd[2]/div/a[4]').click()
driver.find_element_by_link_text('Android').click()
time.sleep(3)

# 关闭浏览器
# driver.close()
driver.quit()
print('浏览器已经被关闭')

# 本文参考至 http://blog.csdn.net/gz_testing/article/details/71251901
