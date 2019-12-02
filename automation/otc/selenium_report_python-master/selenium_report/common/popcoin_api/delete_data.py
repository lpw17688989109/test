# coding:utf-8

import requests
from common.readexcel import ExcelUtil
import unittest
import ddt

from common import db
from common import config_read

uid17688900060 = config_read.configread(
    "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "popcoin.ini", "uid17688900060",
    "uid17688900060")
uid17688900061 = config_read.configread(
    "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "popcoin.ini", "uid17688900061",
    "uid17688900061")
uid17688900062 = config_read.configread(
    "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "popcoin.ini", "uid17688900062",
    "uid17688900062")
uid17688900063 = config_read.configread(
    "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "popcoin.ini", "uid17688900063",
    "uid17688900063")
uid17688900064 = config_read.configread(
    "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "popcoin.ini", "uid17688900064",
    "uid17688900064")
uid17688900065 = config_read.configread(
    "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "popcoin.ini", "uid17688900065",
    "uid17688900065")
uid17688900066 = config_read.configread(
    "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "popcoin.ini", "uid17688900066",
    "uid17688900066")
uid17688900067 = config_read.configread(
    "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "popcoin.ini", "uid17688900067",
    "uid17688900067")
uid17688900068 = config_read.configread(
    "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "popcoin.ini", "uid17688900068",
    "uid17688900068")
uid17688900069 = config_read.configread(
    "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "popcoin.ini", "uid17688900069",
    "uid17688900069")
uid17688900060 = config_read.configread(
    "D:\\自动化\\otc\\selenium_report_python-master\\selenium_report\\config", "popcoin.ini", "uid17688900060",
    "uid17688900060")


def delete_tb_user():
    con = db.dbuser()
    cursor = con.cursor()
    try:
        cursor.execute('delete from tb_user  where id in (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ', (
        uid17688900060, uid17688900061, uid17688900062, uid17688900063, uid17688900064, uid17688900065, uid17688900066,
        uid17688900068, uid17688900069, uid17688900067))
        print("数据删除成功")
    except UserWarning:
        print("数据删除失败")

    con.commit()  # 提交

    cursor.close()


def delete_tb_exchange_entrust():
    con = db.dborder()
    cursor = con.cursor()
    try:
        cursor.execute('delete from tb_exchange_entrust  where user_id in (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ', (
            uid17688900060, uid17688900061, uid17688900062, uid17688900063, uid17688900064, uid17688900065,
            uid17688900066,
            uid17688900068, uid17688900069, uid17688900067))
        print("数据删除成功")
    except UserWarning:
        print("数据删除失败")

    con.commit()  # 提交

    cursor.close()

def delete_tb_popcoin_user_coin():
    con = db.dbaccount()
    cursor = con.cursor()
    try:
        cursor.execute('delete from tb_popcoin_user_coin  where user_id in (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ', (
            uid17688900060, uid17688900061, uid17688900062, uid17688900063, uid17688900064, uid17688900065,
            uid17688900066,
            uid17688900068, uid17688900069, uid17688900067))
        print("数据删除成功")
    except UserWarning:
        print("数据删除失败")

    con.commit()  # 提交

    cursor.close()

def delete_tb_popcoin_transaction():
    con = db.dbaccount()
    cursor = con.cursor()
    try:
        cursor.execute('delete from tb_popcoin_transaction  where userId in (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ', (
            uid17688900060, uid17688900061, uid17688900062, uid17688900063, uid17688900064, uid17688900065,
            uid17688900066,
            uid17688900068, uid17688900069, uid17688900067))
        print("数据删除成功")
    except UserWarning:
        print("数据删除失败")

    con.commit()  # 提交

    cursor.close()

def delete_tb_popcoin_user_coin_record():
    con = db.dbaccount()
    cursor = con.cursor()
    try:
        cursor.execute('delete from tb_popcoin_user_coin_record  where user_id in (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ', (
            uid17688900060, uid17688900061, uid17688900062, uid17688900063, uid17688900064, uid17688900065,
            uid17688900066,
            uid17688900068, uid17688900069, uid17688900067))
        print("数据删除成功")
    except UserWarning:
        print("数据删除失败")

    con.commit()  # 提交

    cursor.close()

def delete_tb_pop_high_authentication():
    con = db.dbuser()
    cursor = con.cursor()
    try:
        cursor.execute('delete from tb_pop_high_authentication  where user_id in (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ', (
        uid17688900060, uid17688900061, uid17688900062, uid17688900063, uid17688900064, uid17688900065, uid17688900066,
        uid17688900068, uid17688900069, uid17688900067))
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
        uid17688900060, uid17688900061, uid17688900062, uid17688900063, uid17688900064, uid17688900065, uid17688900066,
        uid17688900068, uid17688900069, uid17688900067))
        print("数据删除成功")
    except UserWarning:
        print("数据删除失败")

    con.commit()  # 提交

    cursor.close()

def delete_tb_user_agreement():
    con = db.dbuser()
    cursor = con.cursor()
    try:
        cursor.execute('delete from tb_user_agreement  where user_id in (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ', (
        uid17688900060, uid17688900061, uid17688900062, uid17688900063, uid17688900064, uid17688900065, uid17688900066,
        uid17688900068, uid17688900069, uid17688900067))
        print("数据删除成功")
    except UserWarning:
        print("数据删除失败")

    con.commit()  # 提交

    cursor.close()


def delete_tb_pop_user_extend():
    con = db.dbuser()
    cursor = con.cursor()
    try:
        cursor.execute('delete from tb_pop_user_extend  where user_id in (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ', (
        uid17688900060, uid17688900061, uid17688900062, uid17688900063, uid17688900064, uid17688900065, uid17688900066,
        uid17688900068, uid17688900069, uid17688900067))
        print("数据删除成功")
    except UserWarning:
        print("数据删除失败")

    con.commit()  # 提交

    cursor.close()

delete_tb_exchange_entrust()
delete_tb_popcoin_user_coin()
delete_tb_popcoin_user_coin_record()
delete_tb_popcoin_transaction()
delete_tb_pop_high_authentication()
delete_tb_user_invite()
delete_tb_user_agreement()
delete_tb_pop_user_extend()
delete_tb_user()

