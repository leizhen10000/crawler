#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/8/27 09:04
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : moving_between_windows_and_frames.py
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


class MoveBetweenWindow:
    def __init__(self):
        self.driver = webdriver.Firefox()

    # 现代的web应用程序很少没有frams或者只有一个单一的窗口
    # WebDriver 提供了在不同的windows中切换的方法
    # driver.switch_to_window("windowName")

    # 这样一来，所有的矿口都会跟 driver 一一对应
    # 但是如何确定窗口的名称呢？可以通过查看js或者打开窗口的链接
    # <a href="somewhere.html" target="windowName">Click here</a>

    # 另外，还可以通过传送一个 window handle 给 "switch_to.window()" 方法
    # 根据这个方法，就可以获取所有的已打开窗口
    def open_all_windows(self):
        driver = self.driver
        driver.get("http://www.ctrip.com/")

        products = driver.find_elements_by_class_name("product-item")
        products[0].click()
        time.sleep(2)

        for handle in driver.window_handles:
            time.sleep(1)
            driver.switch_to.window(handle)

        driver.quit()

    # 同样可以从 frame 到 frame 切换 todo: 暂时不知道frame是什么
    # driver.switch_to.frame("frameName")
    # 对于 subframe，可以通过 . 的形式访问到，也可以通过 序号index 访问
    # driver.switch_to.frame("frameName.0.child")
    # 这将爱过你会访问第一个名称为"child"的frame
    #
    # 一旦操作完成，需要返回父级内容
    # driver.switch_to.default_content()

    # Selenium WebDriver 提供了一个内置的服务，专用处理弹出对话框 popup dialog boxes
    # 一旦你出发了打开弹窗的动作，你可以通过下面的方法，切换到对话框上
    # alert = driver.switch_to.alert()

    # WebDriver 有很多小型的、关注于任务的接口，比如导航相关的任务接口就相当有用
    # 你可以前进和后退，访问历史记录
    # driver.forward()
    # driver.back()
    # 注意：这里完全依赖于当前的浏览器驱动，如果在不同的driver对象上操作，很有可能抛出异常


if __name__ == '__main__':
    MoveBetweenWindow().open_all_windows()
