#coding:utf-8
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from page import login_page,home_page
from public import setting,common
import unittest
import os


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = common.commom.open_H5(self)
        
    def test_login(self):
        '''测试登录'''
        self.driver = common.commom.open_H5(self)
        self.driver.get(setting.data.home_url)
        home_page.First_page.click_my(self)
        login_page.index_page.input_username(self,setting.data.username)
        login_page.index_page.input_password(self,setting.data.password)
        login_page.index_page.click_submit(self)
        common.commom.time_out(self)
        login_title = "//div[@class='head-info-title']"
        login_name = common.commom.check_Text(self,login_title)
        if login_name == "shmily":
            print "success"
        
        
        
    def tearDown(self):
        driver = self.driver
        driver.quit()

# if __name__ == '__main__':
#     unittest.main()        
        