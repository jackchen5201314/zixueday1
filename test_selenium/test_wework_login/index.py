# -*- coding:utf-8 -*-
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from test_selenium.test_wework_login.login import Login
from test_selenium.test_wework_login.register import Register


class Index:
    """
    首页的po
    """

    def __init__(self):
        # 端口调试
        # op1 = Options()
        # op1.debugger_address = "127.0.0.1:9112"
        # self.dr = webdriver.Chrome(options=op1)
        self.dr = webdriver.Chrome()
        self.dr.get("https://work.weixin.qq.com/")

    def goto_register(self):
        """
        点击立即注册
        进入到立即注册的po
        return
        """
        self.dr.find_element_by_class_name("index_head_info_pCDownloadBtn").click()
        return Register(self.dr)

    def goto_login(self):
        """
        点击企业登录
        进入企业登录的po
         return
        """
        self.dr.find_element_by_class_name("index_top_operation_loginBtn").click()

        return Login(self.dr)
