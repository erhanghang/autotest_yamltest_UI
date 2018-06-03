#-*- coding:utf-8 -*-
#author:yupeng
'''
读取yaml中的内容
采用os.walk()方法来识别提取文件夹中的.yaml文件的内容，以字典的格式输出
{'baiduPage': {'locators': [{'type': 'id', 'name': '百度输入框', 'value': 'kw'}, {'type': 'id', 'name': '百度搜索按钮', 'value': 'su'}], 'dec': '百度首页'}}
'''
import os
import yaml

#获取包含.yaml文件的路径
curpath=os.path.dirname(os.path.realpath(__file__))
pageelementpath=os.path.join(curpath,'pageelement')

def get_yamlfiles(path=pageelementpath,rule='.yaml'):
    pageelements={}
    for dirname in os.walk(path):
        for i in dirname[2]:
            yamlfile=os.path.join(pageelementpath,i)
            if yamlfile.endswith(rule):
                with open(yamlfile,'r',encoding='utf-8') as f:
                    page=yaml.load(f)
                    pageelements.update(page)
    return pageelements
