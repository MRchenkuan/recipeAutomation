# coding=utf-8
import random
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest,os,time,json
import data
from Tools import getCapture

'''
    此处为后台登录的基本类
'''
class BaseSetRecipeAd(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        print 'yes'
        self.driver.implicitly_wait(30)
        print self.driver.title
        self.base_url = "http://www.haodou.com"
        self.verificationErrors = []
        self.accept_next_alert = True

        #---------------------------一次登录
        driver = self.driver
        driver.get(self.base_url + "/admin/v2/index.php")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin@admin.com")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        #取验证码
        #capcode = getCapture(type='adminlogin',ssid=driver.get_cookie('HDSSID').get('value'))
        #driver.find_element_by_id('code').send_keys(capcode)
        driver.find_element_by_tag_name('button').click()
        #---------------------------一次登录结束


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

'''
    此处为前台注册的基本类
'''
class HaodouAcctRegisterBase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        print 'yes'
        self.driver.implicitly_wait(30)
        print self.driver.title
        self.base_url = "http://login.haodou.com/register.php?product=1"
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)