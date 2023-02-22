"""day35 URL Configuration

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
from django.urls import path,re_path
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 注册
    re_path(r'^register/$',views.regedit),
    re_path(r'register/admin/$',views.regedit_admin),
    re_path(r'^$',views.index),
    re_path(r'^login/',views.login),
    re_path(r'^accounts/login/',views.login),
    re_path(r'^home/',views.home),
    re_path(r'^edit/password/',views.edit_password),
    re_path(r'^loginout/',views.logout),
]
