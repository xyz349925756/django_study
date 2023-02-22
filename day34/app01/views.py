from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

def index(request):
    return render(request, 'index.html', locals())


def login_auth(func):
    def inner(request,*args, **kwargs):
        # print(request.get_full_path())
        target_url = request.get_full_path()
        if request.session.get('username'):
            return func(request,*args,**kwargs)
        else:
            return redirect(f'/login/?next={target_url}')
    return inner


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'tom' and password == '123456':
            target_url = request.GET.get('next')
            # print(target_url)
            # request.session['username'] = 'session'
            if target_url:
                obj = redirect(target_url)
            else:
                obj = redirect('/index/')
            request.session['username'] = 'session'
            request.session.set_expiry(60)
            return obj
    return render(request, 'login.html')

@login_auth
def home(request):
    # if request.session.get('username') == 'session':
    #     return HttpResponse('home')
    return HttpResponse('home page')

@login_auth
def client(request):
    return HttpResponse('client')

@login_auth
def db(request):
    return HttpResponse('db')

@login_auth
def test(request):
    return HttpResponse('test')

@login_auth
def loginout(request):
    request.session.flush()
    return redirect('/login/')

import datetime

def cur_time(request):
    now = datetime.datetime.now()
    t = now.strftime("%Y-%m-%d %H:%M:%S")
    print(t)
    return HttpResponse(t)

from django.views.decorators.csrf import csrf_protect,csrf_exempt
# @csrf_exempt
# @csrf_protect
def transfer(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        target_user = request.POST.get('target_user')
        money = request.POST.get('money')
        print(f'{username}给{target_user}转了{money}元！')
    return render(request,'transfer.html')

from django.views import View
from django.utils.decorators import method_decorator

# @method_decorator(csrf_exempt,name='post')
# @method_decorator(csrf_protect,name='post')
class MyCsrfToken(View):

    # @method_decorator(csrf_exempt)
    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        return super(MyCsrfToken,self).dispatch(request,*args,**kwargs)

    def get(self,request):
        return HttpResponse('get')

    # @method_decorator(csrf_exempt)
    # @method_decorator(csrf_protect)
    def post(self,request):
        return HttpResponse('post')

