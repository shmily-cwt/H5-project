#coding:utf-8
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os

class commom():
    
    @staticmethod
    def time_out(self):
        time.sleep(4)
    @staticmethod
    def open_H5(self):
        chromedriver = "D:\\Program Files (x86)\\Python\\chromedriver\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        #去掉ignore-certificate-errors
        options = webdriver.ChromeOptions()  #进入浏览器设置
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        #driver= webdriver.Chrome(chromedriver,chrome_options=options)
        #加载手机模式
        mobile_emulation = { "deviceMetrics": {"width": 375, "height": 667, "pixelRatio": 3.0}, #  定义设备高宽，像素比 
                    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X)" # 通过ua来模拟 
                    "AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"} 
        chrome_options = Options() 
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        driver = webdriver.Chrome(chromedriver,chrome_options = chrome_options)
        driver.maximize_window()  
        return driver
    
    @staticmethod
    def check_Text(self,text_xpath):
        driver = self.driver
        actual_Result = driver.find_element_by_xpath(text_xpath).text
        return actual_Result
        
        
        
         