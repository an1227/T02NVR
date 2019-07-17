#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
@作者：wuchengan
@文件名：T02NVR/init.py
@时间：2019/7/8 11:13
@文档说明:
"""
from selenium import webdriver
from utils.operationXlsx import *
import unittest

class Init(unittest.TestCase,OperationExcel):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get('http://10.169.3.82')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


