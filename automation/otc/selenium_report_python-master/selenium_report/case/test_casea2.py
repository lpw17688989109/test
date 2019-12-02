# coding=utf-8
import json
import requests
from common import config_read


s = requests.session()


def code0(phone):
    u'''这里写了一个登录的方法,账号和密码参数化'''
    method = "post"
    url1 = config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
                                  "url", "ceshiip") + "8087/api/user/otc/get-by-phone"
    # print(url1)
    headers1 = {'Content-Type': 'application/json', 'channel': '0'}
    body1 = {"phone": phone}
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
    print(r1['data'])
    return r1['data']


def code1(phone):
    u'''这里写了一个登录的方法,账号和密码参数化'''
    method = "post"
    url1 = config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
                                  "url", "ceshiip") + "8087/api/user/get-slider/code"
    # print(url1)
    headers1 = {'Content-Type': 'application/json', 'channel': '0'}
    body1 = {"phone": phone, "type": 1}
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
    print(r1)
    return r1['data']


# login(17688989111)
# code1(17611111111)
def code2(phone):
    u'''这里写了一个登录的方法,账号和密码参数化'''
    method = "post"
    url1 = config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
                                  "url", "ceshiip") + "8087/api/user/send-sms/code"
    # print(url1)
    headers1 = {'Content-Type': 'application/json', 'channel': '0'}

    body1 = {"code": code1(phone), "countryCode": "0086", "enName": "CNY", "phone": phone, "type": 1}
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
    print(r2,"++++++++++++++++++++++++++")
    # print(r1['message'],"+++++++++++++++++++++++++++++")
    return r2['message']


def register(phone, code, yqm):
    u'''这里写了一个登录的方法,账号和密码参数化'''
    method = "post"
    url1 = config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
                                  "url", "ceshiip") + "8087/api/user/otc/register"
    #print(url1)
    headers1 = {'Content-Type': 'application/json', 'channel': '0', 'deviceType': '3'}
    body1 = {"code": yqm, "countryId": 1, "loginPassword": "d13149de00848eb013cad318d27829db64b965d7",
             "messageCode": code, "phone": phone}

    body1 = json.dumps(body1)
    #print(body1)
    verify = "verify"
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
    #print(r1,"-----------------------------------------------------")
    return r1['message'], r1['data']['id'], r1['data']['phone']

# code0(17688989555)
# code2(1768898111)
# register(17688989559,code2(17688989559))
#register(17688911111,code2(17688911111),'52GP')
