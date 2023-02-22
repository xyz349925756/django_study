#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: xyz34
# Filer: urls.py
# Time: 2023年1月22日


from django.urls import path,re_path,include
from utils.router import router

from .views import UserViewSet

# 注册ViewSet的路由
# router.register()

urlpatterns = [
    re_path(r'',include(router.urls)),
    re_path(r'^username/',UserViewSet.as_view()),
]