#-*- coding:utf-8 -*-
#author:yupeng
#基础数据
import unittest
from page.glzx_page.basics_data.classTypePage import classTypePage
from page.glzx_page.basics_data.coursePage import coursePage
from selenium import webdriver
from page.glzx_page.glzx_loginPage import loginPage


class guanli_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        '''初始化浏览器，页面实例化'''
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        cls.driver=webdriver.Chrome(chrome_options=option)
        # cls.driver=webdriver.Firefox()
        cls.login=loginPage(cls.driver)
        cls.course=coursePage(cls.driver)
        cls.classtype=classTypePage(cls.driver)
        cls.login.login_glzx()

    def setUp(self):
        '''登录'''
        print('操作基础数据内容')

    def test_query_course_01(self):
        '''查询课程'''
        self.course.click_basicsdata()
        self.course.click_coursenew()
        self.course.input_coursename()
        self.course.select_subject()
        self.course.click_querybutton()
        self.course.assertcourse()

    def test_query_classtype_02(self):
        '''查询班型'''
        self.classtype.click_basicsdata()
        self.classtype.click_classtype()
        self.classtype.input_classtypename()
        self.classtype.select_subject()
        self.classtype.select_laiyuan()
        self.classtype.click_querybutton()
        self.classtype.assertclasstype()


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
