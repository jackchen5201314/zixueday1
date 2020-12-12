# -*- coding:utf-8 -*-
from appium import webdriver
from time import sleep
import pytest
import yaml



with open(r"C:\Users\Administrator\PycharmProjects\zixueday1\test_appium\data1\addmember.yml",encoding='utf-8') as f:
    adddata=yaml.safe_load(f)

class Testaddmember():
    def setup_class(self):
        desired_caps={}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "6.0.1"
        desired_caps["deviceName"] = "127.0.0.1:7555"

        desired_caps["appPackage"] = "com.tencent.wework"
        desired_caps["appActivity"] = ".launch.LaunchSplashActivity"
        desired_caps["skipDeviceInitialization"] = 'True'
        desired_caps["skipServerInstallation"] = 'True'
        desired_caps["dontStopAppOnReset"] = 'false'

        desired_caps["noReset"] = 'True'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()



    @pytest.mark.parametrize("name,tele",adddata)
    def test_addmember(self,name,tele):

        el1 = self.driver.find_element_by_xpath("//*[@text='通讯录']")
        el1.click()
        self.driver.implicitly_wait(3)
        el2 = self.driver.find_element_by_xpath("//*[@text='添加成员']")
        el2.click()
        self.driver.implicitly_wait(3)
        el3 = self.driver.find_element_by_xpath("//*[@text='手动输入添加']")
        el3.click()

        el7 = self.driver.find_element_by_xpath("(//*[@class='android.widget.EditText'])[1]")
        el7.send_keys(name)
        el4 = self.driver.find_element_by_id("com.tencent.wework:id/fow")
        el4.send_keys(tele)
        el4.click()
        el5 = self.driver.find_element_by_xpath("//*[@text='设置部门']")
        el5.click()
        self.driver.implicitly_wait(3)
        el6 = self.driver.find_element_by_id("com.tencent.wework:id/gsh")
        el6.click()
        self.driver.implicitly_wait(3)
        el8 = self.driver.find_element_by_id("com.tencent.wework:id/i6k")
        el8.click()
        sleep(3)
        self.driver.find_element_by_id("com.tencent.wework:id/i63").click()


