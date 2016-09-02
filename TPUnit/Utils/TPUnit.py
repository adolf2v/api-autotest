#coding:utf-8

from Utils.RequestAndAssert import RequestAndAssert
from Utils.ParseXML import ParseXml
import os


class TPUnit():
    def __init__(cls,filename=[]):
        cls.filename=filename
    def run(cls):
        for item in cls.filename:
            newpath=os.path.join(os.path.abspath('.'),item)
            px=ParseXml(newpath)
            data=px.parse()
            if isinstance(data,list):
                raa = RequestAndAssert(data)
                raa.run()
            else:
                print data


# for item in  os.listdir(os.getcwd()+"/case/"):
#     path = os.path.abspath()
#     px=ParseXml(path)
#     data=px.parse()
#     if isinstance(data,list):
#         raa = RequestAndAssert(data)
#         raa.run()
#     else:
#         print data
if __name__=='__main__':
    tpu=TPUnit(['case/case.xml'])
    tpu.run()