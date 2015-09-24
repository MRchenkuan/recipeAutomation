# coding=utf-8
import random
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest,os,time,re
import data,Base


'''
    此部分为添加话题推荐的方法
'''

class setRecipeHomeRecomond(Base.BaseSetRecipeAd):
    def test_setRecipeHomeRecomond(self):
        driver = self.driver
        base_url = self.base_url

        url=base_url+'/admin/v2/data/modules/home/topic.php'
        driver.get(url)
        modurls=[]
        #添加每一个要修改的项目的url
        for i in range(1,4):
            modurls.append('/admin/v2/data/modules/home/topic.php?id=%s'%i)

        #准备基本信息
        topicIds=[
            265734,
            265735,
            265736,
        ]
        recomondedTopicInfo=[]
        for topicId in topicIds:
            recomondedTopicInfo.append({
                'img':random.choice(data.imgLocation),
                'title':u'推荐话题1fromTestAutomation',
                'content':u'%s-from TestAutomation'%random.choice(data.remarkdata),
                'link':'http://group.haodou.com/topic-%s.html'%topicId,
                'topicid':topicId,
            })



        #设置过程，修改每一条
        for i,modurl in enumerate(modurls):
            driver.get(base_url+modurl)
            driver.find_element_by_id('Order').clear()
            driver.find_element_by_id('Order').send_keys((i+1))
            driver.find_element_by_id('imgfile').send_keys(recomondedTopicInfo[i]['img'])
            driver.find_element_by_id('Title').clear()
            driver.find_element_by_id('Title').send_keys(recomondedTopicInfo[i]['title'])
            driver.find_element_by_id('Content').clear()
            driver.find_element_by_id('Content').send_keys(recomondedTopicInfo[i]['content'])
            driver.find_element_by_id('Link').clear()
            driver.find_element_by_id('Link').send_keys(recomondedTopicInfo[i]['link'])
            driver.find_element_by_id('TopicId').clear()
            driver.find_element_by_id('TopicId').send_keys(recomondedTopicInfo[i]['topicid'])
            time.sleep(1)
            #提交
            driver.find_element_by_id('button4').click()

if __name__ == "__main__":
    unittest.main()
    print 'ok'
