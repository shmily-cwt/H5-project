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
        
    def test_first_function(self):
        '''测试登录'''
        self.driver = self.driver
        self.driver.get(setting.data.home_url)
        home_page.First_page.click_bailian_shopping(self)
        common.commom.time_out(self)
        self.driver.back()
        home_page.First_page.click_first_medicine(self)
        common.commom.time_out(self)
        self.driver.back()
        home_page.First_page.click_gift_card(self)
        common.commom.time_out(self)
        self.driver.back()
        home_page.First_page.click_digital(self)
        common.commom.time_out(self)
        self.driver.back()
        home_page.First_page.click_chinese(self)
        common.commom.time_out(self)
        self.driver.back()
        home_page.First_page.click_recharge(self)
        common.commom.time_out(self)
        self.driver.back()
        home_page.First_page.click_parking(self)
        common.commom.time_out(self)
        self.driver.back()
        home_page.First_page.click_coupons(self)
        common.commom.time_out(self)
        self.driver.back()
        home_page.First_page.click_Premium_group(self)
        common.commom.time_out(self)
        self.driver.back()
        home_page.First_page.click_basket(self)
        common.commom.time_out(self)
        self.driver.back()
        
        
        
            
    def tearDown(self):
        driver = self.driver
        driver.quit()

# if __name__ == '__main__':
#     unittest.main() 