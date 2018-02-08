#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/12/20 19:26
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : selenium_demo.py
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
# 打开一个浏览器
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://blog.csdn.net/csdnnews/article/details/78859701')
assert 'CSDN' in driver.title
# 搜索输入框
elem = driver.find_element_by_class_name('input_search')
elem.click()
elem.send_keys('google')
elem.send_keys(Keys.RETURN)
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    sleep(3)
driver.quit()
print('Browser is closed')

# driver = webdriver.Chrome()
# driver.get('https://www.dianping.com/search/category/7/10/p1')
# driver.get('http://www.baidu.com')
# driver.close()
# 获取评论
# comment_list = driver.find_elements_by_class_name('comment_p')
# for comment in comment_list:
#     print(comment.text)
# time.sleep(3)
