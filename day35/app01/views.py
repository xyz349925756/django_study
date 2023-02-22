from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth

# Create your views here.
# 注册
from django.contrib.auth.models import User

def index(request):
    return render(request,'index.html')

def regedit(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 创建普通用户
        User.objects.create_user(username=username, password=password)

        # 创建超级用户
        # User.objects.create_superuser(username=username,email=123@qq.com,password=password)
    return render(request, 'register.html')

def regedit_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        # 操作auth_user表写入数据
        User.objects.create_superuser(username=username,email=email,password=password)
    return render(request,'register_admin.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 校验数据，获取表，密码比对，加密的sha256
        user_obj = auth.authenticate(request,username=username,password=password)
        # print(user_obj)  # 用户对象
        # print(user_obj.username)  # 用户名
        # print(user_obj.password)   # 加密的密钥密码

        if user_obj:   # 确定用户是否存在
            auth.login(request,user_obj)  # 保存用户状态， 类似request,session[key]=user_obj
            # 该方法是缓存了用户登录信息，在其他位置可以通过request.user获取当前登陆对象
            # path_url = request.get_full_path()
            # print(path_url)
            target_url = request.GET.get('next')
            if target_url:
                obj = redirect(target_url)
            else:
                obj = redirect('/')
            return obj
            # return redirect('/home/')
        """
        1、这里面的操作是查找auth_user标签
        2、自动给密码sha256加密再对比
        该方法括号内必须使用用户名，密码。
        """
    return render(request,'login.html')

from django.contrib.auth.decorators import login_required   # 导入用户验证装饰器

@login_required
def home(request):
    # print(request.user)  # 登录之后的用户才能看到home，用户对象
    # print(request.user.is_authenticated)  # 判断用户是否登录
    if request.user.is_authenticated:
        # print(request.get_full_path())
        # path_url = request.get_full_path()
        # return redirect(path_url)
        return HttpResponse('home')

    return redirect('/login/')
    # return render(request,'login.html')


@login_required
def edit_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if new_password == confirm_password:
            is_right = request.user.check_password(old_password)
            if is_right:
                request.user.set_password(new_password)
                request.user.save()
        return redirect('/login/')
    return render(request,'edit_password.html',locals())


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/login/')
