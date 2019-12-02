# coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

import pymysql
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
driver = webdriver.Chrome()


driver.implicitly_wait(5)
######### 项目主网址
base_url = "https://bitcoinfaucet.uo1.net/send.php"

# 初使化浏览器参数
verificationErrors = []
# 不含证书及插件
accept_next_alert = True
# 选择使用的浏览器分辨率
print(driver.get_window_size())
driver.maximize_window()
# 声名鼠标和键盘操作变量
ac = ActionChains(driver)

u"""定位失败截图案例"""
print (u"'测试通过案例")
# print (data)

driver.get(base_url)
#login.login.setUp(self)
#login.login.login(self, "riskadmin", "123456")
time.sleep(3)
driver.find_element_by_xpath("//input[@name='to']").clear()
# self.time.sleep(0.1)
driver.find_element_by_xpath("//input[@name='to']").send_keys("msyTrojXyaFnsbU2jPxe1ZnGMHZGWA1VmS")
#driver.find_element_by_xpath("//input[@name='to']").clear()
driver.find_element_by_xpath("//input[@name='amount']").send_keys("0.00115000")
#driver.find_element_by_xpath("//input[@name='amount']").clear()
driver.find_element_by_name("password").send_keys(Keys.ENTER)

a = 1.23456
b = 2.355
c = 3.5
d = 2.5
print(round(a, 3))