#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: xyz34
# Filer: bookserializer.py
# Time: 2023年2月3日

from rest_framework.serializers import ModelSerializer
from dv_user import models


class BookSerializer(ModelSerializer):
    class Meta:
        model = models.Books
        fields = "__all__"
