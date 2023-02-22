"""BBS URL Configuration

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
from django.urls import re_path
from app01 import views
from django.views.static import serve
from BBS import settings



urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$',views.home,name='home'),
    re_path(r'^home/',views.home),
    # re_path(r'^register/',views.register),
    re_path(r'^register/', views.register_ajax,name='register'),
    re_path(r'^login/', views.login,name='login'),
    re_path(r'^edit/password/',views.edit_password,name='edit_password'),
    re_path(r'^logout/',views.logout,name='logout'),
    re_path(r'^get_code/', views.get_code),

    # avatar
    re_path(r'^media/(?P<path>.*)',serve,{'document_root':settings.MEDIA_ROOT}),

    # 点赞
    re_path(r'^up_or_down/',views.up_or_down),

    # 评论
    re_path(r'^comment/',views.comment),

    # 后台管理
    re_path(r'^badmin/', views.badmin,name='badmin'),

    # add article
    re_path(r'^article/',views.add_article,name='add_article'),

    # suibi
    re_path(r'^suibi/',views.add_suibi,name='add_suibi'),

    # upload image
    re_path(r'^upload_image/', views.upload_image, name='upload_image'),

    # edit_article
    re_path(r'^edit_article/(?P<edit_id>\d+)/',views.edit_article,name='edit_article'),

    # delete article
    re_path(r'^delete_article/',views.delete_article,name='delete_article'),

    # set_avatar
    re_path(r'^set_avatar',views.set_avatar,name='set_avatar'),

    # 个人站点
    re_path(r'^(?P<username>\w+)/$',views.site,name='site'),



    # 文章分类
    # re_path(r'^(?P<username>\w+)/category/(d+)/',views.site),
    # # 标签分类
    # re_path(r'^(?P<username>\w+)/tag/(d+)/',views.site),
    # # 日期分类
    # re_path(r'^(?P<username>\w+)/archive/(\w+)',views.site),
    re_path(r'^(?P<username>\w+)/(?P<condition>category|tag|archive)/(?P<param>.*)/',views.site),

    # 文章详情页
    re_path(r'^(?P<username>\w+)/p/(?P<article_id>\d+)/',views.article_detail),
    re_path(r'', views.error),
]

