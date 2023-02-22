"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from app01 import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('test/',views.test),
#     path('testadd/<int:year>',views.testadd),
# ]

APPEND_SLASH = True

urlpatterns = [
    # re_path(r'^static/$',views.static),
    re_path(r'admin/',admin.site.urls),
    # re_path(r'^test/$',views.test),
    re_path(r'^test/(\d+)/',views.test),
    re_path(r'^testadd/(?P<year>\d+)',views.testadd),
    re_path(r'^$',views.index),
    re_path(r'^func_dsadsadsad/',views.func,name='ooo'),
    re_path(r'^userlist/$',views.userlist),
    # re_path(r'^edit_user/(\d+)/$',views.edit_user,name='xxx'),# 无名分组
    # re_path(r'^edit_user/(?P<xxx>\d+)/$',views.edit_user), #有名分组
    re_path(r'^edit/(\d+)/$',views.edit_user,name='aaa'), #反向解析
    re_path(r'^delete_user/(\d+)/$',views.delete_user,name='deletes_user'),
    # re_path(r'',views.errors),
]
