#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
@作者：wuchengan
@文件名：T02NVR/basePage.py
@时间：2019/7/8 10:44
@文档说明:
"""

from selenium import webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException

class WebDriver(object):
    def __init__(self):
        self.driver = driver

    def findElement(self,*loc):
        """单个元素定位"""
        try:
            return self.driver.find_element(*loc)
        except NoSuchElementException as e:
            print('Error Detail{0}'.format(e.args[0]))

    def findElements(self,*loc):
        """多元素定位方法"""
        try:
            return self.driver.find_elements(*loc)
        except NoSuchElementException as e:
            print('Error Detail{0}'.format(e.args[0]))