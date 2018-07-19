#-*- coding:utf-8 -*-
#author:yupeng
from selenium import webdriver
from common.baseMethod import basePage
from templet_page.pages import glzx_login

url='********************'
username='**********************'
password='***************'
expect_title='管理中心 统一角色访问控制系统 - CMS'

class loginPage(basePage):
    '''创建登录页面类'''
    def open_url(self):
        '''输入url并最大化浏览器'''
        self.open(url)

    def input_username(self):
        '''输入用户名'''
        self.sendkeys(glzx_login.账号输入, username)

    def input_password(self):
        '''输入密码'''
        self.sendkeys(glzx_login.密码输入, password)

    def click_login_button(self):
        '''点击登录按钮'''
        self.click_element(glzx_login.登录按钮)

    def get_gl_title(self):
        '''获取登录后的页面title和预期title进行对比'''
        self.is_title(expect_title)

    def login_glzx(self):
        '''登录流程'''
        self.open_url()
        self.input_username()
        self.input_password()
        self.click_login_button()
        self.get_gl_title()

if __name__ == '__main__':
    driver = webdriver.Firefox()
    login = loginPage(driver)
    login.login_glzx()
# if __name__=='__main__':
#     pass

