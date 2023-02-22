#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: xyz34
# Filer: my_auth.py
# Time: 2022年12月3日

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from app01.models import UserToken


class MyTokenAuth(BaseAuthentication):

    def authenticate(self, request):
        token = request.GET.get('token')
        if token:
            token_obj = UserToken.objects.filter(token=token).first()
            if token_obj:
                return token_obj.user, token
            else:
                raise AuthenticationFailed('认证失败')
        else:
            raise AuthenticationFailed('请求地址没有token')


from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        print(f'当前登录的用户是{user}')  # 判断当前登录的用户是谁
        # print(user.is_superuser)
        # print(user.is_authenticated)
        if user.is_superuser:
            return True
        else:
            return False


class User1Permission(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        # print(user.is_authenticated)
        if user.is_authenticated:
            return True
        else:
            return False


