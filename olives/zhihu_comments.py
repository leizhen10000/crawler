#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/12/20 14:50
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : zhihu_comments.py
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
import json
import pprint
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def santostang_comments():
    """某个文章的评论"""
    url = "https://api-zero.livere.com/v1/comments/list?" \
          "callback=jQuery112404212889260650272_1513761728246&limit=10" \
          "&repSeq=3929772&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020" \
          "&livereSeq=28583&smartloginSeq=5154&_=1513761728248"
    # url = "https://zhuanlan.zhihu.com/api/posts/29645367/comments?limit=10&offset=0"
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/63.0.3239.84 Safari/537.36'
    }

    resp = requests.get(url, headers=headers)
    # print(json.dumps(json.loads(resp.content), sort_keys=True, indent=4, ensure_ascii=False))

    pp = pprint.PrettyPrinter(indent=4, depth=4, width=50)
    # pp.pprint(json.loads(resp.content))

    json_string = resp.text
    json_string = json_string[json_string.find(r'{'):-2]

    json_data = json.loads(json_string)
    # print(json.dumps(json_data, sort_keys=True, indent=4, ensure_ascii=False))

    comment_list = json_data['results']['parents']
    for comment in comment_list:
        message = comment['content']
        print('\n')
        print(message)

    # comment_list = json_data['re']


def relative_article():
    driver = webdriver.Chrome()
    driver.get(url='http://www.voidcn.com/article/p-xckaiwtn-dt.html')
    relatives = driver.find_element_by_css_selector('ul.relative_list')
    relative_list = relatives.find_elements_by_css_selector('li')
    for comment in relative_list:
        print(comment.text)
    driver.quit()


def movie_info():
    """获取豆瓣电影主要信息"""
    driver = webdriver.Chrome()
    url = 'https://movie.douban.com/subject/5350027/'
    driver.get(url)
    try:
        rate_ele = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="interest_sectl"]/div[1]/div[2]/strong'))
        )
        rate = rate_ele.text  # 豆瓣评分
        director_ele = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="info"]/span[1]/span[2]/a')
            )
        )
        director = director_ele.text  # 导演
        release_date = driver.find_element_by_xpath('//*[@id="info"]/span[12]').text

        with open('comment.txt', 'w', encoding='utf-8') as f:
            f.write('=============== 电影基本信息 ===============\n')
            f.write('电影《妖猫传》豆瓣评分：{}\n'.format(str(rate)))
            f.write('导演：{}\n'.format(director))
            f.write('上映时间：{}\n\n'.format(release_date))
            f.close()
    finally:
        driver.quit()


score_dict = {'力荐': '五星', '推荐': '四星',
              '还行': '三星', '较差': '二星',
              '很差': '一星', '无': '没有评分'}


def comments_with_driver():
    """获取豆瓣 电影影评"""
    driver = webdriver.Chrome()
    others = []
    try:
        driver.get(
            'https://movie.douban.com/subject/5350027/comments?status=P')
        _get_info_one_page(driver, others)
        for loop in range(0, 2):
            time.sleep(1)
            next_ele = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.LINK_TEXT, '后页 >'))
            )
            next_ele.click()
            _get_info_one_page(driver, others)

        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(others)

        # with open('comment.txt', 'w', encoding='utf-8') as f:
        #     f.writelines('========== 电影《妖猫传》影评 ==========\n')
        #     f.close()
        index = 0
        for info in others:
            write_txt('评论 {} '.format(str(index)), ':')
            write_txt('点评内容：', info['comment'])
            write_txt('点赞数量：{}'.format(info['loves']))
            write_txt('个人评分：', score_dict[info['score']])
            write_txt('评分时间：{}'.format(str(info['time'])), '\n')
            index += 1
    finally:
        driver.quit()


def _get_info_one_page(driver, others):
    """获取当前页面信息"""
    time.sleep(1)
    for i in range(0, 20):
        info = {}
        comment_ele = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="comments"]/div[' + str(i + 1) + ']/div/p')))
        comment = comment_ele.text  # 获取评论文本
        loves_ele = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 '//*[@id="comments"]/div[' + str(i + 1) + ']/div[2]/h3/span[1]/span')
            ))
        loves = loves_ele.text  # 获取点赞数文本

        item = driver.find_element_by_xpath(  # 部分用户没有评分数据
            '//*[@id="comments"]/div[' + str(i + 1) + ']/div[2]/h3/span[2]/span[2]'
        ).get_attribute('title')
        if item in score_dict.keys():
            info['score'] = item
            info['time'] = driver.find_element_by_xpath(
                '//*[@id="comments"]/div[' + str(i + 1) + ']/div[2]/h3/span[2]/span[3]'
            ).text  # 评论时间文本
        else:
            info['score'] = '无'
            info['time'] = ''
        info['comment'] = comment
        info['loves'] = loves
        others.append(info)


def write_txt(text1='', text2='', file_name='comment.txt'):
    text = '> {}{}\n'.format(text1, text2)
    with open(file_name, 'a', encoding='utf-8') as f:
        for char in text:
            f.writelines(char)
        f.close()


if __name__ == '__main__':
    # santostang_comments()
    # relative_article()
    movie_info()
    comments_with_driver()
