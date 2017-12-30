#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2017/12/26 10:40
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : set_chrome_option.py
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
import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('lang=zh_CN.UTF-8')

# 最常见的场景是设置 user-argument 来模拟移动设备
# 比如下面模拟 iphone6
options.add_argument(
    'user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) '
    'AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 '
    'Mobile/13B143 Safari/601.1"')

# 禁止加载图片
prefs = {
    'profile.default_content_setting_values.images': 2
}
options.add_experimental_option('prefs', prefs)
options.add_extension('../source/extension_1_13_4.crx')
# options.set_headless()

driver = webdriver.Chrome(chrome_options=options)

urls = [
    'http://www.touxiangzhan.com/qinglvtouxiang/',
    'http://www.touxiangzhan.com/nanshengtouxiang/',
    'http://www.touxiangzhan.com/nvshengtouxiang/',
    'http://www.touxiangzhan.com/oumeitouxiang/',
    'http://www.touxiangzhan.com/daizitouxiang/',
    'http://www.touxiangzhan.com/katongtouxiang/',
    'http://www.touxiangzhan.com/gexingtouxiang/',
    'http://www.touxiangzhan.com/weixintouxiang/',
    'http://www.touxiangzhan.com/touxiang/',
    'http://www.touxiangzhan.com/qinglvtouxiang/daizi/',
    'http://www.touxiangzhan.com/qinglvtouxiang/katong/',
    'http://www.touxiangzhan.com/qinglvtouxiang/oumei/',
    'http://www.touxiangzhan.com/qinglvtouxiang/baqi/',
    'http://www.touxiangzhan.com/qinglvtouxiang/feizhuliu/',
    'http://www.touxiangzhan.com/qinglvtouxiang/yizuoyiyou/',
    'http://www.touxiangzhan.com/qinglvtouxiang/jiewen/',
    'http://www.touxiangzhan.com/qinglvtouxiang/weimei/',
    'http://www.touxiangzhan.com/qinglvtouxiang/heibai/',
    'http://www.touxiangzhan.com/qinglvtouxiang/haokan/',
    'http://www.touxiangzhan.com/qinglvtouxiang/xiaoqingxin/',
    'http://www.touxiangzhan.com/qinglvtouxiang/yinanyinv/',
    'http://www.touxiangzhan.com/qinglvtouxiang/keai/'
]
start_time = time.time()
for url in urls:
    try:
        driver.get(url)
    except Exception as e:
        print(e)
print('打开22个包含图片页面耗费时间 ', '%.2f' % (time.time() - start_time))

driver.quit()
