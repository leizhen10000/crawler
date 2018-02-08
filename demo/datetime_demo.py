#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/12/30 09:09
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : datetime_demo.py
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
import datetime
import time

one_day = datetime.timedelta(days=1, seconds=19999.0, microseconds=123124124)
days = one_day.days
seconds = one_day.seconds
microseconds = one_day.microseconds
print(days, seconds, microseconds)
print(one_day)

t1 = one_day * 5 + datetime.timedelta(hours=9, minutes=19, seconds=6.8)
print(t1)
print(t1 // one_day)
print(t1 % one_day)
# 上面返回一个是整数，另一个是求余
# 下面的方法直接返回两个值
q, r = divmod(t1, one_day)
print(q, r)

t2 = datetime.timedelta(days=1)
print(-t2)
# 返回 datetime.timedelta(1) 格式
print(repr(t2))

print(t1.max)
print(t1.min)

# examples
year = datetime.timedelta(days=365)
another_year = datetime.timedelta(weeks=40, days=84, hours=23,
                                  minutes=50, seconds=600)
ten_years = 10 * year
print(ten_years, ten_years.days // 365)
nine_years = ten_years - year
print(nine_years, nine_years.days // 365)

# 获取昨天的时间
one_day = datetime.timedelta(days=1)
# 今天
today = datetime.date.today()
print('今天', today)
# 昨天
yesterday = today - one_day
print('昨天', yesterday)
# 明天
tomorrow = today + one_day
print('明天', tomorrow)
# 获取今天零点的时间
today_zero_time = datetime.datetime.strftime(
    today, '%Y-%m-%d %H:%M:%S')
print('零点时间', today_zero_time, '类型', type(today))
# 字符串时间转换成时间戳
d = datetime.datetime.strptime(today_zero_time, '%Y-%m-%d %H:%M:%S')
time_sec_float = time.mktime(d.timetuple())
print('时间戳', time_sec_float)
# 时间戳再转换成字符串
date_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_sec_float))
print('字符串', date_str)

# 获取上个月最后一天
last_month_last_day = datetime.datetime(
    datetime.datetime.today().year, datetime.datetime.today().month, 1
) - datetime.timedelta(1)
print('上月的最后一天', last_month_last_day)
