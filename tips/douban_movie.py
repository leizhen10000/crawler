#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/12/5 21:54
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : douban_movie.py
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


def get_movies():
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 '
        'Safari/537.36',
        'Host':
        'movie.douban.com'
    }
    movie_list, movie_en_list = [], []

    for i in range(0, 10):
        link = 'https://movie.douban.com/top250?start=' + str(i * 25)
        r = requests.get(url=link, headers=headers, timeout=10)
        print(str(i + 1), "页响应状态码：", r.status_code)

        soup = BeautifulSoup(r.text, 'lxml')
        div_list = soup.find_all('div', class_='hd')
        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)
    return movie_list, movie_en_list


if __name__ == '__main__':
    movies = get_movies()
    print(movies)
