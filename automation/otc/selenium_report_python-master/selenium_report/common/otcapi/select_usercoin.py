# coding:utf-8

import requests
from common.readexcel import ExcelUtil
import unittest
import ddt
from common import db
from common import config_read
def select_usercoin(userid):

    con = db.db()
    cursor = con.cursor()
    try:
        cursor.execute('select balance,freezing_balance,total_price from tb_user_coin  where user_id in (%s) ', (userid))

        strs2 = cursor.fetchall()
        strs2 = strs2[0]
        #print(strs2)
        #print(strs2[0],strs2[1],strs2[2])

        print("数据查询成功")
    except UserWarning:
        print("数据查询失败")

    con.commit() # 提交

    cursor.close()
    return strs2[0],strs2[2]


