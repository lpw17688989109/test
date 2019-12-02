# coding=utf-8

from appium import webdriver
import unittest, time, re
def qidong():

    desired_caps = {

                'platformName': 'Android',

                'deviceName': '127.0.0.1:7555',

                'platformVersion': '6.0.1',

                # apk包名

                'appPackage': 'com.jgyc.popcoin',

                # apk的launcherActivity

                'appActivity': 'com.jgyc.popcoin.activity.start.StartActivity'
                #com.jgyc.popcoin.activity.start.StartActivity


                }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    import unittest, time, re
    time.sleep(3)
    return driver


