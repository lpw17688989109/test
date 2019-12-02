import json
import requests
from common.readexcel import ExcelUtil
import unittest
import ddt
from common import config_read
from case.test_casea2 import code2
from common.otcapi import send_sms_code

s = requests.session()


testData = ExcelUtil("D:\\自动化\\otc\\canshu.xlsx", "资金密码").dict_data()
# print(testData)
s = requests.session()


@ddt.ddt
class OTC(unittest.TestCase):
    u'''资金密码'''

    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Chrome()
        s = requests.session()

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        s = requests.session()

    @ddt.data(*testData)
    def test_maidan(self, data):

        '''资金密码'''
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
        # phone=body['']

        headers['token'] = config_read.configread(
            "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini",
            "token" + str(body['phone']),
            "token" + str(body['phone']))
        body['messageCode'] = send_sms_code.code2(body['phone'],3)

        #print(body['messageCode'])

        test_nub = data['id']

        body = json.dumps(body)
        print("*******正在执行用例：-----  %s  ----**********" % test_nub)
        print("请求方式：%s, 请求url:%s" % (method, url))
        print("请求params：%s" % params)
        print("请求headers：%s" % headers)
        print("请求body：%s" % body)
        print("++++++++++++++++++++++++++++++++++++++++++")

        verify = False

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
        print(r['code'])

        self.assertEqual(1, int(r['code']))


if __name__ == "__main__":
    unittest.main()
