# coding=utf-8
import random
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest,os,time,re
import data

'''报名自动化'''
class newSomeTopic(unittest.TestCase):
    report={}
    def setUp(self):
        self.driver = webdriver.Firefox()
        print 'began'
        self.driver.implicitly_wait(30)
        print self.driver.title
        self.base_url = "http://wo.haodou.com"
        self.verificationErrors = []
        self.accept_next_alert = True

        #---------------------------一次登录
        # driver = self.driver
        # driver.get(self.base_url + "/recipe")
        # driver.find_element_by_link_text(u"登录").click()
        # driver.find_element_by_id("account").clear()
        # driver.find_element_by_id("account").send_keys("393667111@qq.com")
        # driver.find_element_by_id("password").clear()
        # driver.find_element_by_id("password").send_keys("ckadol")
        # driver.find_element_by_id("btn_login").click()
        #---------------------------一次登录结束

    def test_1_newSomeBaoming(self,amount=200):
        topicid = [330479,330480]
        driver = self.driver
        base_url = self.base_url
        for i in range(0,amount,1):
            record = {}
            print '开始i:',i
            #--------------------多次登录
            #--登出系统
            driver.get("http://login.haodou.com/?do=logout")
            #--登出完毕
            time.sleep(1)
            driver.find_element_by_link_text(u"登录").click()
            driver.find_element_by_id("account").clear()
            #报名帐号
            driver.find_element_by_id("account").send_keys(random.choice(data.avalibleAcct))
            driver.find_element_by_id("password").clear()
            #密码
            driver.find_element_by_id("password").send_keys('123456')
            driver.find_element_by_id("btn_login").click()
            #------------------多次登录结束

            #发布报名
            driver.get("http://wo.haodou.com/topic.php?do=FriendsPub&t_id=%s"%random.choice(topicid))
            time.sleep(0.5)
            f_name = driver.find_element_by_id('f_name')
            f_age = driver.find_element_by_id('f_age')
            f_level = driver.find_element_by_id('f_level')
            f_intro = driver.find_element_by_id('f_intro')
            mobile_code = driver.find_element_by_id('mobile_code')
            mobile = driver.find_element_by_id('mobile')
            friends_submit = driver.find_element_by_id('friends_submit')

            f_name.send_keys('Automation')
            f_age.send_keys(random.randint(10,80))
            Select(f_level).select_by_index(random.randint(0,3))
            f_intro.send_keys(random.choice(data.remarkdata))
            mobile.send_keys('13874900776')
            mobile_code.send_keys('97038')
            friends_submit.click()
            time.sleep(1)




    def tearDown(self):
        print self.report
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
    print 'ok'
