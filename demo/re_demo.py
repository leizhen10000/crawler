#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/1/4 16:48
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : re_demo.py
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
import re

line = 'Fat cats are smarter than dogs, is it right?'
m = re.match(r'(.*) are (.*?) dogs', line)
print(m.group(0))
print(m.groups())
print(re.findall(r'cats.ar.*', line))

html_content = '''
<bookstore>
<book>
<title lang="en">Harry Potter</title>
<author>J K. Rowling</author>
<year>2005</year>
<price>29,99</price>
</book>
</bookstore>
'''
