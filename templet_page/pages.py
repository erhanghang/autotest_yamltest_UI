# -*- coding: utf-8 -*-

from templet_page import tools

pages = tools.parseyaml()

def get_locater(page_name, method_name):
    loc=[]
    locators = pages[page_name]['locators']
    for locator in locators:
        if locator['name'] == method_name:
            loc.append(locator['type'])
            loc.append(locator['value'])
            return tuple(loc)


class glzx_login:
    账号输入 = get_locater('glzx_login', '账号输入')
    密码输入 = get_locater('glzx_login', '密码输入')
    登录按钮 = get_locater('glzx_login', '登录按钮')
    