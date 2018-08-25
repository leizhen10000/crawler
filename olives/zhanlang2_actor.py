#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/12/6 19:23
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : zhanlang2_actor.py
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
import re
import urllib.request

import requests
from bs4 import BeautifulSoup


def zhanlang2_actors():
    """获取战狼2所有演员图片"""
    soup = _actors_detail()
    _retrieve_photo(soup)


def _actors_detail():
    """根据url获取所有演员html内容"""
    url = 'https://movie.douban.com/subject/26363254/celebrities'
    # 定义 header，模拟浏览器向服务器发起请求
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/62.0.3202.94 Safari/537.36',
        'Referer':
            'https://movie.douban.com/subject/26363254/celebrities'
    }
    r = requests.get(url, headers=headers)
    if r.status_code != 200:  # 如果返回结果不为200，则抛出异常
        raise r.raise_for_status()
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def _retrieve_photo(soup):
    """根据 html 提取演员的图片"""
    movie = soup.head.title.string.split(' ')[0]
    tags = soup.find_all('div', class_='list-wrapper')

    stars = []  # 存放演员信息
    for tag in tags[1].find_all('li'):
        # 获取演员名称
        title = tag.a['title'].split(' ')[0]
        # 正则匹配图片链接地址
        img_url = re.findall(r'https://img\d.doubanio.com/view/celebrity/'
                             r's_ratio_celebrity/public/p.*.jpg', str(tag))
        if len(img_url) != 0:  # 有一个演员没有提供照片
            stars.append([title, img_url[0]])

    # 将所有演员图片存入某个文件夹底下，并且以演员名称命名文件
    if not os.path.exists(movie):
        os.mkdir(movie)
    for star in stars:
        filename = os.path.join(movie, star[0] + '.jpg')
        # 通过 url 地址提取图片
        # 有时候提取的内容为空，可能是没有权限headers或者sessions，需自行添加
        urllib.request.urlretrieve(star[1], filename=filename)


def zhanlang2_actors_with_urllib():
    """通过 urllib 工具获取演员信息"""
    pass


def zhanlang2_others():
    """战狼其他信息：导演、主演、上映年份、电影分类、评分"""
    soup = _others_detail()
    _extract_others(soup)


def _others_detail():
    """获取电影战狼2其他信息"""
    url = 'https://movie.douban.com/subject/26363254/'
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/63.0.3239.84 Safari/537.36'
    }
    resp = requests.get(url=url, headers=headers)
    if resp.status_code != 200:
        raise resp.raise_for_status()
    return BeautifulSoup(resp.content, 'html.parser')


def _extract_others(soup):
    # all_detail = soup.find_all('div', class_='subject clearfix')
    all_info = soup.find('div', id='info')
    role_list = ['导演', '主演', '类型', '上映日期', '评分']
    others = {}  # 所有信息dict
    span_list = all_info.find_all('span')
    for tag in span_list:
        if role_list[0] in tag.text:  # 获取导演信息
            role_key_value = tag.text.split(':')
            role = role_key_value[0]
            if tag.span is not None:
                # 有的span只是链接的文字标示，不包含名称
                others[role] = role_key_value[1]
        if role_list[1] in tag.text:  # 获取主演信息
            key_value = tag.text.split(':')
            role = key_value[0]
            if tag.span is not None:
                others[role] = key_value[1]

    span_list = all_info.find_all('span', class_='pl')  # 获取类型标签
    for tag in span_list:
        if role_list[2] in tag.text:  # 电影类型
            next_tag_font = tag.find_next_siblings('span')[0].text
            others[role_list[2]] = next_tag_font
        if role_list[3] in tag.text:  # 上映时间
            next_tag_font = tag.find_next_siblings('span')[0].text
            print(next_tag_font)
            others[role_list[3]] = next_tag_font.split(r'(')[0]

    grade_str = soup.find('div', class_='rating_self clearfix').text.strip()  # 评分
    match = re.match(r'[\d.]+', grade_str)
    others[role_list[4]] = match.group()

    with open('others.txt', 'w', encoding='utf-8') as f:
        for key in others:
            aa = others[key]
            bb = '{}:{}\n'.format(key, others[key])
            f.write(bb)


if __name__ == '__main__':
    # zhanlang2_actors()
    zhanlang2_others()
    # 获取方法的注解
    print(zhanlang2_others.__doc__)
    # 获取方法注解为str
    print(repr(zhanlang2_others.__doc__))
