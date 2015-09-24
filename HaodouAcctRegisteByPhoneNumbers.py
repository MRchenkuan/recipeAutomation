# coding=utf-8
'''
用户注册的实现
'''
import Base
from selenium import webdriver
class HaodouAcctRegisterPhone(Base.HaodouAcctRegisterBase):
    def test_HaodouAcctRegisterPhone(self):
        driver = self.driver
        driver.get(self.base_url)

        driver.find_element_by_link_text('手机号注册').click()
        phoneBox = driver.find_element_by_id('mobile_account')
        sendMsgButton = driver.find_element_by_id('btn_send_sms')

        captureBox = driver.find_element_by_id('mobile_register_code')

        mobieCodeBox = driver.find_element_by_id('mobile_code')
        nicknameBox = driver.find_element_by_id('mobile_nickname')
        passwordBox = driver.find_element_by_id('mobile_password')
        passwordretry = driver.find_element_by_id('mobile_password_retype')
        regBtn = driver.find_element_by_id('btn_register')

        #填写信息
            #dosomething

        #填写信息 - 完毕


        #找到验证码
        #审批浏览器
        driver2 = webdriver.Firefox()
        driver2.get('http://www.haodou.com/admin/v2/index.php')
            #dosomething
        #找到验证码 - 完毕

        #填写验证码
            #dosomething

        #填写验证码 - 完毕

        #点击确认
        regBtn.click()
