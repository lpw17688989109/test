# coding=utf-8

from appium import webdriver
import unittest, time, re
from common.appium.qidong import qidong


def login(driver):

    driver.find_element_by_id("com.jgyc.popcoin:id/iv_header").click()
    time.sleep(1)
    driver.find_element_by_id("com.jgyc.popcoin:id/tv_nick_name").click()
    time.sleep(1)

    driver.find_element_by_id("com.jgyc.popcoin:id/edt_mobile").click()
    driver.find_element_by_id("com.jgyc.popcoin:id/edt_mobile").send_keys("17688900005")
    driver.find_element_by_id("com.jgyc.popcoin:id/edt_pswd").click()
    driver.find_element_by_id("com.jgyc.popcoin:id/edt_pswd").send_keys("a1234567")
    driver.find_element_by_id("com.jgyc.popcoin:id/btn_lg").click()
    driver.contexts
login(qidong())


