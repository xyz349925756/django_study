import requests
from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def index(request):
    """
    :param request:  请求相关的所有数据对象，比env更完善
    :return:
    """
    # return HttpResponse('hello,world!')
    # return render(request,'test.html')
    return redirect('https://cloudb.pub')

def ab_render(request):
    # views函数必须要接受一个形参request
    user_dict = {'username':'tom','password':'123'}
    # return render(request,'login.html',locals())
    # 传入参数特别多的时候locals会将所在的名称空间中所有的名字全部传递给html
    return render(request,'login.html',{'data':user_dict,'data':123})
     # 这种方式精确，节省资源

def static(request):
    return HttpResponse('static')
    return render(request,'test.html')


def login(request):
    """
    get与post 请求应该有不同的处理机制
    :param request: 请求相关的数据对象里面有很多简易方法
    :return:
    """
    # print('返回请求方式：',request.method,'类型：',type(request.method)) # 返回请求方式： POST 类型： <class 'str'>
    # if request.method == 'GET':
    #     print('come on')
    #     return render(request,'login.html')
    # elif request.method == 'POST':
    #     print('已收到！')
    if request.method == 'POST':
        # print('获取用户提交的post信息',request.POST)
        # # 获取用户提交的post信息 <QueryDict: {'username': ['xyz'], 'password': ['123']}>
        # username = request.POST.get('username')
        # print(username,type(username))
        # # 获取用户提交的post信息 < QueryDict: {'username': ['xzasd'], 'password': ['21321']} >
        # # xzasd <class 'str'>
        # password = request.POST.get('password')
        # print(password,type(password))
        # #获取用户提交的post信息 < QueryDict: {'username': ['sad'], 'password': ['13213']} >
        # #sad <class 'str'>
        # #13213 <class 'str'>
        # hobby = request.POST.get('hobby')
        # print(hobby,type(hobby))  # 333 <class 'str'> 只获取到最后一个value
        # username = request.POST.getlist('username')
        # password = request.POST.getlist('password')
        # hobby = request.POST.getlist('hobby')
        # print(username,type(username))
        # print(password,type(password))
        # print(hobby,type(hobby))
        """
        ['test'] <class 'list'>
        ['123'] <class 'list'>
        ['111', '222'] <class 'list'>
        """
        # 获取用户名密码利用orm操作数据，校验数据是否正确。
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 查询mysql中的数据
        from app01 import models  # 导入模板
        user_obj = models.User.objects.filter(username=username).first()
        #等价于mysql select * from user where username='xxx';
        # print(user_obj)
        # <QuerySet [<User: User object (1)>, <User: User object (79)>, <User: User object (727)>]>
        # print(user_obj.username)  # Fan Zitao
        # print(user_obj.password)  # qG5I2qn5SY
        if user_obj:
            if password == user_obj.password:
                return HttpResponse('登录成功')
            else:
                return HttpResponse('密码错误')
        else:
            return HttpResponse('用户不存在')

        print(requests.GET)

    return render(request,'login.html')


def reg(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        from app01 import models
        # 第一种
        # res = models.User.objects.create(username=username,password=password)
        # print(res,res.username,res.password)
        # 第二种
        user_obj = models.User(username=username,password=password)
        user_obj.save() # save data
    return render(request,'reg.html')

from app01 import models
def userlist(request):
    # data = models.User.objects.filter()
    # print(data)
    # return HttpResponse("userlist")
    user_queryset = models.User.objects.all()
    # return render(request, 'userlist.html', {'user_queryset':user_queryset})
    return render(request,'userlist.html',locals())

def edit_user(request):
    # 获取url问号后面的参数
    edit_id = request.GET.get('user_id')
    edit_obj = models.User.objects.filter(id=edit_id).first()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # models.User.objects.filter(id=edit_id).update(username=username,password=password)
        # 第二种修改数据的方法
        edit_obj.username = username
        edit_obj.password = password
        edit_obj.save()
        return redirect('/userlist/') # 数据修改完成直接返回userlist
    return render(request,'edit_user.html',locals()) # 将数据展示到页面

def delete_user(request):
    # 获取用户想要删除的数据ID
    delete_id = request.GET.get('user_id')
    # 直接到mysql删除数据即可
    models.User.objects.filter(id=delete_id).delete()
    return redirect('/userlist/') # 删除完成即可返回userlist