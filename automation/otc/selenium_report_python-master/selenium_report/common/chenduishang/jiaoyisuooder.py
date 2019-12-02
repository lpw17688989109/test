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

s = requests.session()
def order_buy_create():
    u'''xiadan'''
    method="post"
    urlprice=config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config","new.ini","url","ceshiip")+"18110/order/buy/create"
    print(urlprice)
    headersprice={'Content-Type': 'application/json', 'channel': '2','responseBodyNoEncryption':'3', 'requestSource': 'h5','Cache-Control':'no-cache'}
    #print(headersprice,type(headersprice))
    #07726544
    #lpw132791
    body1={
    "appKey":"lpw132791",
    "symbol":"usdt",
    "amount":"800",
    "payType":1,
    "purchaseType":"1",
    "outOrderNo":"13131313131",
    "phone":"13632357047",
    "name":"131231313",
    "idCard":"131313131313"
    }
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
    uu=rprice['data']['redirectUrl']
    aa=uu.index('data')
    aa = uu[aa+5:]
    print(aa)
    print(rprice['data']['redirectUrl'])
    #print(rprice['data']['offer'])
    return aa
order_buy_create()
