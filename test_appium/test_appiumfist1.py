# -*- coding:utf-8 -*-
from appium import webdriver
from time import sleep

# 打开小红书
# desired_caps={}
# desired_caps["platformName"] = "Android"
# desired_caps["platformVersion"] = "6.0.1"
# # desired_caps["deviceName"] = "ac99fle7"
# desired_caps["deviceName"] = "127.0.0.1:7555"
# desired_caps["appPackage"] = "com.xingin.xhs"
# desired_caps["appActivity"] = "com.xingin.xhs.activity.SplashActivity"
# desired_caps["noReset"] = "True"

"""
打开游览器页面，百度搜索

"""
desired_caps={}
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "6.0.1"
desired_caps["deviceName"] = "127.0.0.1:7555"
desired_caps["browserName"] = "Browser"
desired_caps["noReset"] = True
desired_caps['skipDeviceInitialization'] = True


driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
sleep(3)
drvier.get("http://m.baidu.com")
sleep(5)
driver.find_element_by_id("index-kw").send_keys("1233")

sleep(5)
driver.quit()



