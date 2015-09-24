# coding=utf-8
import random
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest,os,time,re
import data,Base


'''
    此部分为添加菜谱首页专辑推荐模块的方法
'''

class setRecipeHomeRecomond(Base.BaseSetRecipeAd):
    def test_setRecipeHomeRecomond(self):
        driver = self.driver
        base_url = self.base_url

        url=base_url+'/admin/v2/data/modules/home/collect_top.php'
        driver.get(url)
        modurls=[]
        #添加每一个要修改的项目的url
        for i in range(1,10):
            modurls.append('/admin/v2/data/modules/home/collect_top.php?id=%s'%i)

        albumsid=[
            3105679,
            3105679,
            3105679,
            3105679,
            3105679,
            3105679,
            3105679,
            3105679,
            3105679,
        ]

        #设置过程，修改每一条
        for i,modurl in enumerate(modurls):
            driver.get(base_url+modurl)
            driver.find_element_by_name('CollectId').clear()
            driver.find_element_by_name('CollectId').send_keys(albumsid[i])
            driver.find_element_by_name('Order').clear()
            driver.find_element_by_name('Order').send_keys(i+1)
            driver.find_element_by_name('Title').clear()
            driver.find_element_by_name('Title').send_keys(u'专辑%s - from testAutomation'%(i+1))
            driver.find_element_by_name('Content').clear()
            driver.find_element_by_name('Content').send_keys(random.choice(data.remarkdata))
            time.sleep(1)
            #提交
            driver.find_element_by_id('button4').click()

if __name__ == "__main__":
    unittest.main()
    print 'ok'
