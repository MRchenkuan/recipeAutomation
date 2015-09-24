# coding=utf-8
'''
用户注册的实现
'''
import Base,time,random
from Tools.getCapture import *
from selenium import webdriver
class HaodouAcctRegisterPhone(Base.HaodouAcctRegisterBase):
    def test_HaodouAcctRegisterPhone(self):
        driver = self.driver
        #注册
        for mail in range(0,500):
            driver.get('http://login.haodou.com/register.php')
            driver.find_element_by_link_text('邮箱注册').click()
            mail_account = driver.find_element_by_id('mail_account')
            mail_nickname = driver.find_element_by_id('mail_nickname')
            mail_password = driver.find_element_by_id('mail_password')
            mail_password_retype = driver.find_element_by_id('mail_password_retype')
            mail_valicode = driver.find_element_by_id('mail_valicode')

            mailacc = 'Auto'+('%s'%(time.time()))[-10:]+'@%s.com'%(random.choice(['126','sina','163','qq']))
            mailnick = 'Auto'+('%s'%(time.time()))[-10:]
            mail_account.send_keys(mailacc)
            mail_nickname.send_keys(mailnick)
            mail_password.send_keys('123456')
            mail_password_retype.send_keys('123456')
            mail_valicode.send_keys(getCapture(type='emailreg',ssid=driver.get_cookie('HDSSID').get('value')))

            driver.find_element_by_id('btn_register').click()
            time.sleep(1)
            driver.get('http://login.haodou.com/register.php?doLogout')

            fp = open('FreshHaodouAcct.csv','a')
            fp.write("%s,%s,%s\n"%(mailacc,'123456',mailnick))