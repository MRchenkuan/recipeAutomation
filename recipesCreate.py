# coding=utf-8
import random
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest,os,time,re
import data


class newSomeRecipes(unittest.TestCase):
    recipeId=[]
    report={}
    def setUp(self):
        self.driver = webdriver.Firefox()
        print 'began'
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

    def test_1_newSomeRecipes(self,amount=15):
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
            driver.find_element_by_id("account").send_keys(random.choice(data.useracct))
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys("ckadol")
            driver.find_element_by_id("btn_login").click()
            #------------------多次登录结束

            #发布菜谱
            #driver.find_element_by_xpath(u"(//a[contains(text(),'发布菜谱')])[2]").click()
            driver.get(base_url + "/recipe/create")
            #填写标题
            rtitle = driver.find_element_by_id("rtitle")
            rtitle.click()
            rtitle.clear()
            rtitle.send_keys((u'%s/%s(半自动)%s%s'%((i+1),amount,random.choice(data.recipeName),time.strftime('%I%M%S')))[0:20])
            # 添加美食图片
            SWFUpload_0 = driver.find_element_by_id("SWFUpload_0")
            SWFUpload_0.click()

            #随机选择图片
            #os.system('c:\\autoUpload.exe %s'%random.choice(data.imgLocation))
            os.system('.\\autoOpen.exe %s'%random.choice(data.imgLocation))
            # 添加内容
            rintro = driver.find_element_by_id("rintro")
            rintro.clear()
            rintro.send_keys(u'fdsafdsafasfdsaasfdsafd')
            driver.find_element_by_id("mgringt_name_1").clear()
            driver.find_element_by_id("mgringt_name_1").send_keys(random.choice(data.mainMaterial))
            driver.find_element_by_id("mgringt_weight_1").clear()
            driver.find_element_by_id("mgringt_weight_1").send_keys("3g")
            driver.find_element_by_id("bugingt_name_3").clear()
            driver.find_element_by_id("bugingt_name_3").send_keys(u"牛油")
            driver.find_element_by_xpath("(//input[@id='bugingt_weight_3'])").clear()
            driver.find_element_by_xpath("(//input[@id='bugingt_weight_3'])").send_keys("2ml")
            Select(driver.find_element_by_id("rreadytime")).select_by_visible_text(u"10-20分钟")
            Select(driver.find_element_by_id("rcooktime")).select_by_visible_text(u"10分钟内")
            Select(driver.find_element_by_id("renjoyuser")).select_by_visible_text(u"3-4人")
            #关闭一行
            #driver.find_element_by_xpath("(//a[contains(text(),'×')])[7]").click()
            try:
                driver.find_element_by_id("SWFUpload_1").click()
                driver.find_element_by_id("SWFUpload_1").click()
                driver.find_element_by_id("SWFUpload_1").click()
                os.system('.\\autoOpen.exe %s'%random.choice(data.imgLocation))
                time.sleep(1)
                driver.find_element_by_id("SWFUpload_1").click()
                driver.find_element_by_id("SWFUpload_1").click()
                driver.find_element_by_id("SWFUpload_1").click()
                os.system('.\\autoOpen.exe %s'%random.choice(data.imgLocation))
                time.sleep(0.8)
                driver.find_element_by_id("SWFUpload_1").click()
                driver.find_element_by_id("SWFUpload_1").click()
                driver.find_element_by_id("SWFUpload_1").click()
                os.system('.\\autoOpen.exe %s'%random.choice(data.imgLocation))
                time.sleep(0.8)
            except Exception,e:
                os.system('.\\autoOpen.exe %s'%random.choice(data.imgLocation))
                print e
                continue
            driver.find_element_by_xpath("//ul[@id='create_step']/li[1]/textarea").clear()
            driver.find_element_by_xpath("//ul[@id='create_step']/li[1]/textarea").send_keys(random.choice(data.intruduce))
            driver.find_element_by_xpath("//ul[@id='create_step']/li[2]/textarea").clear()
            driver.find_element_by_xpath("//ul[@id='create_step']/li[2]/textarea").send_keys(random.choice(data.intruduce))
            driver.find_element_by_xpath("//ul[@id='create_step']/li[3]/textarea").clear()
            driver.find_element_by_xpath("//ul[@id='create_step']/li[3]/textarea").send_keys(random.choice(data.intruduce))
            #填写小技巧
            driver.find_element_by_id("rtips").clear()
            driver.find_element_by_id("rtips").send_keys(u'测试测试测试')
            #填写标签
            driver.find_element_by_id("rtag").clear()
            driver.find_element_by_id("rtag").send_keys(random.choice(data.tag))
            driver.find_element_by_id("save_recipe").click()
            time.sleep(1.5)
            #是否成功
            resMesg = driver.find_element_by_xpath("//p[@class='f14']").text
            print '添加i:',i
            record['rid']=i
            print '添加后i:',record['rid']
            record['time'] = time.strftime('%I-%M-%S')
            record['result']=resMesg
            if resMesg == u'恭喜豆亲！您的菜谱已发布成功。请稍等豆币奖励的系统通知。':
                #提取菜谱id
                print resMesg
                p = re.compile(r'[\d]+')
                recipeId = p.findall(driver.current_url)[0]
                self.recipeId.append(recipeId)
                print self.recipeId
                record['recipeid']=recipeId or u'id获取失败'
                #是否能访问的检查点
                assert not driver.get('http://www.haodou.com/recipe/%s'%recipeId)
                #--登出系统
                driver.get("http://login.haodou.com/?do=logout")
                #--登出完毕
                print '第%s条数据添加完毕'%(i+1)
                self.report[recipeId]=record
            else:
                record['recipeid']='发布失败'
                print u'菜谱发布失败：\n\t原因：%s'%resMesg
                # assert False
            print '结束i:',i


    def test_2_newSomeAcheives(self,amount=50,useracct=data.useracct):

        recipesId=[u'442758', u'442759', u'442760', u'442761', u'442762', u'442763', u'442764', u'442765', u'442766', u'442767', u'442768', u'442769']
        for recipesids in recipesId:
            self.report['%s'%recipesids]={}
        print self.recipeId
        if self.recipeId and len(self.recipeId)!=0:
            recipesId=self.recipeId+recipesId
        print recipesId
        driver = self.driver
        base_url = self.base_url
        for i in range(0,amount,1):
            now = time.time()
            #--------------------多次登录
            recipid = random.choice(recipesId)
            if not self.report['%s'%recipid].has_key('achive'):
                self.report['%s'%recipid]['achive']=[]
            #向报表中添加成果照数据
            driver.get(base_url + "/recipe/photo/%s/"%recipid)
            driver.find_element_by_link_text(u"登录").click()
            account = driver.find_element_by_id("account")
            account.clear()
            account.send_keys(random.choice(useracct))
            password = driver.find_element_by_id("password")
            password.clear()
            password.send_keys("ckadol")
            driver.find_element_by_id("btn_login").click()
            #------------------多次登录结束

            # 上传成果照
            try:
                driver.find_element_by_name('Filedata').click()
                os.system('.\\autoUpload.exe %s'%random.choice(data.imgLocation))
                time.sleep(1)
            except Exception,e:
                os.system('.\\autoUpload.exe %s'%random.choice(data.imgLocation))
                print e
                continue
            # 填写心得
            driver.find_element_by_id('Intro').clear()
            driver.find_element_by_id('Intro').send_keys(u'成果照心得')

            #随便选一个标签
            theme = random.choice(driver.find_element_by_id('showtopic').find_elements_by_tag_name('a'))
            print u'成果照标签：%s'%theme.text
            theme.click()

            # 发布
            try:
                driver.find_element_by_id('addphoto').click()
                time.sleep(1.5)
                print '第%s条数据添加完毕'%(i+1)
            except:
                #是否成功
                resMesg = driver.find_element_by_xpath("//p[@class='f14']").text
                i -= 1
                print u'成果照发布失败：\n\t原因：%s'%resMesg
                driver.get("http://login.haodou.com/?do=logout")
                assert False
            #--登出系统
            self.report['%s'%recipid]['achive'].append(driver.current_url)
            driver.get("http://login.haodou.com/?do=logout")
            #--登出完毕


    def tearDown(self):
        print self.report
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
    print 'ok'
