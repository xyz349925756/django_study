from django.shortcuts import render, HttpResponse, redirect, reverse


# Create your views here.

def test(request):
    reverse('app01:xxx')
    return render(request, 'index.html')


import json
from django.http import JsonResponse, HttpResponseRedirect


def ab_json(request):
    u_list = {
        'username': '中文字符出现乱码',
        'password': '123456',
        'hobby': 'boy',
    }

    l = [1, 2, 3, 4, 5, 6, 8]

    # 方法一
    # json_str = json.dumps(u_list,ensure_ascii=False) # 不加中文字符变二进制
    # return HttpResponse(json_str)

    # 方法二
    # return  JsonResponse(u_list,json_dumps_params={'ensure_ascii':False})

    return JsonResponse(l, safe=False)  # 默认只能序列化字典，其他需要设置safe参数


def upload_success(request):
    return HttpResponse('upload file success!')


from .forms_file import Upload_File_Form


# from somewhere import handle_uploaded_file

def handle_uploaded_file(f_name):
    with open(f_name, 'wb+') as f:
        for chunk in f_name.chunks():
            f.write(chunk)

def upload_success(request):
    return HttpResponse('success!')

def upload_file(request):
    if request.method == 'POST':
        print('files:',request.FILES)
        print('post:',request.POST)
        file_obj = request.FILES.get('file')
        # print(request.path)
        # print(file_obj)
        # with open(file_obj,'wb+') as f:
        #     for l in file_obj.chunks():
        #         f.writelines(l)


        return HttpResponseRedirect('/app01/upload_success/')

    return render(request, 'index.html')
