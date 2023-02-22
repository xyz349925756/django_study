from django.urls import re_path
from app01 import views

urlpatterns = [
    re_path(r'^users/', views.UserInfos.as_view()),
    re_path(r'^user/(?P<pk>\d+)/', views.UserInfos.as_view()),
    re_path(r'^login/',views.Login.as_view()),
    re_path(r'^order/',views.Order.as_view()),

    re_path(r'^lo/',views.LoginView.as_view()),
    re_path(r'^or/',views.OrderView.as_view()),
]
