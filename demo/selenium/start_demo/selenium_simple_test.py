#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/8/26 11:39
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : selenium_simple_test.py
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
# Selenium 最广泛的应用场景就是编写测试用例
# selenium 包本身并不提供测试工具或者测试框架
# 可以通过 Python 的unittest模块来编写测试用例，也可以选择 py.test 或者 nose

import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# unittest 模块是内置于Python的测试模块，它基于Java 的JUnit而来
# 这个模块提供了组织测试用例的框架

# 测试用例类继承自 unittest.TestCase，同样也是告知 unittest 模块这是一个测试用例

class PythonOrgSearchTest(unittest.TestCase):
    # setUp 方法是初始化的一部分，类class中的每一个测试方法被调用时，此方法都会被调用一次
    def setUp(self):
        # 在这里初始化的内容是：创建一个 Firefox WebDriver 的实例
        self.driver = webdriver.Firefox()

    # 测试用例方法，这个方法应当以 test_ 开头
    def test_search_in_python_org(self):
        # 创建一个链接指向 setUp方法中创建的 driver 对象
        driver = self.driver
        # 加载页面，细节在 selenium_demo.py 方法中讲过
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    # tearDown 方法将会在每一个测试方法执行完成后调用
    # 这个位置的邹勇就是清理所有的操作
    def tearDown(self):
        # 清除操作：关闭tab
        self.driver.close()


# 执行测试套件
if __name__ == '__main__':
    # 执行全部测试用例
    unittest.main()
