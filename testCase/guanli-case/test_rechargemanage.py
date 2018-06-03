#-*- coding:utf-8 -*-
#author:yupeng

import unittest
from page.glzx_page.glzx_loginPage import loginPage
from selenium import webdriver
from page.glzx_page.recharge_manage.inslistPage import inslistPage


class guanli_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        option=webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        cls.driver=webdriver.Chrome(chrome_options=option)
        cls.login=loginPage(cls.driver)
        cls.inslist=inslistPage(cls.driver)
        cls.login.login_glzx()

    def setUp(self):
        '''登录'''
        print('操作销售管管理内容')

    def test_insmanage(self):
        '''销售管理客户管理查询'''
        self.inslist.click_rechargemanage()
        self.inslist.click_inslist()
        self.inslist.select_instype()
        self.inslist.input_insname()
        self.inslist.click_querybutton()
        self.inslist.assertinsname()

    def tearDown(self):
        '''删除浏览器cookies并刷新'''
        #self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        '''关闭浏览器以及进程'''
        cls.driver.quit()


if __name__=='__main__':
    unittest.main()


