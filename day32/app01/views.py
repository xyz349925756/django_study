import json

from django.shortcuts import render, HttpResponse, redirect, reverse

from django.http import JsonResponse


# Create your views here.

# def index(request):
#     if request.method == 'POST':
#         # print(request.POST)
#         i1 = request.POST.get('i1')
#         i2 = request.POST.get('i2')
#         i3 = int(i1) + int(i2)
#         # d = {'code':100,'msg':i3}
#         # d = {'code':100,'msg':666}
#         return HttpResponse(i3)
#         # return HttpResponse(d)
#         # return HttpResponse(json.dumps(d)) #{"code": 100, "msg": 666}
#         # return JsonResponse(d)  #[object Object]
#     return render(request, 'index.html')

# def is_ajax(request):
#     return request.headers.get('x-requested-with') == 'XMLHttpRequest'


def index(request):
    if request.method == 'POST':
        print("request.post", request.POST)
        print("request.files", request.FILES)
    return render(request, 'index.html')


import json


def ab_json(request):
    # print(request.POST)
    # print(request.FILES)
    # print(request.body)  #b '{"username":"json","age":55}'
    # 针对json格式数据需要自己手动处理,原理如下:
    # json_bytes = request.body
    # print(json_bytes,type(json_bytes))
    # json_str = json_bytes.decode('utf-8')
    # print(json_str,type(json_str))
    # json_dict = json.loads(json_str)
    # print(json_dict,type(json_dict))

    # json_dict = json.loads(json_bytes)
    # print(json_dict,type(json_bytes))
    # print(request.headers)
    # print('111',request.headers.get('x-requested-with') == 'XMLHttpRequest')
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # json_bytes = request.body
        # json_str = json_bytes.decode('utf-8')
        # json_dict = json.loads(json_str)
        json_dict = json.loads(request.body)
        print(json_dict, type(json_dict))
    return render(request, 'ab_json.html')


