#-*- coding:utf-8 -*-
#author:yupeng
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os

class basePage():
    def __init__(self,driver):
        '''初始化'''
        #self.driver=webdriver.Firefox()
        self.driver=driver
        self.timeout=30

    def is_title(self,page_title):
        '''判断登录后的页面是否与期望一致'''
        return page_title in self.driver.title

    def open(self,url):
        '''封装打开浏览器方法'''
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def findelement(self,locator):
        '''显示等待元素出现'''
        element=WebDriverWait(self.driver,self.timeout,0.5).until(EC.presence_of_element_located(locator))
        return element

    def findelements(self,locator):
        '''获取一组元素,返回一个元组'''
        elements=WebDriverWait(self.driver,self.timeout,0.5).until(EC.presence_of_all_elements_located(locator))
        return elements

    def is_text_in_element(self,locator,text):
        '''判断文本是否在页面元素里,存在返回True，不存在返回False'''
        try:
            result=WebDriverWait(self.driver,self.timeout,0.5).until(EC.text_to_be_present_in_element(locator,text))
            return result
        except:
            return False

    def sendkeys(self,locator,text):
        '''输入内容方法'''
        element=self.findelement(locator)
        element.clear()
        element.send_keys(text)

    def click_element(self,locator):
        '''点击元素,只是单个元素'''
        element=self.findelement(locator)
        element.click()

    def focus_element(self,locator):
        '''元素聚焦，出现在浏览器最上方'''
        target=self.findelement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)

    def move_to_element(self,locator):
        '''鼠标悬浮'''
        element=self.findelement(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def move_to_element_and_click(self,locator1,locator2):
        '''鼠标悬浮并点击指定的元素
        locator1  :需要悬浮的位置参数
        locator2  ：点击的位置参数'''
        self.move_to_element(locator1)
        self.click_element(locator2)

    def ele_drag_and_drop_by_offset(self,locator,xoffset, yoffset):
        '''鼠标对元素的拖拽'''
        element=self.findelement(locator)
        ActionChains(self.driver).drag_and_drop_by_offset(element,xoffset, yoffset).perform()

    def select_by_text(self,locator,text):
        '''通过下拉框的可见text来选择需要的内容'''
        element=self.findelement(locator)
        Select(element).select_by_visible_text(text)

    def selects_by_text(self,locator,text,i):
        '''通过下拉框的可见text来选择需要的内容'''
        elements=self.findelements(locator)
        Select(elements[i]).select_by_visible_text(text)

    def alert_accept(self):
        '''处理alert，打印弹窗内容，确定'''
        alert=self.driver.switch_to.alert
        print(alert.text)
        alert.accept()

    def alert_dismiss(self):
        '''处理alert，打印弹窗内容，取消'''
        alert=self.driver.switch_to.alert
        print(alert.text)
        alert.dismiss()

    def is_exist_element(self,locator):
        '''判断元素是否存在，存在进行点击，不存在pass'''
        try:
            self.click_element(locator)
        except:
            pass

    def get_title(self):
        '''获取title'''
        return self.driver.title

    def get_text(self, locator):
        '''获取文本'''
        t = self.findelement(locator).text
        return t

    def get_attribute(self, locator, name):
        '''获取属性'''
        element = self.findelement(locator)
        return element.get_attribute(name)

    def get_current_handle(self):
        '''获取当前窗口句柄'''
        return self.driver.current_window_handle

    def get_all_handles(self):
        '''获取所有窗口句柄'''
        h = self.driver.window_handles
        if len(h) <= 1:
            print("当前只获取到一个窗口句柄，等待3秒后重新获取")
            time.sleep(2)
            h = self.driver.window_handles
        return h

    def switchto_newwindow(self,i=-1):
        '''i为-1时切换到最新的窗口，0时回到原来窗口'''
        handles=self.get_all_handles()
        time.sleep(2)
        self.driver.switch_to.window(handles[i])

    def switchto_frame(self,locator):
        '''切换iframe'''
        self.driver.switch_to.frame(locator)



    def get_screenshot_to_path(self,screenshot_path,screenshot_name):
        '''截图到指定目录下'''
        now=time.strftime("%Y_%m_%d %H_%M_%S")
        try:
            fpath = os.path.join(screenshot_path, "%s%s.png"%(screenshot_name,now))
            self.driver.get_screenshot_as_file(fpath)
            print("screenshot ：%s"%fpath)
        except Exception as a:
            print("Error! screenshot：%s"%a)

    def get_screenasbase64(self):
        return self.driver.get_screenshot_as_base64()

    def get_screenasfile(self, filename):
        return self.driver.get_screenshot_as_file(filename)

    def get_screenaspng(self):
        return self.driver.get_screenshot_as_png()


# if __name__=='__main__':
#     driver=webdriver.Firefox()
#     base=baseBage(driver)
#     base.open('http://www.baidu.com')
#     cur_path=os.path.dirname(os.path.realpath(__file__))
#     parent_path=os.path.dirname(cur_path)
#     screen_path=os.path.join(parent_path,"screenshot_image")
#     base.get_screenshot_to_path(screen_path,"test")

