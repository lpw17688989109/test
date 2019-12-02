# coding:utf-8
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
from common.chenduishang.jiaoyisuooder import order_buy_create

s = requests.session()
def check_order():
    u'''xiadan'''
    method="post"
    urlprice=config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config","new.ini","url","ceshiip")+"18110/order/buy/check-order"
    print(urlprice)
    headersprice={'Content-Type': 'application/json', 'channel': '2','responseBodyNoEncryption':'3', 'requestSource': 'h5','Cache-Control':'no-cache'}
    #print(headersprice,type(headersprice))
    body1={
    "appKey":"lpw132791",
    "data":order_buy_create()}
    body1=json.dumps(body1)
    #print(type(body1),body1)
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
   #print(rprice['data']['redirectUrl'])
    #print(rprice['data']['offer'])
    return rprice
check_order()
