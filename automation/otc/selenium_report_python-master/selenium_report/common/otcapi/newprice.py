# coding=utf-8
# coding:utf-8
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest, time, re
#import cx_Oracle
import pymysql
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import unittest
from common import login
#from common import ExcelUtil
from common.jieshuju import noround
from common import config_read
import ddt
import json
import requests
from common.readexcel import ExcelUtil
import unittest
import ddt
from common import db
from common import config_read
import pymysql
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
# coding:utf-8
from selenium import webdriver
import unittest
import time

s = requests.session()
def realprice(advertisementNo,token):
    u'''取价'''
    method="post"
    urlprice=config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config","new.ini","url","ceshiip")+"8087/api/order/advertisement-get/get"
    print(urlprice)
    headersprice={'Content-Type': 'application/json', 'channel': '0','token':token}
    print(headersprice,type(headersprice))
    body1={"advertisementNo":advertisementNo,"favorableRate":0.0,"floatPremium":0.0}
    body1=json.dumps(body1)
    print(type(body1),body1)
    verify="verify"
    rprice = s.request(method=method,
                   url=urlprice,
                   headers=headersprice,
                   data=body1,
                   verify=verify
                   )
    #print("页面返回信息：%s" % rprice.json())
    rprice = rprice.json()
    print(rprice)
    print(rprice['data']['offer'])
    return rprice['data']['offer']
