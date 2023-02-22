#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: xyz34
# Filer: jwt_auth.py
# Time: 2022年12月30日


from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

from app01 import jwt_auth


class JwtQueryParamAuthentication(BaseAuthentication):
    """
    用户需要在url中通过参数传递token
    """

    def authenticate(self, request):
        token = request.query_params.get('token')
        # print('token', token)

        payload = jwt_auth.parse_payload(token)
        # print('payload:', payload)  # payload: {'code': False, 'data': None, 'error': 'Token 已经过期'}
        # print(payload.get('status'))  # None
        if payload.get('status') is None:
            raise exceptions.AuthenticationFailed(payload)
        return payload, token


class JwtAuthorization(BaseAuthentication):
    """
    用户需要通过请求头的方式来进行传输token
    """

    def authenticate(self, request):
        """
        非登录页面需要校验token
        :param request:
        :return:
        """
        authorization = request.META.get('HTTP_AUTHORIZATION', '')
        # authorization = request.META.get('QUERY_STRING', '')
        # print(request.META)
        print(authorization)
        """
        {'ALLUSERSPROFILE': 'C:\\ProgramData', 
        'APPDATA': 'C:\\Users\\xyz34\\AppData\\Roaming',
         'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 
         'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 
         'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 
         'COMPUTERNAME': 'G', 
         'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 
         'DJANGO_SETTINGS_MODULE': 'day86.settings', 
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
           'PATH': 'C:\\Program Files\\VanDyke Software\\Clients\\;
                   C:\\Program Files (x86)\\VMware\\VMware Workstation\\bin\\;
                   C:\\Windows\\system32;
                   C:\\Windows;
                   C:\\Windows\\System32\\Wbem;
                   C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;
                   C:\\Windows\\System32\\OpenSSH\\;
                   C:\\Program Files\\dotnet\\;
                   D:\\iperf3;
                   F:\\apps\\ja-netfilter-all;
                   F:\\apps\\ja-netfilter-all\\plugins-jetbrains;
                   F:\\apps\\ja-netfilter-all\\vmoptions;
                   F:\\apps\\ja-netfilter-all\\config-jetbrains;
                   F:\\apps\\nginx;
                   D:\\mysql\\bin;C:\\Program Files\\PuTTY\\;
                   E:\\book;
                   C:\\Program Files\\Pandoc\\;
                   D:\\adb;
                   D:\\Python3;
                   C:\\Program Files (x86)\\NetSarang\\Xmanager 7\\;
                   C:\\Program Files (x86)\\NetSarang\\Xshell 7\\;
                   C:\\Program Files (x86)\\NetSarang\\Xftp 7\\;
                   C:\\Program Files (x86)\\NetSarang\\Xlpd 7\\;
                   C:\\Program Files\\nodejs\\;
                   C:\\Program Files\\Git\\cmd;
                   D:\\Python3\\Scripts\\;
                   D:\\Python3\\;
                   C:\\Users\\xyz34\\AppData\\Local\\Microsoft\\WindowsApps;;
                   C:\\Program Files\\JetBrains\\PyCharm 2022.2.3\\bin;;
                   C:\\Program Files\\Microsoft VS Code\\bin;
                   C:\\Users\\xyz34\\AppData\\Roaming\\npm', 
                   'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 
                   'PROCESSOR_ARCHITECTURE': 'AMD64', 
                   'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 61 Stepping 4, GenuineIntel',
                    'PROCESSOR_LEVEL': '6',
                     'PROCESSOR_REVISION': '3d04', 
                     'PROGRAMDATA': 'C:\\ProgramData', 
                     'PROGRAMFILES': 'C:\\Program Files', 
                     'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 
                     'PROGRAMW6432': 'C:\\Program Files', 
                     'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;
                                    C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules', 
                    'PUBLIC': 'C:\\Users\\Public', 
                    'PYCHARM': 'C:\\Program Files\\JetBrains\\PyCharm 2022.2.3\\bin;', 
                    'PYCHARM_DISPLAY_PORT': '63342', 
                    'PYCHARM_HOSTED': '1', 
                    'PYTHONIOENCODING': 'GBK', 
                    'PYTHONPATH': 'F:\\Django_Project_Dir\\day86;
                                  C:/Program Files/JetBrains/PyCharm 2022.2.3/plugins/python/helpers/pycharm_matplotlib_backend;
                                  C:/Program Files/JetBrains/PyCharm 2022.2.3/plugins/python/helpers/pycharm_display', 
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
                    'CONTENT_LENGTH': '297', 
                    'SCRIPT_NAME': '', 
                    'SERVER_PROTOCOL': 'HTTP/1.1', 
                    'SERVER_SOFTWARE': 'WSGIServer/0.2', 
                    'REQUEST_METHOD': 'GET',
                     'PATH_INFO': '/api/or/', 
                     'QUERY_STRING': 'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MiwiZXhwIjoxNjczMjQ5NDY4LCJ1c2VybmFtZSI6InRvbSJ9.oSOVFdv9FEODyF8TxJOk0b3qq_DVKbo9pXQRR7wR4O4', 
                     'REMOTE_ADDR': '127.0.0.1', 
                     'CONTENT_TYPE': 'multipart/form-data; 
                     boundary=--------------------------245627330301314230160042', 
                     'HTTP_USER_AGENT': 'PostmanRuntime/7.30.0', 
                     'HTTP_ACCEPT': '*/*', 
                     'HTTP_POSTMAN_TOKEN': 'cb144b07-37db-44f5-8f34-827aa3ae826c', 
                     'HTTP_HOST': '127.0.0.1:8000', 
                     'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 
                     'HTTP_CONNECTION': 'keep-alive', 
                     'wsgi.input': <django.core.handlers.wsgi.LimitedStream object at 0x0000012E1C06B610>, 
                     'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='gbk'>, 
                     'wsgi.version': (1, 0), 
                     'wsgi.run_once': False, 
                     'wsgi.url_scheme': 'http', 
                     'wsgi.multithread': True, 
                     'wsgi.multiprocess': False, 
                     'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>}

        """
        auth = authorization.split()
        print(auth)
        if not auth:
            raise exceptions.AuthenticationFailed({'error': '未获取到authorization请求头', 'status': False})
        if auth[0].lower() != 'jwt':
            raise exceptions.AuthenticationFailed({'error': 'Authorization 请求头中认证方式错误', 'statu': False})
        if len(auth) == 1:
            raise exceptions.AuthenticationFailed({'error': '非法请求头', 'status': False})
        elif len(auth) > 2:
            raise exceptions.AuthenticationFailed({'error': '非法Authoriztion 请求头', 'status': False})

        token = auth[1]
        result = jwt_auth.parse_payload(token)

        if result.get('status') is None:
            # if not result['status']:
            raise exceptions.AuthenticationFailed(result)
        return result, token
