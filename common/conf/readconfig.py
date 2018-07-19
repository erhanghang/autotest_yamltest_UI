#-*- coding:utf-8 -*-
#author:yupeng

import os
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")

class ReadConfig(object):
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath, encoding='utf-8')

    def get_glzx_login(self, name):
        '''获取后台登录信息'''
        value = self.cf.get('glzx_login', name)
        return value

    def get_axx_login(self, name):
        '''获取email信息'''
        value = self.cf.get('axx_login', name)
        return value

    def get_email(self, name):
        '''获取email信息'''
        value = self.cf.get("email", name)
        return value

    def get_http(self, name):
        '''获取baseurl信息'''
        value = self.cf.get("http", name)
        return value

    def get_url(self, name):
        '''获取接口url信息'''
        value = self.cf.get("url", name)
        return value

    def get_db(self, name):
        '''获取数据库信息'''
        value = self.cf.get("database", name)
        return value

if __name__ == '__main__':
    rc = ReadConfig()
    glzx = rc.get_http('glzx')
    print(glzx)
