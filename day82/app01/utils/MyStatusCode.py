#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: xyz34
# Filer: MyStatusCode.py
# Time: 2022年12月4日

class MyStatusCode():

    def __init__(self):
        self.code = 20
        self.msg = 'Success'


    @property
    def get_dict(self):
        return self.__dict__


if __name__ == '__main__':
    res = MyStatusCode()
    res.code = 40
    res.msg = 'Fail'
    print(res.get_dict)
