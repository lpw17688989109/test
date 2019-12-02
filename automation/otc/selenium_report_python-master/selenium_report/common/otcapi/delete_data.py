# coding:utf-8

import requests
from common.readexcel import ExcelUtil
import unittest
import ddt

from common import db
from common import config_read

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


def delete_user():
    con = db.dbuser()
    cursor = con.cursor()
    try:
        cursor.execute('delete from tb_user  where id in (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ', (
        uid17688911111, uid17688911112, uid17688911113, uid17688911114, uid17688911115, uid17688911116, uid17688911117,
        uid17688911119, uid17688911120, uid17688911118))
        print("数据删除成功")
    except UserWarning:
        print("数据删除失败")

    con.commit()  # 提交

    cursor.close()


def delete_tb_advertisement():
    con = db.dborder()
    cursor = con.cursor()
    try:
        cursor.execute('delete from tb_advertisement  where user_id in (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ', (
            uid17688911111, uid17688911112, uid17688911113, uid17688911114, uid17688911115, uid17688911116,
            uid17688911117,
            uid17688911119, uid17688911120, uid17688911118))
        print("数据删除成功")
    except UserWarning:
        print("数据删除失败")

    con.commit()  # 提交

    cursor.close()

def delete_tb_user_coin():
    con = db.db()
    cursor = con.cursor()
    try:
        cursor.execute('delete from tb_user_coin  where user_id in (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ', (
            uid17688911111, uid17688911112, uid17688911113, uid17688911114, uid17688911115, uid17688911116,
            uid17688911117,
            uid17688911119, uid17688911120, uid17688911118))
        print("数据删除成功")
    except UserWarning:
        print("数据删除失败")

    con.commit()  # 提交

    cursor.close()

def delete_tb_kyc_authentication():
    con = db.dbuser()
    cursor = con.cursor()
    try:
        cursor.execute('delete from tb_kyc_authentication  where user_id in (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ', (
        uid17688911111, uid17688911112, uid17688911113, uid17688911114, uid17688911115, uid17688911116, uid17688911117,
        uid17688911119, uid17688911120, uid17688911118))
        print("数据删除成功")
    except UserWarning:
        print("数据删除失败")

    con.commit()  # 提交

    cursor.close()

def delete_tb_user_invite():
    con = db.dbuser()
    cursor = con.cursor()
    try:
        cursor.execute('delete from tb_user_invite  where invite_id in (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ', (
        uid17688911111, uid17688911112, uid17688911113, uid17688911114, uid17688911115, uid17688911116, uid17688911117,
        uid17688911119, uid17688911120, uid17688911118))
        print("数据删除成功")
    except UserWarning:
        print("数据删除失败")

    con.commit()  # 提交

    cursor.close()

def delete_tb_acceptor_config():
    con = db.dbuser()
    cursor = con.cursor()
    try:
        cursor.execute('delete from tb_acceptor_config  where user_id in (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ', (
        uid17688911111, uid17688911112, uid17688911113, uid17688911114, uid17688911115, uid17688911116, uid17688911117,
        uid17688911119, uid17688911120, uid17688911118))
        print("数据删除成功")
    except UserWarning:
        print("数据删除失败")

    con.commit()  # 提交

    cursor.close()


def delete_tb_ad_time_config():
    con = db.dbuser()
    cursor = con.cursor()
    try:
        cursor.execute('delete from tb_ad_time_config  where user_id in (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ', (
        uid17688911111, uid17688911112, uid17688911113, uid17688911114, uid17688911115, uid17688911116, uid17688911117,
        uid17688911119, uid17688911120, uid17688911118))
        print("数据删除成功")
    except UserWarning:
        print("数据删除失败")

    con.commit()  # 提交

    cursor.close()

delete_tb_advertisement()
delete_tb_user_coin()
delete_tb_kyc_authentication()
delete_tb_user_invite()
delete_tb_acceptor_config()
delete_tb_ad_time_config()
delete_user()

