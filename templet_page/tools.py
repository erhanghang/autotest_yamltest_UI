#-*- coding:utf-8 -*-
#author:yupeng
import os
import jinja2
from templet_page import readyaml

#获取当前路径
curpath=os.path.dirname(os.path.realpath(__file__))

def parseyaml():
    '''通过readyaml读取page页面的中yaml内容，以字典格式展示'''
    pages=readyaml.get_yamlfiles()
    return pages

def get_pagelist(yamlpage):
    '''
    function：把yaml对象转换为需要的页面数据，页面对象--》定位list
    :param yamlpage:yaml解析的对象，dict类型
    :return: {'baiduPage': {'locators': [{'type': 'id', 'value': 'kw', 'name': '百度输入框'}, {'type': 'id', 'value': 'su', 'name': '百度搜索按钮'}], 'dec': '百度首页'}
    '''
    page_object={}
    for page,names in yamlpage.items():
        loc_names=[]
        locs=names['locators']
        for loc in locs:
            loc_names.append(loc['name'])
        page_object[page]=loc_names
    return page_object

def create_pages(page_list):
        '''
        function: 利用jinja2将templetpage模板生成pages.py文件
        :param page_list: get_page_list这个函数返回的page_list列表
                        {'baiduPage': {'locators': [{'type': 'id', 'value': 'kw', 'name': '百度输入框'}, {'type': 'id', 'value': 'su', 'name': '百度搜索按钮'}], 'dec': '百度首页'}
        :return:
        产生pages.py文件
        '''
        templet_loader=jinja2.FileSystemLoader(searchpath=curpath)
        templet_env=jinja2.Environment(loader=templet_loader)
        templetVars={
            'page_list':page_list
        }
        templet=templet_env.get_template('templetpage')
        with open(os.path.join(curpath,'pages.py'),'w',encoding='utf-8') as f:
            f.write(templet.render(templetVars))

if __name__=='__main__':
    yamlpages=parseyaml()
    #print(yamlpages)
    pages=get_pagelist(yamlpages)
    create_pages(pages)

