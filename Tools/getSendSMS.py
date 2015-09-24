# coding=utf-8
import random,re
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest,os,time,re
import data,Base


class getSendSMS(Base.BaseSetRecipeAd):
    def test_getSendSMS(self):
        driver = self.driver
        now = time.time()
        #http://www.haodou.com/admin/v2/data/modules/system/showqueue.php
        driver.get(self.base_url + "/admin/v2/data/modules/system/showqueue.php")
        status = driver.find_element_by_id('status')
        Select(status).select_by_visible_text('SendSMS')
        driver.find_element_by_class_name('btn').click()
        echo = driver.find_element_by_id('status_text').text
        p = re.compile(r'[\d]+')
        #得到队列状态码
        statusCode = p.findall(echo)[4]
        pos = driver.find_element_by_id('pos')
        #查询队列值
        pos.clear()
        pos.send_keys(statusCode)
        driver.find_elements_by_class_name('btn')[1].click()
        search_text = driver.find_element_by_id('search_text')
        p = re.compile(ur'验证码是：[\d]+')
        print search_text.text
        code = p.findall(search_text.text)[0]
        script = 'alert(\''+code+'\')'
        driver.execute_script(script)
        print code
        time.sleep(5)





    # def tearDown(self):
    #     self.driver.quit()
    #     self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
    print 'ok'
