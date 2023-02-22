"""day82 URL Configuration

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

from rest_framework import routers

from app01 import views

router = routers.SimpleRouter()
router.register('userinfo',views.User1View)

# router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path(r'^user1/$', views.User1View.as_view(actions={'get': 'list', 'post': 'create'})),
    # re_path(r'^user1/(?P<pk>\d+)',views.User1View.as_view(actions={'get':'retrieve','put':'update','delete':'destroy'})),
    re_path(r'^login/',views.LoginView.as_view()),
    re_path(r'^test/$',views.TestView.as_view()),
    re_path(r'^test1/$',views.Test1View.as_view()),  # admin后台管理权限
    re_path(r'^test2/$',views.Test2View.as_view()),
    re_path(r'^test3/$',views.Test3View.as_view()),
    re_path(r'^test4/$',views.Test4View.as_view()),
    re_path(r'^test5/$',views.Test5View.as_view()),
    re_path(r'^test6/$',views.Test6View.as_view()),
    re_path(r'^userlist/',views.UserList.as_view()),
    re_path(r'^userlist1/',views.User1List.as_view()),
    re_path(r'^test7/',views.TestView7.as_view()),



]

urlpatterns += router.urls