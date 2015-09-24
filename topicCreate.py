# coding=utf-8
import random
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest,os,time,re
import data

'''由于使用了富文本框，所以很麻烦'''
class newSomeTopic(unittest.TestCase):
    recipeId=[]
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

    def test_1_newSomeTopic(self,amount=40):
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
            #driver.find_element_by_id("account").send_keys('13000000002')
            driver.find_element_by_id("account").send_keys(random.choice(data.useracct))
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys("ckadol")
            #driver.find_element_by_id("password").send_keys("123456")
            driver.find_element_by_id("btn_login").click()
            time.sleep(0.5)
            #------------------多次登录结束

            #发布帖子
            driver.get(base_url + "/topic.php?do=publish")

            #选择小组
            Select(driver.find_element_by_id('group_cat')).select_by_visible_text(u'爱生活')
            time.sleep(0.5)
            Select(driver.find_element_by_id('group_sub_cat')).select_by_visible_text(u'豆友会')

            #-------------------------豆友会部分
            Select(driver.find_element_by_id('group_sub_cat_friends')).select_by_index(1)
            # 选择起止日期
            driver.find_element_by_id('f_start_time').click()
            time.sleep(0.2)
            print driver.find_elements_by_tag_name('iframe')
            frame = driver.find_elements_by_tag_name('iframe')[-1]
            driver.switch_to.frame(frame)
            driver.execute_script('day_Click(2015,4,16);')
            driver.switch_to.default_content()
            driver.find_element_by_id('f_end_time').click()
            driver.switch_to.frame(frame)
            driver.execute_script('day_Click(2015,4,17);')
            driver.switch_to.default_content()
            # 报名人数
            driver.find_element_by_id('joinnum').send_keys('5')
            city = random.choice([
                u'上海',
                u'北京',
                u'哈尔滨',
                u'广州',
                u'厦门',
            ])
            interest = random.choice([
                u'中餐交流',
                u'西点交流',
                u'美食摄影',
                u'亲子活动',
                u'营养课堂',
            ])
            Select(driver.find_element_by_id('f_city')).select_by_visible_text(city)
            Select(driver.find_element_by_id('f_interest')).select_by_visible_text(interest)
            #---------------------------豆友会部分结束
            # 填写标题
            driver.find_element_by_id('title').clear()
            driver.find_element_by_id('title').send_keys((u'%s.%s-%s-报名'%(i+80,city,interest)))

            # #添加超链接 -#用于产生非图片内容
            # driver.find_element_by_class_name('ke-toolbar').find_elements_by_tag_name('span')[40].click()
            # time.sleep(0.5)
            # driver.find_element_by_id('keUrl').send_keys(u'这里是主题内容%s'%time.time())
            # driver.find_element_by_class_name('ke-dialog-footer').find_element_by_tag_name('input').click()
            # time.sleep(0.5)

            #添加图片
            driver.find_element_by_class_name('ke-toolbar').find_elements_by_tag_name('span')[36].click()
            driver.find_element_by_class_name('ke-tabs-ul').find_elements_by_tag_name('li')[1].click()
            driver.find_element_by_name('imgFile').send_keys(random.choice(data.imgLocation))
            driver.find_element_by_class_name('ke-dialog-footer').find_element_by_tag_name('input').click()
            time.sleep(3)

            # #添加文字-由于无法定位到文本编辑器，所以只能通过js脚本添加内容
            frame2 = driver.find_elements_by_tag_name('iframe')[0]
            driver.switch_to.frame(frame2)
            driver.execute_script(u"document.getElementsByTagName('body')[0].innerHTML="
                                  u"'[furl]这里是报名入口文字[/furl]<br>城市：%s<br>兴趣：%s<br>'+document.getElementsByTagName('body')[0].innerHTML"%(city,interest))
            driver.switch_to.default_content()

            #保存发布
            driver.find_element_by_id('publish_btn').click()
            time.sleep(1)




    def tearDown(self):
        print self.report
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
    print 'ok'
