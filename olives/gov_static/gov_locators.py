#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/8/28 09:08
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : gov_locators.py
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
from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """主界面上所有的元素定位器"""
    base_table_xpath = '//*[@id="12802"]/div[2]/table/tbody/tr/td/'
    # //*[@id="12802"]/div[2]/table/tbody/tr/td/div[19]/a
    STATISTIC_2018 = (By.XPATH, base_table_xpath + 'div[1]/a')
    STATISTIC_2017 = (By.XPATH, base_table_xpath + 'div[2]/a')
    STATISTIC_2016 = (By.XPATH, base_table_xpath + 'div[3]/a')
    STATISTIC_2015 = (By.XPATH, base_table_xpath + 'div[4]/a')
    STATISTIC_2014 = (By.XPATH, base_table_xpath + 'div[5]/a')
    STATISTIC_2013 = (By.XPATH, base_table_xpath + 'div[6]/a')
    STATISTIC_2012 = (By.XPATH, base_table_xpath + 'div[7]/a')
    STATISTIC_2011 = (By.XPATH, base_table_xpath + 'div[8]/a')
    STATISTIC_2010 = (By.XPATH, base_table_xpath + 'div[9]/a')
    STATISTIC_2009 = (By.XPATH, base_table_xpath + 'div[10]/a')
    STATISTIC_2008 = (By.XPATH, base_table_xpath + 'div[11]/a')
    STATISTIC_2007 = (By.XPATH, base_table_xpath + 'div[12]/a')
    STATISTIC_2006 = (By.XPATH, base_table_xpath + 'div[13]/a')
    STATISTIC_2005 = (By.XPATH, base_table_xpath + 'div[14]/a')
    STATISTIC_2004 = (By.XPATH, base_table_xpath + 'div[15]/a')
    STATISTIC_2003 = (By.XPATH, base_table_xpath + 'div[16]/a')
    STATISTIC_2002 = (By.XPATH, base_table_xpath + 'div[17]/a')
    STATISTIC_2001 = (By.XPATH, base_table_xpath + 'div[18]/a')
    STATISTIC_2000 = (By.XPATH, base_table_xpath + 'div[19]/a')
    STATISTIC_1999 = (By.XPATH, base_table_xpath + 'div[20]/a')

    def locate_statistic_by_year(self, year):
        return By.XPATH, self.base_table_xpath + 'div[{}]/a'.format(2019 - int(year))


class DetailPageLocators(object):
    """年份详情 所有元素定位器"""
    main_div_locator = '//div[@class="portlet"]'
    AGGREGATE_FINANCE_LINK = (  # 社会融资规模
        By.XPATH,
        main_div_locator + '/div[2]/table[2]/tbody/tr/td/a')
    MONEY_AND_BANK_LINK = (
        By.XPATH,
        main_div_locator + '/div[2]/table[5]/tbody/tr/td/a')
    CREDIT_FUNDS_LINK = (
        By.XPATH,
        main_div_locator + '/div[2]/table[8]/tbody/tr/td/a'
    )
    FINANCIAL_MARKET_LINK = (
        By.XPATH,
        main_div_locator + '/div[2]/table[11]/tbody/tr/td/a'
    )
    CGPI_LINK = (
        By.XPATH,
        main_div_locator + '/div[2]/table[14]/tbody/tr/td/a'
    )
    # //div[contains(contact(" ",@class," "), " portlet ")]
    # //*[@id="f8522e94cf7a4ca7aff09dc41c349af6"]/div[2]/table[2]/tbody/tr/td/a


class AFREPageLocators(object):
    """社会融资规模统计表页面"""
    FLOW_HTML_LINK = (
        By.XPATH,
        '//div[@id="con"]/table[3]/tbody/tr/td/table[1]/tbody/tr/td[2]/a')
    STOCK_HTML_LINK = (
        By.XPATH,
        '//div[@id="con"]/table[3]/tbody/tr/td/table[2]/tbody/tr/td[2]/a')
