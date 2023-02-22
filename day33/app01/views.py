from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def index(request):
    back_dic = {'username': '', 'password': ''}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if '123' in username:
            back_dic['username'] = '不能输入连续数字'
        if len(password) < 8:
            back_dic['password'] = '密码太短，不符合要求！'
    return render(request, 'index.html', locals())


from django import forms
from django.core.validators import RegexValidator


class MyForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=16, label='用户名',
                               error_messages={
                                   'min_length': '用户名不能小于3位',
                                   'max_length': '用户名最多16位',
                                   'required': '用户名不能为空!'
                               }, initial='Tom', widget=forms.TextInput(attrs={'class': 'form-control'})
                               )
    password = forms.CharField(min_length=3, max_length=8, label='密  码',
                               error_messages={
                                   'min_length': '密码不能小于3位',
                                   'max_length': '密码不能超过8位',
                                   'required': '密码不能为空!'
                               }, widget=forms.PasswordInput(attrs={'class': 'form-control'})
                               )

    confirm_password = forms.CharField(min_length=3, max_length=8, label='确认密码',
                                       error_messages={
                                           'min_length': '确认密码不能小于3位',
                                           'max_length': '确认密码不能超过8位',
                                           'required': '确认密码不能为空!'
                                       }, widget=forms.PasswordInput(attrs={'class': 'form-control'})
                                       )

    email = forms.EmailField(label='E-mail',
                             error_messages={
                                 # 'invalid':'Email 格式不正确',
                                 'invalid': 'Email 格式不正确',
                                 'required': 'Email 不能为空!'
                             }, widget=forms.EmailInput(attrs={'class': 'form-control'})
                             )
    phone = forms.CharField(label='电话号码', min_length=11, max_length=11,
                            validators=[
                                RegexValidator(r'^[0-9]+$', '请输入数字'),
                                RegexValidator(r'^1[3,4,5,8,9][0-9]+$', '请输入大陆手机号码段13，14，15，18，19')
                            ], widget=forms.TextInput(attrs={'class': 'form-control'}),
                            error_messages={
                                'min_length': '最少11位',
                                'max_length': '您个傻吊，修改源码突破11？警告：最多11位',
                                'required': '号码不能为空'
                            }
                            )

    gender = forms.ChoiceField(
        choices=((1, '男'), (2, '女'), (3, '保密')),
        label='性别',
        initial=3,
        widget=forms.RadioSelect()
    )

    hobby = forms.ChoiceField(
        choices=((1, '篮球'), (2, '足球'), (3, '羽毛球')),
        label='兴趣',
        initial=2,
        widget=forms.Select()
    )

    hobby1 = forms.MultipleChoiceField(
        choices=((1, '篮球'), (2, '足球'), (3, '羽毛球')),
        label='爱好',
        initial=2,
        widget=forms.SelectMultiple()
    )

    keep = forms.ChoiceField(
        label='记住密码',
        initial='checked',
        widget=forms.CheckboxInput()
    )

    hobby2 = forms.MultipleChoiceField(
        choices=((1, '篮球'), (2, '足球'), (3, '羽毛球')),
        label='Love',
        initial=[2, 3],
        widget=forms.CheckboxSelectMultiple()
    )

    # 局部钩子hook 在类里面写
    def clean_username(self):
        # 获取用户名
        username = self.cleaned_data.get('username')
        if 'abc' in username:
            self.add_error('username', '不能使用abc作为用户名')
        # 将钩子函数钩取出来，数据再放回去
        return username

    # 全局钩子
    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if not confirm_password == password:
            self.add_error('confirm_password', '两次密码不一致')
        return self.cleaned_data


def test(request):
    # 产生一个空对象
    form_obj = MyForm()
    if request.method == 'POST':
        '''
        获取用户数据并且校验。解决数据获取繁琐，校验数据需要构造字典才能传入，request.POST 本身就是一个queryset object 字典对象
        '''
        form_obj = MyForm(request.POST)
        if form_obj.is_valid():  # 校验数据
            return HttpResponse('OK')  # 如果合法 操作数据库数据
        # 如果不是结果直接传递给html
    return render(request, 'test.html', locals())


def login_auth(func):
    def inner(request,*args,**kwargs):
        # print(request.path_info)
        # print(request.get_full_path())  # 可以获取输入的用户名和密码
        target_url = request.get_full_path()
        if request.COOKIES.get('username'):
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
            if target_url:
                obj = redirect(target_url)
            else:
                obj = redirect('/home/')
            obj.set_cookie('username','cookie_name',max_age=3)
            return obj
    return render(request,'login.html')

@login_auth
def home(request):
    # 判断cookie是否存在
    # if request.COOKIES.get('username') == 'cookie_name':
    #     return HttpResponse('只有登录的用户才可以看到这个页面')
    return HttpResponse('只有登录的用户才可以看到home页面')

@login_auth
def clinet(request):
    return HttpResponse('当前页 client')

@login_auth
def login_out(request):
    obj = redirect('/login/')
    obj.delete_cookie('username')
    return obj


