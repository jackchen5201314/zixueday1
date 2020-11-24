from selenium import webdriver
import time


class AddMember:

    def __init__(self, dr):
        self.dr = dr

    def add_member(self):
        time.sleep(2)
        self.dr.find_element_by_id("username").send_keys("张三")
        self.dr.find_element_by_id("memberAdd_acctid").send_keys("12333")
        self.dr.find_element_by_id("memberAdd_phone").send_keys("12233311121")
        self.dr.find_element_by_xpath("//div/div[2]/div/div[4]/div/form/div[3]/a[2]").click()
