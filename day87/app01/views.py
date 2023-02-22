from django.shortcuts import render, HttpResponse

# Create your views here.
from django.views.decorators.cache import cache_page
import datetime,time
from app01 import models


# view缓存
# @cache_page(60 * 3)
# def index(request):
#     t = datetime.datetime.now()  # 获取当前时间
#     bookList = models.Book.objects.all()
#     return render(request,'index.html',locals())

# 全站缓存
# def index(request):
#     t = datetime.datetime.now()
#     bookList = models.Book.objects.all()
#     return render(request, 'index.html', locals())
#
#
# def foo(request):
#     t = datetime.datetime.now()
#     return HttpResponse('hello' + str(t))

# 局部缓存

def index(request):
    t = datetime.datetime.now()
    bookList = models.Book.objects.all()
    return render(request, 'index.html', locals())
