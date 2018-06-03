#-*- coding:utf-8 -*-
#author:yupeng
import unittest
from selenium import webdriver
from page.glzx_page.glzx_loginPage import loginPage


class guanli_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        '''初始化浏览器，的呢牢固页面实例化'''
        cls.driver=webdriver.Firefox()
        cls.login=loginPage(cls.driver)

    def setUp(self):
        '''登录'''
        self.login.login_glzx()

    def test_01(self):
        pass


    def tearDown(self):
        '''删除浏览器cookies并刷新'''
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        '''关闭浏览器以及进程'''
        cls.driver.quit()


if __name__=='__main__':
    unittest.main()