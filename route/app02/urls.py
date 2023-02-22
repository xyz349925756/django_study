#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: urls.py
# TIME: 2022/8/29 星期一  周一

from django.contrib import admin
from django.urls import path,re_path

from app02 import views

urlpatterns = [
    # re_path(r'^admin/$',admin.site.urls),
    re_path(r'^test/$',views.test)
]