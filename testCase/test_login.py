#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
@作者：wuchengan
@文件名：T02NVR/test_login.py
@时间：2019/7/8 11:11
@文档说明:
"""
from page.loginElement import *
from base.init import *
import time

class LoginTest(Init,T02nvrLogin):

    def test_a_login_null_username(self, filename='data.xlsx'):
        """登录业务：用户名为空"""
        self.login(self.getExcelData(filename)[0][0], self.getExcelData(filename)[0][1])
        time.sleep(1)
        try:
            self.assertEqual(self.getUserNameEmpty, self.getExcelData(filename)[0][2])
            self.modifyExcel(filename, 2, 4, 'P', '测试通过')
        except Exception as e:
            self.modifyExcel(filename, 2, 4, 'F', repr(e))

    def test_b_login_null_password(self, filename='data.xlsx'):
        """登录业务：密码为空"""
        self.login(self.getExcelData(filename)[1][0], self.getExcelData(filename)[1][1])
        time.sleep(1)
        try:
            self.assertEqual(self.getPassWordEmpty, self.getExcelData(filename)[1][2])
            self.modifyExcel(filename, 3, 4, 'P', '测试通过')
        except Exception as e:
            self.modifyExcel(filename, 3, 4, 'F', repr(e))

    def test_c_login_wrong(self, filename='data.xlsx'):
        """登录业务：用户名密码错误"""
        self.login(self.getExcelData(filename)[2][0], self.getExcelData(filename)[2][1])
        time.sleep(2)
        try:
            self.assertEqual(self.getLoginError, self.getExcelData(filename)[2][2])
            self.modifyExcel(filename, 4, 4, 'P', '测试通过')
        except Exception as e:
            self.modifyExcel(filename, 4, 4, 'F', repr(e))

    def test_d_login_success(self, filename='data.xlsx'):
        """登录业务：登录成功"""
        self.login(self.getExcelData(filename)[3][0], self.getExcelData(filename)[3][1])
        try:
            self.assertEqual(self.getLoginSuccess, self.getExcelData(filename)[3][2])
            self.modifyExcel(filename, 5, 4, 'P', '测试通过')
        except Exception as e:
            self.modifyExcel(filename, 5, 4, 'F', repr(e))


if __name__ == '__main__':
    # unittest.main(verbosity=2)
    suite = unittest.TestSuite()
    list = ['test_a_login_null_username', 'test_b_login_null_password', 'test_c_login_wrong', 'test_d_login_success']
    for testcase in list:
        suite.addTest(LoginTest(testcase))
    runner = unittest.TextTestRunner()
    runner.run(suite)