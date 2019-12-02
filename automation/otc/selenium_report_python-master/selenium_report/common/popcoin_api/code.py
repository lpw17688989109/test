# coding=utf-8
import json
import requests
from common import config_read
true=True
false=False
null=None


s = requests.session()


def get_by_phone(phone):
    u'''这里写了一个登录的方法,账号和密码参数化'''
    method = "post"
    url1 = config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
                                  "url", "ceshiip") + "8006/api/user/otc/get-by-phone"
    # print(url1)
    headers1 = {'Content-Type': 'application/json', 'channel': '3', 'deviceType': '3'}
    body1 = {"phone": phone,"serviceKey":"POPCoin70947"}
    body1 = json.dumps(body1)
    verify = "verify"
    r1 = s.request(method=method,
                   url=url1,
                   headers=headers1,
                   data=body1,
                   verify=verify
                   )
    # print("页面返回信息：%s" % r1.json())
    r1 = r1.json()
    #print(r1['data'])
    return r1['data']

#get_by_phone(17688900060)

def get_slider_code(phone):
    u'''这里写了一个登录的方法,账号和密码参数化'''
    method = "post"
    url1 = config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
                                  "url", "ceshiip") + "8006/api/user/get-slider/code"
    # print(url1)
    headers1 = {'Content-Type': 'application/json', 'channel': '3', 'deviceType': '3'}
    body1 = {"phone": phone, "type": 1,"serviceKey":"POPCoin70947"}
    body1 = json.dumps(body1)
    verify = "verify"
    r1 = s.request(method=method,
                   url=url1,
                   headers=headers1,
                   data=body1,
                   verify=verify
                   )
    # print("页面返回信息：%s" % r1.json())
    r1 = r1.json()
    #print(r1)
    return r1['data']
#get_slider_code(17688900060)


# login(17688989111)
# code1(17611111111)
def send_sms_code(phone):
    u'''这里写了一个登录的方法,账号和密码参数化'''
    method = "post"
    url1 = config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
                                  "url", "ceshiip") + "8006/api/user/send-sms/code"
    # print(url1)
    headers1 = {'Content-Type': 'application/json', 'channel': '3', 'deviceType': '3'}

    body1 = {"code": get_slider_code(phone), "countryCode": "0086", "enName": "CNY", "phone": phone, "type": 1,"serviceKey":"POPCoin70947"}
    body1 = json.dumps(body1)
    print(body1)
    verify = "verify"
    r2 = s.request(method=method,
                   url=url1,
                   headers=headers1,
                   data=body1,
                   verify=verify
                   )
    # print("页面返回信息：%s" % r1.json())
    r2 = r2.json()
    #print(r2,"++++++++++++++++++++++++++")
    # print(r1['message'],"+++++++++++++++++++++++++++++")
    return r2['message']
#send_sms_code(17688900060)


def register(phone, code):
    u'''这里写了一个登录的方法,账号和密码参数化'''
    method = "post"
    url1 = config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
                                  "url", "ceshiip") + "8006/api/user/pop/register"
    #print(url1)
    headers1 = {'Content-Type': 'application/json;charset=UTF-8', 'channel': '3', 'deviceType': '3'}
    body1 = {"countryId": 1, "loginPassword": "d13149de00848eb013cad318d27829db64b965d7","messageCode": code, "phone": phone,"type": 1,"serviceKey":"POPCoin70947"}

    body1 = json.dumps(body1)
    print(body1)
    verify = False
    r1 = s.request(method=method,
                   url=url1,
                   headers=headers1,
                   data=body1,
                   verify=verify
                   )
    # print("页面返回信息：%s" % r1.json())
    r1 = r1.json()
    #r1=r1.content
    # print(r1['message'],r1['data']['id'],r1['data']['phone'],"+++++++++++++++++++++++++++++")
    # r1['id'],r1['phone']
    print(r1,"-----------------------------------------------------")
    return r1['message'], r1['data']['id'], r1['data']['phone']


# code0(17688989555)
# code2(1768898111)
#register(17688900060,send_sms_code(17688900060))

