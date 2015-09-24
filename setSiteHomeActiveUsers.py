# coding=utf-8
import random
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest,os,time,re
import data,Base


'''
    此部分为添加全站首页添加活跃用户模块的方法
'''

class setSiteHomeActiveUsers(Base.BaseSetRecipeAd):
    def test_setSiteHomeActiveUsers(self):
        driver = self.driver
        base_url = self.base_url
        url=base_url+'/admin/v2/data/modules/home/setindex.php?key=index_topuser'
        driver.get(url)
        modurls=[]
        #添加每一个要修改的项目的url
        for i in range(1,7):
            modurls.append('/admin/v2/data/modules/home/setindex.php?key=index_topuser&id=%s'%i)

        userid=[
            497679,
            4040919,
            3301397,
            2985494,
            136135,
            4041054,
            4041062,
            2539239,
            4041107,

        ]

        #设置过程，修改每一条
        for i,modurl in enumerate(modurls):
            driver.get(base_url+modurl)
            driver.find_element_by_name('UserId').clear()
            driver.find_element_by_name('UserId').send_keys(userid[i])
            driver.find_element_by_name('order').clear()
            driver.find_element_by_name('order').send_keys(i+1)
            time.sleep(1)
            #提交
            driver.find_element_by_id('button4').click()

if __name__ == "__main__":
    unittest.main()
    print 'ok'
