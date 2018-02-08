#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/2/8 11:29
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : district.py
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
import requests
from bs4 import BeautifulSoup


def get_all_district_in_area(area_link):
    url = 'https://hz.lianjia.com/zufang/xihu/'
    r = requests.get(url, timeout=5)
    print("页响应状态码：", r.status_code)

    soup = BeautifulSoup(r.content, 'lxml')
    # soup = BeautifulSoup(r.content,'html.parser')
    district_tag = soup.find_all('div', {'class': 'option-list sub-option-list'})[0]
    a_list = district_tag.find_all('a')
    district_list = []
    for tag in a_list:
        district_list.append(tag.text)
    district_list.pop(0)
    print('当前区域的所有小区有 : ', district_list)
    return district_list

def click_district():
    button = '//*[@id="filter-options"]/dl[1]/dd/div[2]/a[2]'



if __name__ == '__main__':
    get_all_district_in_area(area_link=None)
