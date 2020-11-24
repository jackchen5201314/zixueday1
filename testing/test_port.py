from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


class Test():
    def setup_method(self):
        op1 = Options()
        op1.debugger_address = "127.0.0.1:9112"
        self.dr = webdriver.Chrome(options=op1)

    # def teardown_method(self):
    #     self.dr.quit()

    # C:\Users\Administrator > C:\Users\Administrator\AppData\Local\Google\Chrome\Applic
    # ation\chrome --remote-debugging-port= 9112

    def test_login1(self):
        self.dr.get("https://www.baidu.com")
