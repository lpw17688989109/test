# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
#import cx_Oracle
import pymysql
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import unittest
from common import login
#from common import ExcelUtil
import ddt
import json
import requests
from common.readexcel import ExcelUtil
import unittest
import ddt


def dbaccount():
    ''''''
    conn = pymysql.connect(host='192.168.1.230', port=3306, user='root', password='123456', db="account", charset='utf8mb4')
    return conn
def dbuser():
    ''''''
    conn = pymysql.connect(host='192.168.1.230', port=3306, user='root', password='123456', db="user", charset='utf8mb4')
    return conn
def dborder():
    ''''''
    conn = pymysql.connect(host='192.168.1.230', port=3306, user='root', password='123456', db="order", charset='utf8mb4')
    return conn
def dbwallet():
    ''''''
    conn = pymysql.connect(host='192.168.1.230', port=3306, user='root', password='123456', db="wallet", charset='utf8mb4')
    return conn