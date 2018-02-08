#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/12/26 17:45
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : airbnb.py
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
# 获取前20页整租放的名称、价格、评价数量、房屋类型、床数量
import os
from selenium import webdriver


def airbnb_info():
    # # Setup the profile.
    # firefox_profile = webdriver.FirefoxProfile()
    # # 禁止加载图片
    # firefox_profile.set_preference('permissions.default.image', 2)
    # # firefox_profile.set_preference('browser.migration.version', 9001)
    # # 禁用 css
    # # firefox_profile.set_preference('permissions.default.stylesheet', 2)
    # # 禁用js
    # # firefox_profile.set_preference('javascript.enabled', 'false')
    # # 禁用 flash
    # # firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    #
    # driver = webdriver.Firefox(firefox_profile=firefox_profile)

    options = webdriver.ChromeOptions()
    options.add_argument('lang=zh_CN.UTF-8')
    prefs = {
        'profile.default_content_setting_values.images': 2
    }
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(chrome_options=options)

    try:
        house_list = []
        driver.get('https://zh.airbnb.com/s/Shenzhen--China?'
                   'cdn_cn=1&s_tag=nNolWxOC&allow_override%5B%5D=')
        detail = driver.find_elements_by_xpath('//*[@class="_f21qs6"]/div/div[2]')
        for item in detail:
            house = {}
            # 名称
            name = item.find_element_by_xpath('./div/a/div[2]/div/div')
            '//*[@class="_f21qs6"]/div/div[2]/div/a/div[2]/div/div'
            house['name'] = name.text
            # 价格
            price = item.find_element_by_xpath(
                './div/a/div[3]/div/div/div/div/span/span[1]/span[1]/span/span[2]')
            house['price'] = price.text
            house_list.append(house)
        if not os.path.exists('result_data'):
            os.mkdir('result_data')
        with open('result_data/airbnb.txt', 'w', encoding='utf-8') as f:
            for house in house_list:
                f.writelines('#\n')
                f.writelines(str(house))
                f.writelines('\n')
        f.close()
    finally:
        driver.quit()


if __name__ == '__main__':
    airbnb_info()
