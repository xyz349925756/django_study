#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: xyz34
# Filer: MyStaticCode.py
# Time: 2022年11月21日


class MyStaticCode():

    def __init__(self):
        self.status = 100
        self.msg = 'success'

    @property
    def get_dict(self):
        return self.__dict__



if __name__ == '__main__':
    res = MyStaticCode()
    res.status = 101
    res.msg = 'fail'
    print(res.get_dict)