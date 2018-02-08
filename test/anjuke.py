#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/1/4 18:49
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : anjuke.py
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
import re

import pymysql
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


def get_html_content():
    url = 'https://hangzhou.anjuke.com/sale/'
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/62.0.3202.94 Safari/537.36',
        'Referer':
            'https://movie.douban.com/subject/26363254/celebrities'
    }
    session = requests.Session()
    session.max_redirects = 60
    resp = session.get(url=url, headers=headers)
    return BeautifulSoup(resp.text, 'html.parser')


def extract_detail(soup):
    house_details = soup.find_all('div', class_='house-details')
    detail_list = []
    for house_detail in house_details:
        detail = {}
        # 标题
        title = house_detail.find('div', class_='house-title') \
            .text.strip().replace('\n', '')
        detail['title'] = title
        # 户型,面积，楼层，建造时间
        house_params = house_detail.find('div', class_='details-item') \
            .text.strip().split('|')
        detail['house_type'] = house_params[0]
        detail['size'] = house_params[1]
        detail['floor'] = house_params[2]
        detail['build_time'] = re.match(r'^(.*)建造', house_params[3]).group()
        # 详细地址
        address = house_detail.find('span', class_='comm-address') \
            .text.strip().split('\n')
        detail['address'] = address[0].strip()
        detail['address_detail'] = address[1].strip()
        # 标签
        detail['tags'] = house_detail.find('div', class_='tags-bottom').text.strip()
        detail_list.append(detail)
    return detail_list


def write_into_txt(house_details):
    with open('result_data/anjuke.txt', 'w', encoding='utf-8') as f:
        for detail in house_details:
            f.writelines('>>>>>>>>>>> 房源 >>>>>>>>>>>\n')
            f.writelines('标   题：' + detail['title'])
            f.writelines('\n户   型：' + detail['house_type'])
            f.writelines('\n面   积：' + detail['size'])
            f.writelines('\n楼   层：' + detail['floor'])
            f.writelines('\n建造时间：' + detail['build_time'])
            f.writelines('\n地   址：' + detail['address'])
            f.writelines('\n详细地址：' + detail['address_detail'])
            f.writelines('\n标   签：' + detail['tags'])
            f.writelines('\n\n')
    f.close()


def write_into_mysql(house_details):
    print('连接本地 mysql 服务...')
    connect = pymysql.connect(host='localhost', user='root', password='root', charset='utf8')
    try:
        with connect.cursor() as cursor:
            sql = "INSERT INTO mybatis.anjuku_house (title, type, size, build_time, high, address, tag) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s)"
            for detail in house_details:
                cursor.execute(sql,
                               (detail['title'], detail['house_type'], detail['size'],
                                detail['build_time'], detail['floor'], detail['address_detail'],
                                detail['tags']))
        connect.commit()
        with connect.cursor() as cursor:
            sql = "select * from mybatis.anjuku_house"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
    finally:
        connect.close()


def write_into_mongodb(house_details):
    print('连接本地 mongodb 服务...')
    # 连接有两种方式，一个是键值对配置，另一个是通过传入命令连接
    connection = MongoClient('localhost', 27017)
    connection = MongoClient('mongodb://localhost:27017/')



if __name__ == '__main__':
    html_soup = get_html_content()
    house_info = extract_detail(html_soup)
    # write_into_txt(house_info)
    write_into_mysql(house_info)
