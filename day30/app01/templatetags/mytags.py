#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: mytags.py
# TIME: 2022/9/2 星期五  周五

from django import template

register = template.Library()

@register.filter(name='boby')
def my_sum(v1,v2):
    return v1 + v2

# 多个参数
@register.simple_tag(name='plus')
def index(a,b,c,d):
    return f'{a}-{b}-{c}-{d}'


# 自定义inclusion_tag
@register.inclusion_tag('left_ht.html')
def left(n):
    data = [f'第{i}项' for i in range(n)]
    # data = ['第{}项'.format(i) for i in range(n)]
    # 第一种
    return {'data':data}

    # return locals()