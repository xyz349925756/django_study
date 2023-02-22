#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: xyz34
# Filer: __init__.py
# Time: 2022/10/22

import importlib
import notify_setting

def send_all(content):
    for path_str in notify_setting.NOTIFY_LIST:
        module_path,class_name = path_str.rsplit('.',maxsplit=1)
        # 从右到左按.分割一次就结束
        module = importlib.import_module(module_path)
        cls = getattr(module,class_name)   # 反射
        obj = cls()
        obj.send(content)