#!coding:utf8

"""
author:weiqiang.liu
date:2016/09/02
"""

import json
import sys

import requests

from Utils.ParseXML import ParseXml
from Utils.Report import Report

reload(sys)
sys.setdefaultencoding("utf-8")
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}


class RequestAndAssert():
    def __init__(self, data=[]):
        self.data = data

    def post(self, api, data):
        try:
            res = requests.post(api, data=data, headers=headers, timeout=10)
            return res
        except:
            print "Request post failed"

    def get(self, api, data, ):
        try:
            res = requests.get(api, params=data, headers=headers, timeout=10)
            # print res
            return res
        except:
            print "Request get failed"

    def Assert(self, Obj, desc, method, api, data, status, retcode, content):
        print 'start test %s'%desc
        if method == "post":
            res = self.post(api, data)
        elif method == "get":
            res = self.get(api, data)
        else:
            print "Don't support this method!"
        if res.status_code == int(status):
            if res.json().get('code') == int(retcode):
                if content:
                    result = content[0].split(':')
                    if res.json().get(result[0]) == result[1]:
                        Obj.addPass(desc)
                    else:
                        Obj.addFail(desc, u'验证失败%s' % res.json().get(result[0]))
            else:
                Obj.addFail(desc, u'服务器返回失败%s' % res.json().get('text'))

        else:
            Obj.addFail(desc, u'服务器错误%s' % res.status_code)
        print 'end test %s'%desc

    def run(self):
        filename = self.data[-1]
        print filename
        self.data.pop()
        with open(r'%s.html' % filename, 'wb') as fp:
            rr = Report(fp)
            rr.startHtml()
            for item in self.data:
                method = item.get('method')
                api = item.get('api')
                data = json.loads(item.get('data'))
                content = item.get('content')
                status = item.get('status')
                retcode = item.get('retcode')
                desc = item.get('desc')
                self.Assert(rr, desc, method, api, data, status, retcode, content)

            rr.endHtml()





if __name__ == "__main__":
    px = ParseXml('/Users/shouwang/PycharmProjects/TPUnit/case.xml')
    data = px.parse()
    if isinstance(data,list):
        raa = RequestAndAssert(data)
        raa.run()
    else:
        print data