def ab_file(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.method == 'POST':
            print(request.POST)
            print(request.FILES)
    return render(request, 'ab_file.html')


from app01 import models
import json
from django.http import JsonResponse
from django.core import serializers


def ab_ser(request):
    user_queryset = models.User.objects.all()
    # user_list = []
    # for user_obj in user_queryset:
    #     tmp = {
    #         'pk':user_obj.pk,
    #         'username':user_obj.username,
    #         'age':user_obj.age,
    #         'gender':user_obj.get_gender_display(),
    #         'score':user_obj.score,
    #     }
    #     user_list.append(tmp)
    # # return render(request,'ab_ser.html',locals())
    # return JsonResponse(user_list,safe=False)
    res = serializers.serialize('json', user_queryset)
    return HttpResponse(res)


from app01.utils.page import Pagination


def user_list(request):
    user_queryset = models.User.objects.all()

    current_page = request.GET.get('page', 1)  # 如果获取不到当前页码就返回第一页
    # try:
    #     current_page = int(current_page)
    # except Exception:
    #     current_page = 1
    #
    # # 每页展示数据条数
    # per_page_num = 15
    #
    # # 起始位置
    # start_page = (current_page - 1) * per_page_num
    #
    # end_page = current_page * per_page_num
    # print(f'起始页{start_page},最后一页{end_page},当前页{current_page}')

    all_count = user_queryset.count()

    # page_count, more = divmod(all_count, per_page_num)
    #
    #
    # print(f'总数:{all_count},满:{page_count}页,剩余:{more}')
    #
    # if more:
    #     page_count += 1
    #
    # page_html = ''
    # error_html = ''
    #
    # xxx = current_page
    #
    #
    # if current_page < 6:
    #     current_page = 6
    # elif current_page > (page_count - 6):
    #     current_page = (page_count-5)
    #
    #
    # for i in range(current_page - 5, current_page+6):
    #     if xxx == 1:
    #         Previous = f'<li class="page-item disabled"><a aria-label="Previous" class="page-link" href="?page=1"><span aria-hidden="true">Previous</span></a></li>'
    #         if xxx == i:
    #             page_html += f'<li class="page-item active" aria-current="page"><a class="page-link" href="?page={i}">{i}</a></li>'
    #         else:
    #             page_html += f'<li class="page-item" aria-current="page"><a class="page-link" href="?page={i}">{i}</a></li>'
    #
    #         Next = f'<li class="page-item"><a aria-label="Next" class="page-link" href="?page={xxx+1}"><span aria-hidden="true">Next</span></a></li>'
    #     elif xxx > (page_count + 1):
    #         error_html = f'<div class="bd-example" style="margin-left: 40%; margin-top: 10%;">\
    #             <p class="h1">这是一个虚空 <span class="badge bg-primary">这</span></p>\
    #             <p class="h2">这是一个虚空 <span class="badge bg-secondary">是</span></p>\
    #             <p class="h3">这是一个虚空 <span class="badge bg-success">一</span></p>\
    #             <p class="h4">这是一个虚空 <span class="badge bg-danger">个</span></p>\
    #             <p class="h5">这是一个虚空 <span class="badge bg-warning text-dark">虚</span></p>\
    #             <p class="h6">这是一个虚空 <span class="badge bg-info text-dark">空</span></p>\
    #             <p class="h6">这是一个虚空 <span class="badge bg-dark">!</span></p>\
    #             <hr><p class="h6">您以为你发现了bug,其实这是隐藏功能!</p>\
    #         </div>'
    #     elif xxx >= (page_count-5):
    #         Previous = f'<li class="page-item"><a aria-label="Previous" class="page-link" href="?page={xxx-1}"><span aria-hidden="true">Previous</span></a></li>'
    #         if xxx == i:
    #             page_html += f'<li class="page-item active" aria-current="page"><a class="page-link" href="?page={i}">{i}</a></li>'
    #         else:
    #             page_html += f'<li class="page-item" aria-current="page"><a class="page-link" href="?page={i}">{i}</a></li>'
    #         Next = f'<li class="page-item disabled"><a aria-label="Next" class="page-link" href="?page={xxx+1}"><span aria-hidden="true">Next</span></a></li>'
    #
    #     else:
    #         Previous = f'<li class="page-item"><a aria-label="Previous" class="page-link" href="?page={xxx-1}"><span aria-hidden="true">Previous</span></a></li>'
    #         if xxx == i:
    #             page_html += f'<li class="page-item active" aria-current="page"><a class="page-link" href="?page={i}">{i}</a></li>'
    #         else:
    #             page_html += f'<li class="page-item" aria-current="page"><a class="page-link" href="?page={i}">{i}</a></li>'
    #
    #         Next = f'<li class="page-item"><a aria-label="Next" class="page-link" href="?page={xxx+1}"><span aria-hidden="true">Next</span></a></li>'
    #

    # user_queryset_list = user_queryset[start_page:end_page]
    # return render(request,'user_list.html',locals())
    page_obj = Pagination(current_page=current_page, all_count=all_count)
    page_queryset = user_queryset[page_obj.start:page_obj.end]

    return render(request, 'add_dates.html', locals())


import time


def delete_user(request):
    """
    前端使用ajax交互时候,后端通常会返回一个字典格式的数据
    @param request:
    @return:
    """
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.method == 'POST':
            back_dict = {'code': 10086, 'msg': ''}
            time.sleep(3)
            delete_id = request.POST.get('delete_id')
            data = models.User.objects.filter(pk=delete_id)
            # data1 = data.values('username').first()['username']
            data1 = data.first().username
            # print(data1)
            data.delete()
            back_dict['msg'] = f' {data1} 已经删除'
            return JsonResponse(back_dict)


def ab_adds(request):
    # for i in range(1000):
    #     models.Publish.objects.create(name=f'{ i } 出版社')
    publish_list = []
    for i in range(1000):
        pub_obj = models.Publish.objects.create(name=f'{i} 出版社')
        publish_list.append(pub_obj)
    models.Publish.objects.bulk_create(publish_list)

    publish_queryset = models.Publish.objects.all()


def reg(request):
    return render(request,'reg_user.html',locals())