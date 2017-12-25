#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/12/14 19:36
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : own_contract.py
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


def get_own_contracts():
    """获取我的合同"""
    url = 'https://17dz.com/xqy-portal-web/manage/contract/getOwnContracts'
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/63.0.3239.84 Safari/537.36',
        'xsrf-token':
            '79695179DEFB459F9ED3F6DC910A5565',
        'Host':
            '17dz.com',
        'uc_session_id':
            'VwvAI4H2',
        'Referer':
            'https://17dz.com/manage/index.html?_1495188200'
    }
    cookies = {
        'CACHESESSIONID':
            '1C1ACL77L1O41168A8C0000002E3B63910',
        'xsrf-token':
            '79695179DEFB459F9ED3F6DC910A5565',
        'UM_distinctid':
            '16053e51c432cc-0e603942b9f35d-17386d57-1fa400-16053e51c44966'
    }
    params = {
        "pageNo": 1,
        "pageSize": "25",
        "nameOrNoLike": "",
        "orderName": "",
        "create": "",
        "signers": [],
        "customerManagers": [],
        "responsibles": [],
        "agreements": [],
        "deadlineStart": "",
        "deadlineEnd": "",
        "asc": ""
    }
    response = requests.post(
        url=url, headers=headers, cookies=cookies, params=params)
    print(response.status_code)
    print(response.text)


if __name__ == '__main__':
    get_own_contracts()
