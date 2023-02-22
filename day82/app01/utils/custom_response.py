#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: xyz34
# Filer: custom_response.py
# Time: 2022年12月9日

from rest_framework.response import Response
from app01.utils.MyStatusCode import MyStatusCode

class CutomResponse(Response):

    # def __init__(self, code=200, msg="success", data=None, status=None, headers=None, **kwargs):
    #     dic = {'code': code, 'msg': msg, 'data': data}
    #     if data:
    #         dic = {'code': code, 'msg': msg, 'data': data}
    #     dic.update(kwargs)
    #     super().__init__(data=dic, status=status, headers=headers)
    # status_code = MyStatusCode()

    def __init__(self, **kwargs):
        self.code = 10
        self.msg = 'success'
        self.data = None
        self.status = None
        self.headers = None

        status_dic = {'code': self.code, 'msg': self.msg, 'data': self.data}
        if self.data:
            status_dic = {'code': self.code, 'msg': self.msg, 'data': self.data}

        status_dic.update(kwargs)
        super().__init__(data=status_dic, status=self.status, headers=self.headers)
