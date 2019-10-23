#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/8/27 13:42
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : explicit_waits.py
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
# 确切式等待
# 最极端的例子就是 time.sleep() 可以理解为跟这个相似，只不过这里的条件是设置了确切的时间来等待
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("http://somedomain/url_that_delays_loading")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.ID, 'myDynamicElement'))
    )
finally:
    driver.quit()

# 这里规定了10s等待时间，在该时间内没有找到元素，将会抛出 TimeoutException 异常
# 默认情况下 WebDriverWait 会等待 500ms

# Expected Conditions
# 在自动化操作web浏览器的时候，EC 提供了很多常用的条件，接下来将会一一列出
# title_is
# title_contains
# presence_of_element_located
# visibility_of_element_located(locator)
# visibility_of(element)
# presence_of_all_elements_located(locator)
# text_to_be_present_in_element(locator, text_)
# text_to_be_present_in_element_value(locator, text_)
# frame_to_be_available_and_switch_to_it(locator)
# invisibility_of_element_located()
# element_to_be_clickable()
# staleness_of() # todo: 没看懂什么意思，应该用的比较少
# element_to_be_selected(element)
# element_located_to_be_selected(locator)
# element_selection_state_to_be(element)
# element_located_selection_state_to_be(loactor)
# alert_is_present()
