#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: forms_file.py
# TIME: 2022/8/29 星期一  周一

from django import forms

class Upload_File_Form(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
