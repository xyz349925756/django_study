from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from app01.models import UserInfo
from app01.ser_api import UserinfoSerializer


class User1View(ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserinfoSerializer

    @action(methods=['get', 'post'], detail=False)
    def get_l(self, request, pk):
        print(pk)
        user_list = self.get_queryset()[:10]  # error 'Manager' object is not subscriptable queryset 后面需要加.all()
        ser = self.get_serializer(user_list, many=True)
        return Response(ser.data)


from rest_framework.views import APIView


class TestView(APIView):
    def get(self, request):
        print('hhhhhh')
        print(request.user)
        print(request.user.username)
        return Response({'msg': 'test'})


import uuid

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.authentication import BaseAuthentication

from app01.models import LoginUser, UserToken
from app01.utils.MyStatusCode import MyStatusCode
from app01.my_auth import MyTokenAuth


class LoginView(APIView):
    # authentication_classes = [MyTokenAuth]
    authentication_classes = []
    res_msg = MyStatusCode()

    # print(res_msg.get_dict)  # 启动就加载成功状态码

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = LoginUser.objects.filter(username=username, password=password).first()
        # print(user)  # LoginUser object (1)
        if user:
            token = uuid.uuid4()
            # UserToken.objects.create(token=token, user=user) #IntegrityError: UNIQUE constraint failed: app01_usertoken.user_id
            # 上面不能保存user_id 是因为有unique 唯一约束属性.避免登陆一次生成一个token.这种问题应该是不存在,因为models中一对一关系自带unique所以
            # 再次登录就出现异常只能使用下面的update_or_create方法
            UserToken.objects.update_or_create(defaults={'token': token}, user=user)
            self.res_msg.code = 21
            self.res_msg.msg = 'user and token verify success!'
            self.res_msg.token = token
            # print(self.res_msg.get_dict)
            return Response(self.res_msg.get_dict)
        else:
            self.res_msg.code = 41
            self.res_msg.msg = 'username or password is errors'
            # print(self.res_msg.get_dict)
            return Response(self.res_msg.get_dict)


from app01 import my_auth


class Test1View(APIView):
    # authentication_classes = [my_auth.MyTokenAuth]
    permission_classes = [my_auth.UserPermission]

    def get(self, request, *args, **kwargs):
        return Response('Test Data')


class Test2View(APIView):
    # authentication_classes = [my_auth.MyTokenAuth]
    permission_classes = [my_auth.User1Permission]

    def get(self, request, *args, **kwargs):
        return Response('普通用户数据')


from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class Test3View(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        return Response('is admin')


# from rest_framework.parsers import MultiPartParser


class Test4View(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        return Response('未登录用户')


from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class Test5View(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = [AnonRateThrottle]

    def get(self, request, *args, **kwargs):
        return Response('未登录用户,局部限制')


class Test6View(APIView):
    # permission_classes = [my_auth.User1Permission]
    authentication_classes = [SessionAuthentication]
    throttle_classes = [UserRateThrottle]

    def get(self, request, *args, **kwargs):
        user = request.user
        # print(request.META)
        """
        {
        'ALLUSERSPROFILE': 'C:\\ProgramData', 
        'APPDATA': 'C:\\Users\\xyz34\\AppData\\Roaming', 
        'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 
        'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 
        'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 
        'COMPUTERNAME': 'G',
        'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 
        'DJANGO_SETTINGS_MODULE': 'day82.settings',
         'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 
         'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 
         'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 
         'HOMEDRIVE': 'C:', 
         'HOMEPATH': '\\Users\\xyz34',
         'IDEA_INITIAL_DIRECTORY': 'C:\\Program Files\\JetBrains\\PyCharm 2022.2.3\\bin', 
         'LOCALAPPDATA': 'C:\\Users\\xyz34\\AppData\\Local', 
         'LOGONSERVER': '\\\\G', 
         'NUMBER_OF_PROCESSORS': '4', 
         'ONEDRIVE': 'D:\\OneDrive', 
         'ONEDRIVECONSUMER': 'D:\\OneDrive', 
         'OS': 'Windows_NT', 
         'PATH': '', 
         'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 
         'PROCESSOR_ARCHITECTURE': 'AMD64', 
         'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 61 Stepping 4, GenuineIntel', 
         'PROCESSOR_LEVEL': '6', 
         'PROCESSOR_REVISION': '3d04', 
         'PROGRAMDATA': 'C:\\ProgramData', 
         'PROGRAMFILES': 'C:\\Program Files', 
         'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 
         'PROGRAMW6432': 'C:\\Program Files', 
         'PSMODULEPATH': '', 
         'PUBLIC': 'C:\\Users\\Public', 
         'PYCHARM': 'C:\\Program Files\\JetBrains\\PyCharm 2022.2.3\\bin;', 
         'PYCHARM_DISPLAY_PORT': '63342',
         'PYCHARM_HOSTED': '1',
          'PYTHONIOENCODING': 'GBK', 
          'PYTHONPATH': '', 
          'PYTHONUNBUFFERED': '1', 
          'SESSIONNAME': 'Console', 
          'SYSTEMDRIVE': 'C:', 
          'SYSTEMROOT': 'C:\\Windows', 
          'TEMP': 'C:\\Users\\xyz34\\AppData\\Local\\Temp', 
          'TMP': 'C:\\Users\\xyz34\\AppData\\Local\\Temp', 
          'USERDOMAIN': 'G', 
          'USERDOMAIN_ROAMINGPROFILE': 'G', 
          'USERNAME': 'xyz34', 
          'USERPROFILE': 'C:\\Users\\xyz34', 
          'WINDIR': 'C:\\Windows', 
          'RUN_MAIN': 'true', 
          'SERVER_NAME': 'G', 
          'GATEWAY_INTERFACE': 'CGI/1.1', 
          'SERVER_PORT': '8000', 
          'REMOTE_HOST': '', 
          'CONTENT_LENGTH': '', 
          'SCRIPT_NAME': '', 
          'SERVER_PROTOCOL': 'HTTP/1.1', 
          'SERVER_SOFTWARE': 'WSGIServer/0.2', 
          'REQUEST_METHOD': 'GET', 
          'PATH_INFO': '/test6/', 
          'QUERY_STRING': '', 
          'REMOTE_ADDR': '127.0.0.1', 
          'CONTENT_TYPE': 'text/plain', 
          'HTTP_HOST': '127.0.0.1:8000', 
          'HTTP_CONNECTION': 'keep-alive', 
          'HTTP_PRAGMA': 'no-cache', 
          'HTTP_CACHE_CONTROL': 'no-cache',
          'HTTP_SEC_CH_UA': '"Microsoft Edge";v="107", 
          "Chromium";v="107", 
          "Not=A?Brand";v="24"', 
          'HTTP_SEC_CH_UA_MOBILE': '?0', 
          'HTTP_SEC_CH_UA_PLATFORM': '"Windows"', 
          'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 
          'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35', 
          'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
          'HTTP_SEC_FETCH_SITE': 'none', 
          'HTTP_SEC_FETCH_MODE': 'navigate', 
          'HTTP_SEC_FETCH_USER': '?1', 
          'HTTP_SEC_FETCH_DEST': 'document', 
          'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 
          'HTTP_ACCEPT_LANGUAGE': 'zh-CN,zh;q=0.9,en;q=0.8', 
          'HTTP_COOKIE': 'csrftoken=EysDMvPDfzqEJWkrr21N6aVySZjoVp2B;sessionid=h4f9ujavlejxucpnurapxfgt9wlt71dd', 
          'wsgi.input': <django.core.handlers.wsgi.LimitedStream object at 0x00000148E2C21BD0>, 
          'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='gbk'>, 
          'wsgi.version': (1, 0), 
          'wsgi.run_once': False, 
          'wsgi.url_scheme': 'http',
          'wsgi.multithread': True, 
          'wsgi.multiprocess': False, 
          'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>, 
          'CSRF_COOKIE': 'EysDMvPDfzqEJWkrr21N6aVySZjoVp2B'
          }
        """
        if user.is_authenticated:

            return Response('已登录,可以连续10次')
        else:
            return Response('未登录,5次')


from rest_framework.generics import ListAPIView, RetrieveAPIView


class UserList(ListAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserinfoSerializer
    filterset_fields = ('id', 'gender')


from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 10000


from rest_framework.views import exception_handler


class User1List(ListAPIView, RetrieveAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserinfoSerializer
    # pagination_class = LargeResultsSetPagination
    pagination_class = None
    filter_backends = [OrderingFilter]
    ordering_fields = ('id', 'gender')


from app01.utils.custom_response import CutomResponse


class TestView7(APIView):
    def get(self, request, *args, **kwargs):
        return CutomResponse(data={"name": 'jack'}, token='xxxxxxxxx', aa='ssssssssss')
