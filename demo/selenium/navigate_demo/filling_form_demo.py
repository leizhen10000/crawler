#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2018/8/26 20:27
# @Author  : Lei Zhen
# @Contract: leizhen8080@gmail.com
# @File    : filling_form_demo.py
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
# 前面已经讲了，怎么在 textarea or test field 中输入文本，但是其他元素
# 比如下拉选择框
# 你可以切换下拉列表的状态，然后使用 "useSelected" 来选中可选项
# element = driver.find_element_by_xpath("//select[@name='name']")
# all_options = element.find_elements_by_tag_name("option")
# for option in all_options:
#     print("Value is : %s" % option.get_attribute("value"))
#     option.click()
#
#
from selenium import webdriver
from selenium.webdriver.support.select import Select


class CTripForm:

    def __init__(self):
        self.driver = webdriver.Firefox()

    def get_drop_down(self):
        driver = self.driver
        driver.get("http://www.ctrip.com/")

        # 这将会找到第一个 SELECT 元素，然后循环每隔 OPTIONs，打印option内容，并选中
        element = driver.find_element_by_id("J_roomCountList")
        all_options = element.find_elements_by_tag_name("option")
        for option in all_options:
            print("Value is : %s" % option.get_attribute("value"))
            option.click()
        driver.quit()

        # 但是，这并不是最有效的方式来处理 SELECT 元素

    # WebDriver 类包含 Select 方法，能提供有用的交互
    def get_select(self):
        driver = self.driver
        driver.get("http://www.ctrip.com/")

        select = Select(driver.find_element_by_id("J_roomCountList"))
        # 选中下拉内容的三种方式
        select.select_by_index(2)
        select.select_by_visible_text("2间")
        select.select_by_value('4')
        driver.quit()

    # WebDriver 同样提供了多种反选方式
    # 跟上面三个方法一一对应
    # 还提供了另一个方法
    # select= Select(driver.find_element_by_id('id'))
    # select.deselect_all()

    # 假设在测试环境中，我们需要列出所有的默认可选项
    # Select 类提供了一个合适的方法，返回所有的内容

    # //*[@id="J_RoomGuestInfoTxt"]
    def get_select_guest_num(self):
        driver = self.driver
        driver.get("http://www.ctrip.com/")

        # //*[@id="searchHotelLevelSelect"]
        select = Select(driver.find_element_by_xpath('//select[@id="searchHotelLevelSelect"]'))
        # 获取所有已选项
        all_selected_options = select.all_selected_options
        # 获取所有可选项
        options = select.options

        driver.close()

    # 一旦完成了form的填充，你可能需要马上提交
    # 有一种方式可以发现 "submit" 按钮，并且点击
    # Assume the button has the ID "submit"
    # driver.find_element_by_id("submit").click()
    # 另外，WebDriver 非常方便的方法"submit"，每一个元素都可以调用
    # 如果在表单form中调用这个方法，WebDriver将会查找DOM树知道发现相似表单，并提交
    #     否则将抛出 NoSuchElementException 异常
    # element.submit()


if __name__ == '__main__':
    # CTripForm().get_select()
    CTripForm().get_select_guest_num()
