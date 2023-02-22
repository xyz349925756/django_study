#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: xyz34
# Filer: sidebar.py
# Time: 2022/11/2

from django import template
from app01 import models
from django.db.models import Count
from django.db.models.functions import TruncMonth

register = template.Library()

@register.inclusion_tag('left_menu.html')
def left_menu(username):
    user_obj = models.UserInfo.objects.filter(username=username).first()
    blog = user_obj.blog
    # 文章分类
    category_list = models.Category.objects.filter(blog=blog).annotate(count_num=Count('article__id')).values_list(
        'name', 'count_num', 'id')
    # values  [{'id': 1, 'name': 'python', 'blog_id': 1, 'count_num': 1}, ]
    # values_list [(1, 'python', 1, 1), (2, 'html', 1, 1), (3, 'bash', 1, 1)]
    # print(category_list)
    tag_list = models.Tag.objects.filter(blog=blog).annotate(count_num=Count('article__id')).values_list('name',
                                                                                                         'count_num',
                                                                                                         'id')
    # values [{'name': '编程', 'count_num': 1}, ]
    # <QuerySet [('编程', 1), ('计算机语言', 1), ('linux', 1)]>
    # print(tag_list)
    # 日期分类
    date_list = models.Article.objects.filter(blog=blog).annotate(month=TruncMonth('create_time')).values(
        'month').annotate(count_num=Count('pk')).values_list('month', 'count_num')
    # values  [{'month': datetime.date(2022, 10, 1)},]
    # values_list <QuerySet [(datetime.date(2022, 10, 1), 3)]>
    # print(date_list)
    return locals()
