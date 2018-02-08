#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/1/10 19:37
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : handel_data.py
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
import pymysql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def connect_mysql():
    connect = pymysql.connect(host='10.139.154.114', port=3307, user='zcm_only_read',
                              password='zw5hV0oV6Anujz3P', db='zcm', charset='utf8')
    try:
        # 统计月激活用户量
        active_monthly_sql = ("SELECT "
                              "DATE_FORMAT(create_time, '%Y年%m月') 月份,"
                              "COUNT(DISTINCT (id))               激活 "
                              "FROM platform_imei "
                              "WHERE create_time IS NOT NULL "
                              "AND create_time "
                              "  BETWEEN date_add(CURDATE(), INTERVAL -5 MONTH) "
                              "  AND date_add(CURDATE(), INTERVAL -1 DAY) "
                              "GROUP BY 月份")
        active_query = pd.read_sql(sql=active_monthly_sql, con=connect)
        # 统计月注册用户量
        register_monthly_sql = None
        active_query.plot()
        plt.show()
        print(active_query)

    finally:
        connect.close()


if __name__ == '__main__':
    connect_mysql()
