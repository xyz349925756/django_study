from django.shortcuts import render, HttpResponse, reverse, redirect


# Create your views here.

def index(request):
    return HttpResponse('index')


from django.views import View


class MyLogin(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        return HttpResponse('post 请求')


def index(request):
    n = 123
    f = 1.3495726
    s = 'hello,你们好'
    b = True
    l = ['jack', 'Tom', '张三', '李四']
    t = (1, 2, 3, 4, 5, 6, 7)
    d = {'username': 'jack', 'password': '123456', 'age': 18, 'hobby': ['boy', 'girl', 'other', {'info': '哈哈哈'}]}
    se = {'1', '3', '4', '神探'}
    lll = []

    def func():
        print('执行了func')
        return 'func 函数'

    class MyClass(object):
        def get_self(self):
            return 'self'

        @staticmethod
        def get_func(self):
            return 'func_obj'

        @classmethod
        def get_class(cls):
            return 'cls_obj'

        def __str__(self):
            return 'class str'

    obj = MyClass()

    file_size = 123456789

    import datetime
    current_time = datetime.datetime.now()

    info = '社会从不缺少一个迟早要被淘汰的工程师，但缺少与时俱进的解决方案架构师！ 一个IT方案没有优秀的架构设计，那么只会增加运维成本和风险。架构师不是纸上谈兵， 每一个方案会导致什么结果都已经在架构师胸中，当然所涉及到的知识可不是点到点，线到线的，而是面到空间！'

    egl = 'my name is jack , age 49 ,from chinese.'

    msg = 'This is my python study'
    hh = '<h1> Title 标题 </h1>'
    ss = '<script>alert("警告")</script>'

    from django.utils.safestring import mark_safe
    res = mark_safe('<h2>h2标题</h2>')

    return render(request, 'index.html', locals())


def g(request):
    return render(request,'g.html')

def login(request):
    return render(request,'login.html')

def reg(request):
    return render(request,'reg.html')