# coding=utf-8
import random
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest,os,time,re
import data,Base

'''
    此部分为菜谱首页添加图片轮拨slider的方法
'''
class setRecipeHomeSlider(Base.BaseSetRecipeAd):
    def test_setrecipehomeslider(self):
        driver = self.driver
        base_url = self.base_url

        #这里填写要设置哪几个
        url=base_url+'/admin/v2/data/modules/ads/recipead.php?do=edit&id=7'
        driver.get(url)

        # --------------在这里开始填写要添加的数据，默认为随机,所添加的数据条目不能大于5
        info = {
            'name':u'菜谱首页滚动图-from testAutomation',
            'status':u'显示',
            'data':[
                {
                    'content':u'描述文字--from testAutomation',
                    'link':'http://www.haodou.com/recipe/%s'%(random.choice(data.recipids)),
                    'Limg':random.choice(data.imgLocation),
                    'Simg':random.choice(data.imgLocation),
                },
                {
                    'content':u'描述文字--from testAutomation',
                    'link':'http://www.haodou.com/recipe/%s'%(random.choice(data.recipids)),
                    'Limg':random.choice(data.imgLocation),
                    'Simg':random.choice(data.imgLocation),
                },
                {
                    'content':u'描述文字--from testAutomation',
                    'link':'http://www.haodou.com/recipe/%s'%(random.choice(data.recipids)),
                    'Limg':random.choice(data.imgLocation),
                    'Simg':random.choice(data.imgLocation),
                },
                {
                    'content':u'描述文字--from testAutomation',
                    'link':'http://www.haodou.com/recipe/%s'%(random.choice(data.recipids)),
                    'Limg':random.choice(data.imgLocation),
                    'Simg':random.choice(data.imgLocation),
                },
                {
                    'content':u'描述文字--from testAutomation',
                    'link':'http://www.haodou.com/recipe/%s'%(random.choice(data.recipids)),
                    'Limg':random.choice(data.imgLocation),
                    'Simg':random.choice(data.imgLocation),
                },
            ],
            'startime':None,
            'endtime':None,
            'intro':u'设置菜谱首页slider - from testAutomation',
        }
        # ----------------------默认数据准备完毕

        # ----------------------------------------- 元素获取开始
        #页面基本元素
        name = driver.find_element_by_id('Name')
        status = driver.find_element_by_id('Status')
        #一共添加几条
        howmuchtr=len(info['data'])
        tabletr=[]
        for i in range(0,howmuchtr):
            tabletr.append(driver.find_element_by_id('data_%s'%i))
        #页面内容部分元素
        table=[]
        for eachtr in tabletr:
            table.append({
                'content':eachtr.find_element_by_tag_name('td').find_element_by_tag_name('textarea'),
                'link':eachtr.find_elements_by_tag_name('td')[1].find_element_by_tag_name('input'),
                'Limg':eachtr.find_elements_by_tag_name('td')[2].find_elements_by_tag_name('input')[1],
                'Simg':eachtr.find_elements_by_tag_name('td')[3].find_elements_by_tag_name('input')[0],
            })

        #开始结束时间控件
        startime = driver.find_element_by_id('StartTime')
        endtime = driver.find_element_by_id('EndTime')
        #描述文字
        intro =  driver.find_element_by_name('Intro')
        # ------------------------------------ 元素获取结束


        # --------------------------------- 设置过程开始
        name.clear()
        name.send_keys(info['name'])
        Select(status).select_by_visible_text(info['status'])
        for i,eachdata in enumerate(table):
            eachdata['content'].clear()
            eachdata['content'].send_keys(info['data'][i]['content'])
            eachdata['link'].clear()
            eachdata['link'].send_keys(info['data'][i]['link'])
            #此处可能会要运行上传脚本
            eachdata['Limg'].send_keys(info['data'][i]['Limg'])
            eachdata['Simg'].send_keys(info['data'][i]['Simg'])
        info['startime'] and startime.send_keys(info['startime'])
        info['endtime'] and endtime.send_keys(info['endtime'])
        #time.sleep(10)
        driver.find_element_by_id('button4').click()
        # --------------------------------- 设置过程结束

if __name__ == "__main__":
    unittest.main()
    print 'ok'
