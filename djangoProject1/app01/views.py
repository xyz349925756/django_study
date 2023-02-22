from django.shortcuts import render,HttpResponse,redirect,reverse

# Create your views here.

def test(request,xxx):
    print(xxx)
    return HttpResponse('test')


def testadd(request,year):
    print(year)
    return HttpResponse('testadd')

def index(request):
    print(reverse('ooo'))
    return render(request,'test.html')

def errors(request):
    return HttpResponse('404')

def func(request):
    # return reverse('ooo')
    return HttpResponse('func')
#
# def static(request):
#     return HttpResponse('static')

from app01 import models
def userlist(request):
    user_queryset = models.App01User.objects.all()
    return render(request,'userinfo.html',locals())



def edit_user(request,xxx):
    # print(xxx)  # id
    reverse('aaa', args=(xxx,))
    # print(request.GET)  # 空字典
    # edit_id = request.GET.get('/edit_user/xxx')
    # print(edit_id)
    edit_obj = models.App01User.objects.filter(id=xxx).first()
    # print(edit_obj.username,edit_obj.password)
    # print(request) #<WSGIRequest: GET '/edit/5/'>
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # username = edit_obj.username
        # password = edit_obj.password
        edit_obj.username = username
        edit_obj.password = password
        edit_obj.save()
        return redirect('/userlist/')
    # return render(request,'edit_mysql.html',locals())
    return render(request,'edit_mysql.html',locals())

def delete_user(request,deletes_user):
    models.App01User.objects.filter(id=deletes_user).delete()
    return redirect('/userlist/')
