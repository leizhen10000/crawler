#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/12/25 16:09
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : python_org_search.py
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
import unittest


from selenium import webdriver

from test.python_org import page


class PythonOrgSearch(unittest.TestCase):
    """如何封装一个 Page 对象"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.python.org')

    def test_search_in_python_org(self):
        """
        测试 在 python.org 中搜索 "python" ，然后查看搜索结果
        是否包含该字段
        """
        # 加载主界面
        main_page = page.MainPage(self.driver)
        # 验证 Python 在 title 中
        # assert main_page.is_title_matches()."Python.org title dose"
