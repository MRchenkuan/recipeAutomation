# coding=utf-8
import random,re
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest,os,time,re
import data,Base


class getSendEmail(Base.BaseSetRecipeAd):
    def test_getSendEmail(self):
        driver = self.driver
        now = time.time()
        #http://www.haodou.com/admin/v2/data/modules/system/showqueue.php
        driver.get(self.base_url + "/admin/v2/data/modules/system/showqueue.php")
        status = driver.find_element_by_id('status')
        Select(status).select_by_visible_text('SendEmail')
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
        p = re.compile(ur'==================[\s\S]*==================([\s\S]*)')
        result = p.findall(search_text.text)
        # script = 'alert(\''+search_text.text+'\')'
        # driver.execute_script(script)
        print result[0]
        # script = 'alert(\''+result+'\')'
        # driver.execute_script(script)
        # print result
        time.sleep(5)





    # def tearDown(self):
    #     self.driver.quit()
    #     self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
    print 'ok'
