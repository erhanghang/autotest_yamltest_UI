#-*- coding:utf-8 -*-
#author:yupeng
#机构管理
import unittest

from page.glzx_page.glzx_loginPage import loginPage
from selenium import webdriver

from page.glzx_page.ins_manage.insPage import insPage


class guanli_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        '''初始化浏览器，页面实例化'''
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        cls.driver=webdriver.Chrome(chrome_options=option)
        # cls.driver=webdriver.Firefox()
        cls.login=loginPage(cls.driver)
        cls.ins=insPage(cls.driver)
        cls.login.login_glzx()

    def setUp(self):
        '''登录'''
        print('操作机构内容')

    def test_query_ins_01(self):
        '''查询机构'''
        self.ins.click_insmanage()
        self.ins.click_ins()
        self.ins.input_insname()
        self.ins.select_instype()
        self.ins.click_querybutton()
        self.ins.assertinsname()


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
