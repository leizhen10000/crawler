#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/8/13 18:34
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : machine_trading.py
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
import tushare as ts

QUOTES_CODE = '518880'


def get_current_price():
    """获取该股实时价格"""
    real_time_quotes = ts.get_realtime_quotes(QUOTES_CODE)
    df = real_time_quotes[['code', 'name', 'price', 'time']]

    real_time = df['time'][0]
    price = float(real_time_quotes['price'][0])

    print("r  > 当前时间 {time}, 价格为 {price}".format(time=real_time, price=price))


def set_price_range():
    """
    设置价格区间
    :return:    返回最大值即可
    """
    # 调用 模型接口，获取价格区间
    # todo(leizhen 2018/08/13) 模型的接口需要单独设计
    high_price = None
    return high_price


def get_today_max_price():
    """
    获取当天最大价格

    每隔一分钟获取一次，防止获取实时价格2s间隔中出现最大价格
    :return:
    """
    # todo(leizhen 2018/08/13) 需要商定获取间隔，接口获取时间较长，且容易出差
    try:
        today_ticks = ts.get_today_ticks(QUOTES_CODE, retry_count=5, pause=0.5)
        max_price = today_ticks['price'].max()
        # todo: leizhen 2018/08/13 需要确定保留小数到多少位，否则会出现精度缺失
        print("今日历史最大价格为 %s" % max_price)
        return max_price
    except IOError:
        print("查询最大价格失败，请10s后继续查询")


if __name__ == '__main__':
    # get_current_price()
    get_today_max_price()
