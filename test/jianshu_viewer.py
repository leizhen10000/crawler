#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/12/21 19:20
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : jianshu_viewer.py
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


def jianshu_viewer():
    url = 'http://www.jianshu.com/u/987d66f618ee'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    # 获取作者的所有文章
    note_list = soup.find_all('div', class_='content')
    view_detail = {}
    for note in note_list:
        title = note.select('[class~=title]')[0].text.encode('utf-8')
        viewers = note.find(
            'i', class_='iconfont ic-list-read').parent.text.strip()
        view_detail[title] = viewers

    print(view_detail)

    with open('jianshu.txt', 'w', encoding='utf-8') as f:  #这里有 python 中文编码问题
        for article in view_detail:
            detail = '标题 ：{} \n访问量 : {}\n\n'.format(
                article.decode('utf-8'), str(view_detail[article]))
            f.write(detail)
        f.close()


if __name__ == '__main__':
    jianshu_viewer()
