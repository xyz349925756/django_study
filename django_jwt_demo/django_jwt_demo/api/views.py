from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from utils.jwt_auth import create_token


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(self, request, *args, **kwargs):
        """ 用户登录 """
        user = request.POST.get('username')
        pwd = request.POST.get('password')

        # 检测用户和密码是否正确，此处可以在数据进行校验。
        if user == 'wupeiqi' and pwd == '123':
            # 用户名和密码正确，给用户生成token并返回
            token = create_token({'username': 'wupeiqi'})
            return JsonResponse({'status': True, 'token': token})
        return JsonResponse({'status': False, 'error': '用户名或密码错误'})


@method_decorator(csrf_exempt, name='dispatch')
class OrderView(View):

    def get(self, request, *args, **kwargs):
        print(request.user_info)
        return JsonResponse({'data': '订单列表'})

    def post(self, request, *args, **kwargs):
        print(request.user_info)
        return JsonResponse({'data': '添加订单'})

    def put(self, request, *args, **kwargs):
        print(request.user_info)
        return JsonResponse({'data': '修改订单'})

    def delete(self, request, *args, **kwargs):
        print(request.user_info)
        return JsonResponse({'data': '删除订单'})
