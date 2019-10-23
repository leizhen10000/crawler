#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/8/28 09:49
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : extract_statistic.py
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

from olives.gov_static import gov_page


class ExtractData:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("http://www.pbc.gov.cn/diaochatongjisi/116219/116319/index.html")

    def get_into_detail(self):
        # 进入主界面
        main_page = gov_page.MainPage(self.driver)
        # 点击年份，查看详情
        main_page.click_year_for_detail()

    def get_aggregate_finance(self):
        # 进入社会融资规模界面
        detail_page = gov_page.DetailPage(self.driver)
        detail_page.click_aggregate_financing()

    def follow_data(self):
        """社会融资规模 增量统计表"""
        AFRE_page = gov_page.AFREPage(self.driver)
        AFRE_page.get_flow_html()

    def stock_data(self):
        """社会融资规模 存量统计表"""
        AFRE_page = gov_page.AFREPage(self.driver)
        AFRE_page.get_stock_html()


if __name__ == '__main__':
    web_driver = webdriver.Firefox()
    process = ExtractData(web_driver)
    process.get_into_detail()
    # 查看社会融资规模
    process.get_aggregate_finance()
    # 查看增量统计表
    process.follow_data()
    # 关闭driver
    web_driver.quit()
