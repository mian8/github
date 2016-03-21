#百度访问

# -*- coding: utf-8 -*-
from selenium import webdriver          #导入selenium中的webdriver
from selenium.webdriver.common.keys import Keys    #导入虚拟键盘模块
from selenium.webdriver.common.action_chains import ActionChains    #导入虚拟鼠标
import time

browser=webdriver.Firefox()             #打开Firefox浏览器

browser.get('http://www.baidu.com')     #打开网页
browser.find_element_by_id('kw').clear()#清空输入框
browser.find_element_by_id('kw').send_keys('斯大林')#输入文本
browser.find_element_by_id('su').click()#点击搜索
browser.maximize_window() #浏览器窗口最大化
time.sleep(3)
browser.quit()