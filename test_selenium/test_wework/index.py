from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from test_selenium.test_wework.add_member import AddMember


class Index:
    def __init__(self):
        op1 = Options()
        op1.debugger_address = "127.0.0.1:9135"
        self.dr = webdriver.Chrome(options=op1)
        self.dr.get("https://work.weixin.qq.com/wework_admin/frame#index")

    # def teardown_method(self):
    #     self.dr.quit()

    # C:\Users\Administrator\AppData\Local\Google\Chrome\Applic
    # ation\chrome --remote-debugging-port=9135

    def goto_add_member(self):
        """
        添加成员

        """
        self.dr.implicitly_wait(3)
        self.dr.find_element_by_css_selector(".index_service_cnt_item_title").click()

        return AddMember(self.dr)

    def goto_import_address(self):
        pass

    """
    导入通讯录
    
    """

    def join_member(self):
        """

        """
