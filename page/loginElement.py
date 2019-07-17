#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
@作者：wuchengan
@文件名：T02NVR/loginElement.py
@时间：2019/7/8 10:59
@文档说明:
"""

from base.basePage import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class T02nvrLogin(WebDriver):
    username_loc = (By.XPATH, '//*[@id="app"]/div/section/div[2]/form/div[1]/div/div[1]/input')
    password_loc = (By.XPATH, '//*[@id="app"]/div/section/div[2]/form/div[2]/div/div[1]/input')
    login_loc = (By.XPATH, '//*[@id="app"]/div/section/div[2]/form/div[3]/div/button/span')
    usernameEmpty_loc = (By.XPATH, '//*[@id="app"]/div/section/div[2]/form/div[1]/div/div[2]')
    passwordEmpty_loc = (By.XPATH, '//*[@id="app"]/div/section/div[2]/form/div[2]/div/div[2]')
    loginError_loc = (By.XPATH, '/html/body/div[3]/p')
    loginSuccess_loc = (By.XPATH, '//*[@id="app"]/section/header/ul/li[1]')

    def typeUserName(self,username):
        self.findElement(*self.username_loc).send_keys(Keys.CONTROL,'a')
        self.findElement(*self.username_loc).send_keys(Keys.DELETE)
        self.findElement(*self.username_loc).send_keys(username)

    def typePassword(self, password):
        self.findElement(*self.password_loc).send_keys(Keys.CONTROL, 'a')
        self.findElement(*self.password_loc).send_keys(Keys.DELETE)
        self.findElement(*self.password_loc).send_keys(password)

    def clickLogin(self):
        self.findElement(*self.login_loc).click()

    def login(self, username, password):
        self.typeUserName(username)
        self.typePassword(password)
        self.clickLogin()

    @property
    def getUserNameEmpty(self):
        """获取用户名为空的信息"""
        return self.findElement(*self.usernameEmpty_loc).text

    @property
    def getPassWordEmpty(self):
        """获取密码为空的信息"""
        return self.findElement(*self.passwordEmpty_loc).text

    @property
    def getLoginError(self):
        """获取错误的信息"""
        return self.findElement(*self.loginError_loc).text

    @property
    def getLoginSuccess(self):
        """获取登录成功信息"""
        return self.findElement(*self.loginSuccess_loc).text