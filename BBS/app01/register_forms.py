#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: xyz34
# Filer: register_forms.py
# Time: 2022/10/24

from django import forms
from app01 import models


class Register_Forms(forms.Form):
    username = forms.CharField(label='用户名', min_length=5, max_length=16,
                               error_messages={
                                   'min_length': '用户名不能少于5位',
                                   'max_length': '用户名不能超过16位',
                                   'required': '用户名不能为空',
                               },
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control',  'placeholder': 'username'}) #'id': 'floatingInput',
                               )

    password = forms.CharField(label='密码', min_length=8, max_length=16,
                               error_messages={
                                   'min_length': '密码最低不能少于8位',
                                   'max_length': '密码最多不能少于16位',
                                   'required': '密码不能为空'
                               }, widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'password'})#'id': 'floatingPassword',
                               )

    confirm_password = forms.CharField(label='密码', min_length=8, max_length=16,
                                       error_messages={
                                           'min_length': '确认密码最低不能少于8位',
                                           'max_length': '确认密码最多不能少于16位',
                                           'required': '确认密码不能为空'
                                       }, widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'password'}) # 'id': 'floatingPassword',
                                       )

    email = forms.EmailField(label='Email',
                             error_messages={
                                 'required': '邮箱不能为空',
                                 'invalid': '邮箱格式不正确'
                             }, widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'name@example.com'}) # 'id': 'floatingInput',
                             )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        is_exist = models.UserInfo.objects.filter(username=username)
        if is_exist:
            self.add_error('username','用户名已经存在')
        return username

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if not password == confirm_password:
            self.add_error('confirm_password','两次密码不一致')
        return self.cleaned_data



