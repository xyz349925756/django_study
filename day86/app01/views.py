from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from app01 import models, serializers


class UserInfos(APIView):

    def get(self, request, *args, **kwargs):

        if kwargs:
            user_obj = models.UserInfo.objects.filter(pk=kwargs.get('pk')).first()
            user_ser = serializers.UserModelSerializers(user_obj)
            return Response({'code': 100, 'msg': '单项', 'data': user_ser.data})
        else:
            user_list = models.UserInfo.objects.all()
            user_ser = serializers.UserModelSerializers(user_list, many=True)
            return Response({'code': 101, 'msg': '多项', 'data': user_ser.data})


from django.contrib.auth import authenticate


class Login(APIView):
    """
    用户登录
    """

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if authenticate(username=username, password=password):
            # 因为这里的用户他们的密码被加密了,只能使用这种方法验证
            # print(username)
            # 如果你的密码是明文的使用下面这个验证既可
            # user_obj = models.UserInfo.objects.filter(username=username,password).first()
            user_obj = models.UserInfo.objects.filter(username=username).first()
            print(user_obj.pk, username, password)
        else:
            return Response({'code': 400, 'msg': '用户名或密码错误!'})

        import jwt
        import datetime
        salt = 'xxxxxxsdadsadsadsqewqewgftyjyjyt'

        # build header
        headers = {
            "alg": "HS256",
            "typ": "JWT"
        }

        # build payload
        payloads = {
            "id": user_obj.pk,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=1),  # 超时时间
            "username": user_obj.username
        }

        result = jwt.encode(payload=payloads, key=salt, algorithm="HS256", headers=headers)

        return Response({'code': 88, 'Token': result})


class Order(APIView):

    def get(self, request, *args, **kwargs):

        token = request.query_params.get('token')
        # print(type(token))
        # 判断token是否合法  (切割,判断是否过期,是否合法)
        import jwt
        from jwt import exceptions
        import datetime
        salt = 'xxxxxxsdadsadsadsqewqewgftyjyjyt'
        verified_payload = None
        msg = None
        try:
            verified_payload = jwt.decode(token, salt, algorithms=["HS256"])
        except exceptions.ExpiredSignatureError:
            msg = 'token 已经失效'
        except jwt.DecodeError:
            msg = 'Token 认证失败'
        except jwt.InvalidTokenError:
            msg = '非法的token'

        if not verified_payload:
            return Response({'code': 888, 'error': msg})

        print(verified_payload['id'], verified_payload['username'])
        return Response('列表')


from app01 import jwt_auth
from app01 import auth


class LoginView(APIView):
    authentication_classes = []  # 使用全局验证之后对于登录界面不需要验证是否登录，都是没有登录的才需要登录操作

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        # print(request.data)
        print(username, password)
        if authenticate(username=username, password=password):
            user_obj = models.UserInfo.objects.filter(username=username).first()
            payload = {
                'id': user_obj.pk,
                'username': user_obj.username
            }
            token = jwt_auth.create_token(payload)
            return Response({'status': True, 'token': token})
        return Response({'status': False, 'error': '用户名或密码错误'})


class OrderView(APIView):
    # authentication_classes = [auth.JwtQueryParamAuthentication, ]
    authentication_classes = [auth.JwtAuthorization,]

    def get(self, request, *args, **kwargs):
        print(request.user, request.auth)
        return Response({'data': '订单列表'})

    def post(self, request, *args, **kwargs):
        print(request.user, request.auth)
        return Response({'data': '添加订单'})

    def put(self, request, *args, **kwargs):
        print(request.user, request.auth)
        return Response({'data': '修改订单'})

    def delete(self, request, *args, **kwargs):
        print(request.user, request.auth)
        return Response({'data': '删除订单'})
