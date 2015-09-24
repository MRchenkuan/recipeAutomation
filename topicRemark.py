# coding=utf-8
import random
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest,os,time,re
import data


class remarkRecipes(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        print 'yes'
        self.driver.implicitly_wait(30)
        print self.driver.title
        self.base_url = "http://www.haodou.com"
        self.verificationErrors = []
        self.accept_next_alert = True

        # #---------------------------一次登录
        # driver = self.driver
        # driver.get(self.base_url + "/recipe")
        # driver.find_element_by_link_text(u"登录").click()
        # driver.find_element_by_id("account").clear()
        # driver.find_element_by_id("account").send_keys("393667111@qq.com")
        # driver.find_element_by_id("password").clear()
        # driver.find_element_by_id("password").send_keys("ckadol")
        # driver.find_element_by_id("btn_login").click()
        # #---------------------------一次登录结束

    def test_remark(self,amount=100,useracct=data.useracct):

        driver = self.driver
        base_url = self.base_url
        for i in range(0,amount,1):
            now = time.time()
            #--------------------多次登录
            driver.get("http://login.haodou.com/?do=logout")
            driver.find_element_by_link_text(u"登录").click()
            driver.find_element_by_id("account").clear()
            driver.find_element_by_id("account").send_keys(random.choice(useracct))
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys("ckadol")
            driver.find_element_by_id("btn_login").click()
            #------------------多次登录结束


            for j in range(1,3):
                driver.get('http://group.haodou.com/topic-%s.html'%random.choice(range(330356,330396)))
                #driver.get('http://group.haodou.com/topic-%s.html'%330253)
                frame = driver.find_element_by_class_name('ke-edit-iframe')
                driver.switch_to.frame(frame)
                driver.execute_script(u"document.body.innerHTML='%s -- Automation'"%(random.choice(data.remarkdata)+time.strftime('%Y-%m-%d-%I:%M:%S')))
                driver.switch_to.default_content()
                driver.find_element_by_name('reply_submit').click()
                time.sleep(1)
                print u'评论',i

            # #是否成功
            # try:
            #     resMesg = driver.find_element_by_xpath("//p[@class='f14']").text
            # except:
            #     resMesg =u'评论成功'
            # print resMesg
        driver.get("http://login.haodou.com/?do=logout")
        time.sleep(1.5)


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
    print 'ok'
