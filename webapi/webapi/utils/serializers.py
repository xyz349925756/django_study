#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: xyz34
# Filer: serializers.py
# Time: 2023年2月2日

from rest_framework.serializers import ModelSerializer
from webapi.apps.user.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'username,email,phone_num,last_login'

