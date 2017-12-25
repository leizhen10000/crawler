#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/12/13 15:30
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : urllib_util.py
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
import os
import urllib.request
import http.cookiejar

import requests


def download_image():
    file_name = os.path.join('吴京.jpg')
    with open(file_name, 'w') as f:
        urllib.request.urlretrieve(
            'https://img1.doubanio.com/view/celebrity/s_ratio_celebrity/public/p58967.webp'
        )


def url_open():
    # 设置头
    header = [(
        'User-Agent',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/57.0.2987.133 Safari/537.36'
    )]

    # 设置代理
    proxy_handler = urllib.request.ProxyHandler({'http': '127.0.0.1:1087'})

    # 设置 cookie
    cookie = http.cookiejar.MozillaCookieJar()
    cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

    opener = urllib.request.build_opener(proxy_handler, cookie_handler)
    # opener.addheaders = header
    # 设置 opener 对象作为 url open（）使用的全局 opener
    urllib.request.install_opener(opener)

    url = 'http://www.google.com'
    response = urllib.request.urlopen(url=url)
    # print(response.read())
    print(response.geturl())
    print(response.info())
    print(response.getcode())
    for item in cookie:
        print('name = ', item.name)
        print('value = ', item.value)
    cookie.save(filename='cookie.txt', ignore_discard=True, ignore_expires=True)

    keyword = '哈哈'
    kw = urllib.request.quote(keyword)
    url = 'http://www.baidu.com/s?is=UTF-8&wd=' + kw
    response = urllib.request.urlopen(url)
    buff = response.read()
    html = buff.decode('utf8')
    response.close()
    # print(html)


def url_open_with_requests():
    proxies = {
        'http': 'http://127.0.0.1:1087',
        'https': 'https://127.0.0.1:1087'
    }
    r = requests.get('http://www.google.com', proxies=proxies)
    print(r.text)
    print(r.status_code)


def free_proxy():
    proxies = {
        'http': 'http://116.199.115.79:80',
        'https': 'https://209.126.102.151:8888'
    }
    r = requests.get('http://www.baidu.com', proxies=proxies)
    print(r.text)
    print(r.status_code)


if __name__ == '__main__':
    # download_image()
    url_open()
    # url_open_with_requests()
    # free_proxy()
