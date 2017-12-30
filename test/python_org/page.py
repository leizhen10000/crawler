#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/12/25 16:27
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : page.py
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
# page 对象跟 web页面 一一对应
# 根据限免对层级的匪类，我们可以将测试代码和 实现类巧妙的分开
from test.python_org.element import BasePageElement
from test.python_org.locators import MainPageLocators


class SearchTextElement(BasePageElement):
    """根据特定的 定位器 获取搜索文本框"""
    locator = 'q'


class BasePage(object):
    """基础类用于初始化 driver"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """主页的 执行方法 """
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """校验 Python 在title 中"""
        return "Python" in self.driver.title

    def click_go_button(self):
        """点击执行搜索"""
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class SearchResultsPage(BasePage):
    """搜索结果页面的 执行方法都放在这"""

    def is_results_found(self):
        return 'No results found.' not in self.driver.page_source
