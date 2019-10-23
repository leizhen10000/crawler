#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/8/28 11:52
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : aa.py
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
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.pbc.gov.cn/diaochatongjisi/resource/cms/2018/04/2018041118102745057.htm")

title_elem = driver.find_element_by_xpath(
    '//div[@id="社会融资规模增量2017-12_8640"]/table/tbody/tr[6]/td[1]'
)
title_elem2 = driver.find_element(
    By.XPATH,
    '//*[@id="社会融资规模增量2017-12_8640"]/table/tbody/tr[6]/td[2]')

'//*[@id="社会融资规模增量2017-12_8640"]/table/tbody/tr[6]/td[8]'

elem_list = []
for index in range(1, 9):
    elem = driver.find_element(
        By.XPATH,
        '//*[@id="社会融资规模增量2017-12_8640"]/table/tbody/tr[6]/td[{}]'.format(index)
    )
    elem_list.append(elem.text.strip(''))

month_list = []
AFRE_list = []
result = {}
for index in range(0, 12):
    row_locator = '//*[@id="社会融资规模增量2017-12_8640"]/table/tbody/tr[{}]'.format(8 + index)
    month = driver.find_element(By.XPATH, row_locator + '/td[1]')

    AFRE = driver.find_element(By.XPATH, row_locator + '/td[2]')
    RMB_loans = driver.find_element(By.XPATH, row_locator + '/td[3]')
    foreign_loans = driver.find_element(By.XPATH, row_locator + '/td[4]')
    entrusted_loans = driver.find_element(By.XPATH, row_locator + '/td[5]')
    trust_loans = driver.find_element(By.XPATH, row_locator + '/td[6]')
    undiscounted = driver.find_element(By.XPATH, row_locator + '/td[7]')
    corporate_bond = driver.find_element(By.XPATH, row_locator + '/td[8]')
    equity_finance = driver.find_element(By.XPATH, row_locator + '/td[9]')

    result[month] = {'AFRE': AFRE, 'RMB_loans': RMB_loans, 'foreign_loans': foreign_loans,
                     'entrusted_loans': entrusted_loans, 'trust_loans': trust_loans,
                     'undiscounted': undiscounted, 'corporate_bond': corporate_bond,
                     'equity_finance': equity_finance}

driver.quit()
