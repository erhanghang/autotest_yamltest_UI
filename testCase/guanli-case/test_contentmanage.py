#-*- coding:utf-8 -*-
#author:yupeng
#机构管理
import unittest

from page.glzx_page.glzx_loginPage import loginPage
from selenium import webdriver
from page.glzx_page.content_manage.lessonmanagePage import lessonmanagePage


class guanli_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        '''初始化浏览器，页面实例化'''
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        cls.driver=webdriver.Chrome(chrome_options=option)
        # cls.driver=webdriver.Firefox()
        cls.login=loginPage(cls.driver)
        cls.lessonmanage=lessonmanagePage(cls.driver)
        cls.login.login_glzx()

    def setUp(self):
        '''登录'''
        print('操作机构内容')

    def test_upfile_01(self):
        '''课节管理中上传课件'''
        self.lessonmanage.click_contentmanage()
        self.lessonmanage.click_lessonmanage()
        self.lessonmanage.upfile()



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
