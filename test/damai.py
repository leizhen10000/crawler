#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/3/13 11:20
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : damai.py
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
import email
import smtplib
import time
from datetime import datetime
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests


def get_html_content():
    url = 'https://piao.damai.cn/ajax/getPriceList.html'
    # headers = {
    #     'User-Agent':
    #         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) '
    #         'AppleWebKit/537.36 (KHTML, like Gecko) '
    #         'Chrome/62.0.3202.94 Safari/537.36',
    #     'Referer':
    #         'https://movie.douban.com/subject/26363254/celebrities'
    # }
    params = {'projectId': 142859, 'performId': 9027509, 't': 0.8487496491197795}
    session = requests.Session()
    session.max_redirects = 60
    resp = session.get(url=url, params=params)
    print('获取的响应状态为 : ', resp.status_code)
    resp.raise_for_status()
    resp_json = resp.json()
    price_list = resp_json['Data']['list']
    has_ticket = False
    for price in price_list:
        if price['Status'] == 0:
            print('妈的邮票了！！！')
            print('票价为: ', price['PriceName'])
            has_ticket = True
            send_email()
    if not has_ticket:
        print('就是不给你票')


def send_email():
    # 发件人地址
    sender = 'lz@zcmlc.com'
    # 发件人密码
    password = 'Yg123456'
    # 自定义回复地址
    reply_to = ''
    # 收件人地址，支持多个收件人，最多30个
    receivers = ['lz@zcmlc.com', '979638485@qq.com', 'mayp@yusys.com.cn',
                 'leizhen8080@foxmail.com'
                 ]

    # 构建 alternative 结构
    message = MIMEMultipart('alternative')
    message['Subject'] = Header('发送给阿鹏的抢票提醒', 'utf-8')
    message['From'] = Header('雷圳', 'utf-8')
    message['To'] = Header('马云鹏', 'utf-8')
    message['Reply-to'] = reply_to
    message['Message-id'] = email.utils.make_msgid()
    message['Date'] = email.utils.formatdate()

    # 构建 alternative 的 text/plain 部分
    # 三个参数：第一个为文本内容，第二 plain 设置文本格式，第三个 utf-8 设置编码
    text_plain = MIMEText('大麦网 dota2 邮票提醒', 'plain', 'utf-8')
    message.attach(text_plain)

    # 构建 alternative 的 text/html 部分
    html_msg = """
    <p>有票了，赶紧来抢吧...</p>
    <p><a href="https://piao.damai.cn/142859.html">直达抢票网页</a></p>
    """
    text_html = MIMEText(html_msg, 'html', 'utf-8')
    message.attach(text_html)

    try:
        # client = smtplib.SMTP_SSL()
        client = smtplib.SMTP()
        # SMTP 普通端口为25或80
        client.connect('smtp.mxhichina.com', 25)
        # 开启 DEBUG 模式
        client.set_debuglevel(0)
        # 登陆
        client.login(sender, password)
        # 发送邮件
        client.sendmail(sender, receivers, message.as_string())
        # 退出
        client.quit()
        print('邮件发送成功')
    except smtplib.SMTPConnectError as e:
        print('邮件发送失败，连接失败:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPAuthenticationError as e:
        print('邮件发送失败，认证错误:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPSenderRefused as e:
        print('邮件发送失败，发件人被拒绝:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPRecipientsRefused as e:
        print('邮件发送失败，收件人被拒绝')
    except smtplib.SMTPDataError as e:
        print('邮件发送失败，数据接收拒绝:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPException as e:
        print('邮件发送失败')
    except Exception as e:
        print('邮件发送异常, ', str(e))


def timer(n):
    while True:
        get_html_content()
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(n)


if __name__ == '__main__':
    timer(90)
