# coding:utf-8
import json
import requests
from common import config_read
import time
aa=0

s = requests.session()
#lpw1_184844,

def order_buy_create():
    global aa
    u'''xiadan'''
    method="post"
    urlprice=config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config","new.ini","url","ceshiip")+"18110/order/buy/create"
    print(urlprice)
    headersprice={'Content-Type': 'application/json', 'channel': '2','responseBodyNoEncryption':'3', 'requestSource': 'h5','Cache-Control':'no-cache'}
    #print(headersprice,type(headersprice))
    body1={
    "appKey":"lpw1_184844",
    "symbol":"usdt",
    "amount":"800",
    "payType":2,
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
    print(rprice)
    uu=rprice['data']['redirectUrl']
    aa=uu.index('data')
    aa = uu[aa+5:]
    print(aa)
    print(rprice['data']['redirectUrl'])
    #print(rprice['data']['offer'])

s = requests.session()
def check_order():
    u'''xiadan'''
    method="post"
    urlprice=config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config","new.ini","url","ceshiip")+"18110/order/buy/check-order"
    print(urlprice)
    headersprice={'Content-Type': 'application/json', 'channel': '2','responseBodyNoEncryption':'3', 'requestSource': 'h5','Cache-Control':'no-cache'}
    #print(headersprice,type(headersprice))
    body1={
    "appKey":"lpw1_184844",
    "data":aa}
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
   #print(rprice['data']['redirectUrl'])
    #print(rprice['data']['offer'])
    return rprice

def send_sms():
    u'''xiadan'''
    method = "post"
    urlprice = config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
                                      "url", "ceshiip") + "18110/order/buy/send-sms"
    print(urlprice)
    headersprice = {'Content-Type': 'application/json', 'channel': '2', 'responseBodyNoEncryption': '3',
                    'requestSource': 'h5', 'Cache-Control': 'no-cache'}
    # print(headersprice,type(headersprice))
    body1 = {
        "appKey": "lpw1_184844",
        "data": aa}
    body1 = json.dumps(body1)
    print(type(body1),body1)
    verify = "verify"
    rprice = s.request(method=method,
                       url=urlprice,
                       headers=headersprice,
                       data=body1,
                       verify=verify
                       )
    # print("页面返回信息：%s" % rprice.json())
    rprice = rprice.json()

    print(rprice)
    # print(rprice['data']['redirectUrl'])
    # print(rprice['data']['offer'])
    return rprice['message']

def match_advertise():
    u'''xiadan'''
    method = "post"
    urlprice = config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
                                      "url", "ceshiip") + "18110/order/buy/match-advertise"
    print(urlprice)
    headersprice = {'Content-Type': 'application/json', 'channel': '2', 'responseBodyNoEncryption': '3',
                    'requestSource': 'h5', 'Cache-Control': 'no-cache'}
    # print(headersprice,type(headersprice))
    body1 = {
        "appKey": "lpw1_184844",
        "code": send_sms(),
        "payName": "11",
        "payType": "2",
        "data": aa}
    body1 = json.dumps(body1)
    print(type(body1), body1)
    verify = "verify"
    rprice = s.request(method=method,
                       url=urlprice,
                       headers=headersprice,
                       data=body1,
                       verify=verify
                       )
    # print("页面返回信息：%s" % rprice.json())
    rprice = rprice.json()

    print(rprice)
    # print(rprice['data']['redirectUrl'])
    # print(rprice['data']['offer'])
    return rprice

def conform_pay():
    u'''xiadan'''
    method="post"
    urlprice=config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config","new.ini","url","ceshiip")+"18110/order/buy/conform-pay"
    print(urlprice)
    headersprice={'Content-Type': 'application/json', 'channel': '2','responseBodyNoEncryption':'3', 'requestSource': 'h5','Cache-Control':'no-cache'}
    #print(headersprice,type(headersprice))
    body1={
    "appKey":"lpw1_184844",
    "data":aa,
    "status":"1"}
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

order_buy_create()
check_order()
match_advertise()
time.sleep(0.5)
conform_pay()


