#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/8/11 13:17
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : swsindex_code.py
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
import calendar
import datetime
import json
import random
import re
import time

import pymysql
import requests


def get_recent_data():
    # 根据不同的年份-月份获取数据
    year_list = [2019]
    month_list = [10]
    for year in year_list:
        for month in month_list:
            print("当前月份为", year, month)

            # 首先初始化页面，获得session
            year, month = int(year), int(month)
            session, count = init_page(int(year), int(month))

            # 查询该月份数据，分为月份查询，较方便
            data_list = get_data_by_month(session, count, year, month)

            # 解析并将数据写入数据库
            parse_result = parse_data(data=data_list)
            write_into_mysql(index_data=parse_result)

            session.close()

            print(f"当前查询月份{month}结束")
            # print("等待200s")
            # time.sleep(200)
        break
        print("跨过年份，等待10分钟")
        time.sleep(600)


def _cal_month_day(year, month):
    """
    计算固定月份的初始日期
    :param year:    年份
    :param month:   月份
    :return: 开始日期，结束日期
    """
    year, month = int(year), int(month)
    month_range = calendar.monthrange(year, month)[1]
    first = str(datetime.date(year=year, month=month, day=1))
    end = str(datetime.date(year=year, month=month, day=month_range))
    return first, end


def get_data_by_month(session, count, year, month):
    """
    获取固定月份数据
    :param session:     包含初始化session_id
    :param count:       总计数量，用于计算分页
    :param year:        查询年份
    :param month:       查询月份
    :return:            查询结果<list>
    """
    cur_datetime = int(time.time() * 1000)

    first, end = _cal_month_day(year, month)

    url = 'http://www.swsindex.com/handler.aspx'
    cookies = session.cookies.get('ASP.NET_SessionId')
    headers = {
        'Referer': 'http://www.swsindex.com/idx0200.aspx?columnid=8838&type=Day',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'ASP.NET_SessionId={}'.format(cookies),
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/62.0.3202.94 Safari/537.36',
    }

    root_list = []
    for p in range((count + 20) // 20):
        p += 1
        data = {
            'tablename': 'V_Report',
            'key': 'id',
            'p': str(p),
            'where': "swindexcode in ('801010','801020','801030','801040','801050',"
                     "'801060','801070','801080','801090','801100','801110','801120',"
                     "'801130','801140','801150','801160','801170','801180','801190',"
                     "'801200','801210','801220','801230','801710','801720','801730',"
                     "'801740','801750','801760','801770','801780','801790','801880',"
                     "'801890') "
                     "and  BargainDate>='{first_date}' and  BargainDate<='{end_date}' "
                     "and type='Day'".format(first_date=first, end_date=end),
            'orderby': 'swindexcode asc,BargainDate_1',
            'fieldlist': 'SwIndexCode,SwIndexName,BargainDate,'
                         'PE,PB',
            'pagecount': count,
            'timed': cur_datetime}
        resp = session.post(url=url, headers=headers, data=data)
        time.sleep(2 * random.random())
        print("稍等1s")
        resp_json = json.loads(resp.text.replace('\'', '\"'))
        root_list.extend(resp_json['root'])
    return root_list


def parse_data(data):
    """
    解析固定格式数据

    目前查询的为四列数据，如果要添加列数，除了数据库添加，这里也要做改动
    :param data:    查询数据结果
    :return         格式化成数据库插入的结构 [[],[],[]..]
    """
    result = []
    for item in data:
        result.append([item['SwIndexCode'], item['SwIndexName'], item['BargainDate'],
                       item['PE'], item['PB']])
    return result


def write_into_mysql(index_data):
    """
    将指标写入数据库
    :param index_data:
    :return:
    """
    print('连接本地 mysql 服务...')
    connect = pymysql.connect(
        host='192.168.1.61', user='xingyuer', password='lQ*foSwLofxs', port=3318, db='financial', charset='utf8')
    try:
        sql = ("insert ignore into swsindex_daily_report "
               " (index_code, index_name, bargain_date, pe_ratio, pb_ratio) "
               " values(%s, %s, %s, %s, %s)")
        with connect.cursor() as cursor:
            cursor.executemany(sql, index_data)
            connect.commit()

        with connect.cursor() as cursor:
            sql = "select * from swsindex_daily_report"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
    finally:
        connect.close()
        print("插入数据完毕")
        print("关闭 mysql 连接...")


def init_page(year, month):
    first, end = _cal_month_day(year, month)
    pre_url = 'http://www.swsindex.com/ajaxpro/Idx0200,App_Web_hhibvfoy.ashx'
    pre_headers = {
        'X-AjaxPro-Method': 'ReturnPageCount',
        'Origin': 'http://www.swsindex.com',
        'Content-Type': 'text/plain; charset=UTF-8',
        'Referer': 'http://www.swsindex.com/idx0200.aspx?columnid=8838&type=Day',
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/62.0.3202.94 Safari/537.36',
    }
    pre_body = {
        "table": "V_Report",
        "where": "  swindexcode in ('801010','801020','801030','801040',"
                 "'801050','801060','801070','801080','801090','801100',"
                 "'801110','801120','801130','801140','801150','801160',"
                 "'801170','801180','801190','801200','801210','801220',"
                 "'801230','801710','801720','801730','801740','801750',"
                 "'801760','801770','801780','801790','801880','801890') "
                 "and  BargainDate>='{first_day}' and  BargainDate<='{end_day}'"
                 " and type='Day'".format(first_day=first, end_day=end)}
    session = requests.Session()
    resp = session.post(
        url=pre_url, headers=pre_headers, data=json.dumps(pre_body))
    count = int(re.findall('\d+', resp.text)[0])
    return session, count


if __name__ == '__main__':
    get_recent_data()
