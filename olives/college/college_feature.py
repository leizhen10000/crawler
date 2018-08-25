#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/17 10:43
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : college_feature.py
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
import time

import pymysql
import requests
from bs4 import BeautifulSoup


class CollegeFeatureSpider():

    def get_html_content(self, real_url):

        headers = {
            'User-Agent':
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/62.0.3202.94 Safari/537.36',
        }

        proxies = {
            'http': 'http://39.137.77.66:8080',
            'https': 'https://127.0.0.1:1087'
        }

        session = requests.Session()
        session.max_redirects = 60
        resp = session.get(url=real_url, headers=headers, proxies=proxies)
        soup = BeautifulSoup(resp.text, 'html5lib')
        resp.raise_for_status()

        all_college = soup.findAll('table', class_='ch-table')[0]

        details = all_college.select("tr")
        college_info_list = []
        for college_info in details[1:]:
            college_name = college_info.select("td.js-yxk-yxmc")[0].text.strip()
            academic_level = college_info.select("td:nth-of-type(5)")[0].text.strip()
            college_features = college_info.select("td.ch-table-center")[0].text
            college_feature_list = re.findall('\w+', college_features)

            college_info_pair = {'name': college_name, 'level': academic_level,
                                 'feature': self.charge_feature(college_feature_list)}

            college_info_list.append(college_info_pair)

        self.write2_mysql(college_info_list)

    def charge_feature(self, college_feature_list):
        """根据院校特性，返回数据库特定值"""
        is211 = '211' in college_feature_list
        is985 = '985' in college_feature_list
        college_feature = 0  # 默认为0
        if is211 and is985:
            college_feature = 3
        elif is211:
            college_feature = 1
        elif is985:
            college_feature = 2

        return college_feature

    @staticmethod
    def write2_mysql(college_info_list):
        connect = pymysql.connect(host='localhost', user='root', password='root', charset='utf8')
        try:
            with connect.cursor() as cursor:
                sql = "INSERT INTO mybatis.college (name, level, feature) VALUES (%s, %s, %s)"
                for college_info in college_info_list:
                    cursor.execute(sql,
                                   (college_info['name'], college_info['level'], str(college_info['feature'])))
                    if connect.commit():
                        print('学校{} 信息写入成功'.format(college_info['name']))
        except Exception as e:
            raise Exception('添加数据入库报错，请重新检查')
            raise e
        finally:
            connect.close()


if __name__ == '__main__':
    url_list = ["http://gaokao.chsi.com.cn/sch/search.do?searchType=1&yxmc=&zymc=&sySsdm=&ssdm=&yxls=&yxlx=&xlcc="]
    for i in range(0, 134):
        index = str(20 * (i + 1))
        start_url = "http://gaokao.chsi.com.cn/sch/search.do?searchType=1&start=%s" % index
        url_list.append(start_url)

    for url in url_list:
        time.sleep(1)
        CollegeFeatureSpider().get_html_content(url)
