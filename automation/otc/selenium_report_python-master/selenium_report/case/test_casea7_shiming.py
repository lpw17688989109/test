# coding:utf-8
import json
import requests
from common.readexcel import ExcelUtil
import unittest
import ddt
from common import config_read

s = requests.session()

testData=ExcelUtil("D:\\自动化\\otc\\canshu.xlsx","实名认证").dict_data()
#print(testData)
s = requests.session()



@ddt.ddt
class OTC(unittest.TestCase):
    u'''OTC实名认证'''

    @classmethod
    def setUpClass(cls):
        #cls.driver = webdriver.Chrome()
        s = requests.session()

    @classmethod
    def tearDownClass(cls):
        #cls.driver.quit()
        s = requests.session()

    @ddt.data(*testData)
    def test_maidan(self, data):

        '''注册'''
        method = data["method"]
        url = config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
                                     "url", "ceshiip") + data["url"]

        # url后面的params参数
        try:
            params = eval(data["params"])
        except:
            params = None
        # 请求头部headers
        try:
            headers = eval(data["headers"])
            # print("请求头部：%s" % headers)
        except:
            headers = None
        # 请求body
        try:
            body = eval(data["body"])
            # print("请求body：%s" % body)
            # print(type(body))
        except:
            body = None
        # print(type(body))
        #phone=body['']

        headers['token'] = config_read.configread(
            "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini", "token"+str(body['username']),
            "token"+str(body['username']))
        body['id'] = config_read.configread(
            "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
            "uid" + str(body['username']),
            "uid" + str(body['username']))
        userid=body['id'] = config_read.configread(
            "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
            "uid" + str(body['username']),
            "uid" + str(body['username']))


        test_nub = data['id']

        body = json.dumps(body)
        print("*******正在执行用例：-----  %s  ----**********" % test_nub)
        print("请求方式：%s, 请求url:%s" % (method, url))
        print("请求params：%s" % params)
        print("请求headers：%s" % headers)
        print("请求body：%s" % body)
        print("++++++++++++++++++++++++++++++++++++++++++")


        verify = False
        res = {}  # 接受返回数据

        r = s.request(method=method,
                      url=url,
                      params=params,
                      headers=headers,
                      data=body,
                      verify=verify
                      )
        print("页面返回信息：%s" % r.json())
        r = r.json()
        print(r)


        self.assertEqual(1, r['code'])


        #后台认证+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        method = data["method1"]
        url = config_read.configread("D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
                                     "url", "ceshiip") + data["url1"]

        # url后面的params参数
        try:
            params = eval(data["params1"])
        except:
            params = None
        # 请求头部headers
        try:
            headers = eval(data["headers1"])
            # print("请求头部：%s" % headers)
        except:
            headers = None
        # 请求body
        try:
            body = eval(data["body1"])
            # print("请求body：%s" % body)
            # print(type(body))
        except:
            body = None
        # print(type(body))

        headers['token'] = config_read.configread(
            "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
            "token" + str("admin"),
            "token" + str("admin"))

        body['userId']=userid
        test_nub = data['id']

        body = json.dumps(body)
        print("*******正在执行用例：-----  %s  ----**********" % test_nub)
        print("请求方式：%s, 请求url:%s" % (method, url))
        print("请求params：%s" % params)
        print("请求headers：%s" % headers)
        print("请求body：%s" % body)
        print("++++++++++++++++++++++++++++++++++++++++++")

        verify = False
        res = {}  # 接受返回数据

        r = s.request(method=method,
                      url=url,
                      params=params,
                      headers=headers,
                      data=body,
                      verify=verify
                      )
        print("页面返回信息：%s" % r.json())
        r = r.json()
        print(r)

        self.assertEqual(1, r['code'])













if __name__ == "__main__":
    unittest.main()
