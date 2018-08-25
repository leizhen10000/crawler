#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/12/1 18:10
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : use_requests.py
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


def get_page_text():
    link = 'http://www.santostang.com/'
    r = requests.get(
        link,
        headers={
            "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36"
        })

    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.title)
    print(soup.title.name)
    print(soup.title.string)
    print(soup.title.parent.name)
    print(soup.p)
    print(soup.a)
    print(soup.find_all('a'))

    for link in soup.find_all('a'):
        print(link.get('href'))

    css_soup = BeautifulSoup('<p class="body"></p>')


if __name__ == '__main__':
    get_page_text()
