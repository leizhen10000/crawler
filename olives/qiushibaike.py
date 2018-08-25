#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/12/14 21:02
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : qiushibaike.py
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

import requests
from bs4 import BeautifulSoup


def qiushibaike():
    """糗事百科页面内容"""
    url = 'http://www.qiushibaike.com/hot/page/1'
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/63.0.3239.84 Safari/537.3',
        # 'Host': 'qa.qiushibaike.com',
        # 'Origin': 'https://www.qiushibaike.com',
    }
    proxies = {
        'http': 'http://182.88.131.28:9797',
        'https': 'https://113.221.45.248:8888'
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        raise resp.raise_for_status()

    # proxy = 'http://116.226.124.226:9000'
    # proxy_support = urllib.request.ProxyHandler({'http': proxy})
    # opener = urllib.request.build_opener(proxy_support)
    # urllib.request.install_opener(opener)
    # request = urllib.request.Request(url, headers=headers)
    # html = urllib.request.urlopen(request)
    # resp = html.read().decode()

    # 获取发布人，发布日期，段子内容，以及点赞的个数
    soup = BeautifulSoup(resp.text, 'html.parser')
    # qiubai = soup.body.find_all('div', class_='col1')
    # qiubai = soup.body.find_all('div', {'class': 'col1'})
    # qiubai = soup.body.find_all('div', {'id': 'content-left'})
    # qiubai = soup.body.find_all('div', id='content-left')
    # qiubai_title = soup.body.find_all('div', class_='author clearfix')
    # qiubai_title = soup.body.select('#content-left')
    # qiubai_title = soup.body.select('[class~=author]')
    pattern = re.compile(r'article block untagged mb15')
    aaa = soup.body.text
    qiubai = soup.body.find_all('div', pattern)

    user_list = []

    for one_qiubai in qiubai:
        title_tag = one_qiubai.find('div', class_='author clearfix')
        stats_tag = one_qiubai.find('div', class_='stats')
        content = one_qiubai.find('a', class_='contentHerf')
        user_info = title_tag.find_all('a')
        user = {}
        if len(user_info) > 1:
            # 用户姓名
            user['name'] = user_info[1].h2.text.strip('\n')
            # 用户性别
            gender_class = title_tag.div['class'][1]
            if 'women' in gender_class:
                user['gender'] = '女'
            else:
                user['gender'] = '男'
            # 等级
            level = title_tag.div.text
            user['level'] = level
            # 点赞数
            likes = stats_tag.span.i.text
            user['likes'] = likes
            # 段子内容（如果包含图片，则跳过）
            if content.span is not None:
                user['content'] = content.span.text
            user_list.append(user)

    with open('qiubai.txt', 'w', encoding='utf-8') as f:
        for user in user_list:
            f.write('\n用户姓名：\t{}'.format(user['name']))
            f.write('\n用户性别：\t{}'.format(user['gender']))
            f.write('\n用户等级：\t{}'.format(user['level']))
            f.write('\n点赞数量：\t{}'.format(user['likes']))
            f.write('\n段子内容：\t{}'.format(user['content']))


class QiushiBaike:
    def __init__(self):
        self.page_index = 1
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) ' \
                          'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                          'Chrome/63.0.3239.84 Safari/537.36'
        self.headers = {'User-Agent': self.user_agent}
        self.stories = []
        self.enable = False

    def get_page(self, page_index):
        """获取页面html内容"""
        url = 'https://www.qiushibaike.com/hot/page/' + str(page_index)
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            raise response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')


if __name__ == '__main__':
    # QiushiBaike().get_page(1)
    qiushibaike()
