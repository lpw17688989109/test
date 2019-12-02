# coding=utf-8

from appium import webdriver
from appium import webdriver
import unittest, time, re

desired_caps = {

                'platformName': 'Android',

                'deviceName': '127.0.0.1:7555',

                'platformVersion': '6.0.1',

                # apk包名

                'appPackage': 'com.jgyc.popcoin',

                # apk的launcherActivity

                'appActivity': 'com.jgyc.popcoin.activity.start.StartActivity'

                }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(3)

driver.find_element_by_id("com.jgyc.popcoin:id/iv_header").click()
time.sleep(1)
driver.find_element_by_id("com.jgyc.popcoin:id/tv_nick_name").click()
time.sleep(1)

driver.find_element_by_id("com.jgyc.popcoin:id/edt_mobile").click()
driver.find_element_by_id("com.jgyc.popcoin:id/edt_mobile").send_keys("17688989109")
driver.find_element_by_id("com.jgyc.popcoin:id/edt_pswd").click()
driver.find_element_by_id("com.jgyc.popcoin:id/edt_pswd").send_keys("a1234567")
driver.find_element_by_id("com.jgyc.popcoin:id/btn_lg").click()
driver.contexts
