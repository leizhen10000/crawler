#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/8/28 09:03
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : gov_page.py
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
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from olives.gov_static.gov_locators import MainPageLocators, DetailPageLocators, AFREPageLocators


class BasePage(object):
    """初始化 浏览器驱动"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """统计数据的主界面，包含界面上的所有操作和验证"""

    def click_year_for_detail(self):
        """点击各个年份，查看统计数据详情"""
        year = 2018
        try:
            year_locator = MainPageLocators().locate_statistic_by_year(year)
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.element_to_be_clickable(year_locator))
            element.click()
        except TimeoutException:
            raise Exception("无法点击该按钮")


class DetailPage(BasePage):
    """详情界面"""

    def click_aggregate_financing(self):
        element = self.driver.find_element(
            *DetailPageLocators().AGGREGATE_FINANCE_LINK
        )
        element.click()

    def click_money_and_bank(self):
        element = self.driver.find_element(
            *DetailPageLocators().MONEY_AND_BANK_LINK
        )
        element.click()

    def click_credit_fund(self):
        element = self.driver.find_element(
            *DetailPageLocators().CREDIT_FUNDS_LINK
        )
        element.click()

    def click_financial_marker(self):
        element = self.driver.find_element(
            *DetailPageLocators().FINANCIAL_MARKET_LINK
        )
        element.click()

    def click_GGPI(self):
        element = self.driver.find_element(
            *DetailPageLocators().CGPI_LINK
        )
        element.click()


class AFREPage(BasePage):
    """社会融资规模 Aggregate Financing to the Real Economy(AFRE)"""

    def get_flow_html(self):
        element = self.driver.find_element(
            *AFREPageLocators().FLOW_HTML_LINK
        )
        element.click()

    def get_stock_html(self):
        element = self.driver.find_element(
            *AFREPageLocators().STOCK_HTML_LINK
        )
        element.click()
