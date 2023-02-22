"""startproject URL Configuration

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
from django.urls import path, re_path

import app01.views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', app01.views.index),
    re_path(r'^book/list/', app01.views.book_list, name='book_list'),
    re_path(r'^publish/list/', app01.views.publish_list, name='publish_list'),
    re_path(r'^author/list/',app01.views.author_list,name='author_list'),
    re_path(r'^book/add/',app01.views.book_add,name='book_add'),
    re_path(r'^edit/(?P<edit_id>\d+)/',app01.views.edit_book,name='edit_book'),
    re_path(r'^del/(\d+)/',app01.views.del_book,name='book_del'),
]
