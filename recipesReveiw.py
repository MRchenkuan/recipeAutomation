# coding=utf-8
import random
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest,os,time,re
import data,Base


class newSomeRecipes(Base.BaseSetRecipeAd):

    def test_reveiwRcipes(self,amount=50,which=1):

        driver = self.driver
        base_url = self.base_url
        for i in range(0,amount,1):
            now = time.time()
            driver.get(self.base_url + "/admin/v2/data/modules/recipe/recipes.php")
            driver.find_element_by_xpath('html/body/table[2]/tbody/tr[%s]/td/a[1]'%(which*2+2)).click()
            driver.find_element_by_xpath("(//*[@type='radio'])[%s]"%(1+i%5)).click()
            driver.find_element_by_xpath("(//*[@type='radio'])[%s]"%(6+i%3)).click()
            driver.find_element_by_class_name('btn').click()
            print i,'is completed'



            # #是否成功
            # resMesg = driver.find_element_by_xpath("//p[@class='f14']").text
            # print resMesg
            # if resMesg == u'恭喜豆亲！您的菜谱已发布成功。请稍等豆币奖励的系统通知。':
            #     #提取菜谱id
            #     p = re.compile(r'[\d]+')
            #     recipeId = p.findall(driver.current_url)[0]
            #     print recipeId or u'id获取失败'
            #     #是否能访问的检查点
            #     assert not driver.get('http://www.haodou.com/recipe/%s'%id)
            #     time.sleep(1)
            #     driver.get("http://login.haodou.com/?do=logout")
            #     print '第%s条数据添加完毕'%(i+1)
            # else:
            #     i -= 1
            #     print u'菜谱发布失败：\n\t原因：%s'%resMesg
            #     assert False


    # def tearDown(self):
    #     self.driver.quit()
    #     self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
    print 'ok'
