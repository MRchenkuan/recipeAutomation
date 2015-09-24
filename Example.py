# coding=utf-8
import random
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest,os,time,re
import data


class newSomeRecipes(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        print 'yes'
        self.driver.implicitly_wait(30)
        print self.driver.title
        self.base_url = "http://www.haodou.com"
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

    def test_newSomeRecipes(self,amount=10,useracct=data.useracct):

        driver = self.driver
        base_url = self.base_url
        for i in range(0,amount,1):
            now = time.time()
            #--------------------多次登录
            driver.get(base_url + "/recipe/create")
            driver.find_element_by_link_text(u"登录").click()
            driver.find_element_by_id("account").clear()
            driver.find_element_by_id("account").send_keys(random.choice(useracct))
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys("ckadol")
            driver.find_element_by_id("btn_login").click()
            #------------------多次登录结束


            # do something


            #是否成功
            resMesg = driver.find_element_by_xpath("//p[@class='f14']").text
            print resMesg
            if resMesg == u'恭喜豆亲！您的菜谱已发布成功。请稍等豆币奖励的系统通知。':
                #提取菜谱id
                p = re.compile(r'[\d]+')
                recipeId = p.findall(driver.current_url)[0]
                print recipeId or u'id获取失败'
                #是否能访问的检查点
                assert not driver.get('http://www.haodou.com/recipe/%s'%id)
                time.sleep(1)
                driver.get("http://login.haodou.com/?do=logout")
                print '第%s条数据添加完毕'%(i+1)
            else:
                i -= 1
                print u'菜谱发布失败：\n\t原因：%s'%resMesg
                assert False


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
    print 'ok'
