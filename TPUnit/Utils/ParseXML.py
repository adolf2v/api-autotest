#!coding:utf8
from bs4 import BeautifulSoup
from bs4 import NavigableString
import os

"""
author:weiqiang.liu
date:2016/09/02
"""
"""用来解析指定格式的xml,获取测试所需要的
接口名称,请求方法,用例描述,测试数据,相应状态码
相应返回的json数据的code,预期内容"""


class ParseXml():
    # 类的初始化,传入一个文件路径,并声明一个list类型用来后边储存程序返回的结果
    def __init__(self, path):
        self.path = path
        self.apiList = []

    # 解析函数
    def parse(self):
        # 判断文件是否存在
        if os.path.exists(self.path):
            # 用with语句读取文件,并用BeautifulSoup 对文件内容进行解析,提取所需要的数据
            with open(self.path, 'rb') as fb:
                bs = BeautifulSoup(fb.read(), 'xml')
                for item in bs.testcase:
                    # print item.name
                    # print type(item)
                    a = {}
                    b = []
                    if not isinstance(item, NavigableString):
                        a['api'] = item.api.text
                        a['method'] = item.method.text
                        a['desc'] = item.desc.text
                        a['data'] = item.data.text
                        a['retcode'] = item.assert1.retcode.text
                        a['status'] = item.assert1.status.text
                        con = bs.find_all('content')
                        if con:
                            for ite in bs.find_all('content'):
                                b.append(ite['id'] + ':' + ite.text)
                            a['content'] = b
                        else:
                            a['content'] = []
                        self.apiList.append(a)
                self.apiList.append(bs.testcase['name'])
            return self.apiList
        else:
            return u'%s:文件不存在'%self.path
