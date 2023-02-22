#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: xyz34
# Filer: response.py
# Time: 2023年1月18日

from rest_framework.response import Response


class APIResponse(Response):
    def __init__(self, status=0, msg='ok', http_status=None, headers=None, exception=False, **kwargs):
        data = {
            'status': status,
            'msg': msg
        }

        if kwargs:
            data.update(kwargs)
        super().__init__(data=data, status=http_status, headers=headers, exception=exception)
