#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/12/14 15:47
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : exception_in_requests.py
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
import urllib.request


def simple_exception():
    """简单抛出异常"""
    try:
        request = urllib.request.Request('http://wwwq.nothing.com')
        urllib.request.urlopen(request)
    except urllib.request.URLError as e:
        print('错误原因', e.reason)
        print(e.args)
    # 简单的HTTPError
    try:
        req = urllib.request.Request('http://blog.csdn.net/cqcre')
        urllib.request.urlopen(req)
    except urllib.request.HTTPError as e:
        print(e.code)
        print(e.reason)
    except urllib.request.URLError as e:
        print(e.reason)
    else:
        print('OK')


if __name__ == '__main__':
    simple_exception()
    print(repr(simple_exception.__doc__))
