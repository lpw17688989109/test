# coding=utf-8
# coding:utf-8
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
#import cx_Oracle
import pymysql
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
# coding:utf-8
from selenium import webdriver
import unittest
import time
class login(unittest.TestCase):
    u'''登录博客'''
    def setUp(self):
        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome()
        base_url = "http://10.201.200.94:8086"
        self.driver.get(base_url + "/#/login")
        self.driver.implicitly_wait(5)
        print ("登录")

    def login(self, username, psw):
        u'''这里写了一个登录的方法,账号和密码参数化'''

        #driver.get(base_url + "/#/login")
        self.driver = webdriver.Chrome()
        base_url = "http://10.201.200.94:8086"
        self.driver.get(base_url + "/#/login")
        self.driver.implicitly_wait(5)

        time.sleep(2)
        self.driver.find_element_by_name("userId").clear()
        time.sleep(0.1)
        self.driver.find_element_by_name("userId").send_keys(username)
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys(psw)
        self.driver.find_element_by_name("password").send_keys(Keys.ENTER)
        time.sleep(2)

    def is_login_sucess(self):
        u'''判断是否获取到登录账户名称'''
        try:
            self.driver.find_element_by_xpath("//span[text()='风险控制']")
            #print text
            return True
        except:
            return False

    def tearDown(self):
        self.driver.quit()

    def test_01(self):
        u"""定位失败截图案例"""
        print (u"'测试通过案例")
        u'''登录案例参考:账号，密码自己设置'''
        self.login(u"riskadmin", u"123456")  # 调用登录方法

if __name__ == "__main__":
    unittest.main()