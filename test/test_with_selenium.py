#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/12/21 14:38
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : test_with_selenium.py
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
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class GoogleTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.baidu.com')
        self.assertIn('百度', self.browser.title)
        # select = Select(self.browser.find_element_by_id('su'))
        # select.su
        time.sleep(3)
        self.browser.find_element(By.XPATH, '')


if __name__ == '__main__':
    unittest.main(verbosity=2)
