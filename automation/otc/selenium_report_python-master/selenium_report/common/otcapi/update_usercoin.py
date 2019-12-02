# coding:utf-8

import requests
from common.readexcel import ExcelUtil
import unittest
import ddt
from common import db
from common import config_read
def update_usercoin():
    uid17688911111 = config_read.configread(
            "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini", "uid17688911111",
            "uid17688911111")
    uid17688911112 = config_read.configread(
        "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini", "uid17688911112",
        "uid17688911112")
    uid17688911113 = config_read.configread(
        "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini", "uid17688911113",
        "uid17688911113")
    uid17688911114 = config_read.configread(
        "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini", "uid17688911114",
        "uid17688911114")
    uid17688911115 = config_read.configread(
        "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini", "uid17688911115",
        "uid17688911115")
    uid17688911116 = config_read.configread(
        "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini", "uid17688911116",
        "uid17688911116")
    uid17688911117 = config_read.configread(
        "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini", "uid17688911117",
        "uid17688911117")
    uid17688911118 = config_read.configread(
        "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini", "uid17688911118",
        "uid17688911118")
    uid17688911119 = config_read.configread(
        "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini", "uid17688911119",
        "uid17688911119")
    uid17688911120 = config_read.configread(
        "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini", "uid17688911120",
        "uid17688911120")
    uid17688911111 = config_read.configread(
                "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "new.ini", "uid17688911111",
                "uid17688911111")
    print(uid17688911119)
    con = db.db()
    cursor = con.cursor()
    try:
        cursor.execute('update tb_user_coin set balance=100000000 , freezing_balance=0 , total_price=100000000  where user_id in (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ', (uid17688911111,uid17688911112,uid17688911113,uid17688911114,uid17688911115,uid17688911116,uid17688911117,uid17688911119,uid17688911120,uid17688911118))
        print("数据更新成功")
    except UserWarning:
        print("数据更新失败")

    con.commit() # 提交

    cursor.close()

update_usercoin()
