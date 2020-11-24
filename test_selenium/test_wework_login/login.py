from selenium import webdriver

from test_selenium.test_wework_login.register import Register


class Login:
    """
    扫描二维码
    进入登录页面po
    """

    def __init__(self, dr):
        self.dr = dr

    def scan(self):
        """
        扫描二维码
        """
        pass

    def goto_register(self):
        """
               企业注册
               进入到立即注册的po
               return
               """
        self.dr.find_element_by_class_name("login_registerBar_link").click()

        return Register(self.dr)
