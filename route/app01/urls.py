#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: urls.py
# TIME: 2022/8/29 星期一  周一

from django.contrib import admin
from django.urls import path,re_path

import app01.views

urlpatterns = [
    # re_path(r'^admin/',admin.site.urls),
    # re_path(r'^test/$',app01.views.test,name='xxx'),
    # re_path(r'^test/$',app01.views.ab_json),
    re_path(r'^test/$',app01.views.upload_file),
    re_path(r'^upload_success/',app01.views.upload_success),
]