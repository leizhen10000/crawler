#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/12/26 11:26
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : set_firefox_option.py
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

# Setup the profile.
firefox_profile = webdriver.FirefoxProfile()
# 禁止加载图片
firefox_profile.set_preference('permissions.default.image', 2)
# firefox_profile.set_preference('browser.migration.version', 9001)
# 禁用 css
firefox_profile.set_preference('permissions.default.stylesheet', 2)
# 禁用js
firefox_profile.set_preference('javascript.enabled', 'false')
# 禁用 flash
firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')

driver = webdriver.Firefox(firefox_profile=firefox_profile)

urls = [
    'http://news.sina.com.cn/',
    'http://mil.news.sina.com.cn/',
    'http://news.sina.com.cn/society/',
    'http://finance.sina.com.cn/'
]
start_time = time.time()
for url in urls:
    driver.get(url=url)
print('执行时间:', '%.2f' % (time.time() - start_time))
driver.quit()
