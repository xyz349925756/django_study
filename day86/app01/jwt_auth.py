#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: xyz34
# Filer: jwt_auth.py
# Time: 2022年12月30日

import jwt
import datetime

from django.conf import settings
from django.contrib.auth import authenticate
from jwt import exceptions

from app01 import models

JWT_SALT = settings.SECRET_KEY


# def create_token(request, timeout=1):
def create_token(payload, timeout=2):
    """
    create token
    :param payload: 有效载体
    :param request:
    :param timeout:  超时时间
    :return:
    """

    # username = request.data.get('username')
    # password = request.data.get('password')

    # if authenticate(username=username, password=password):
    #     user_obj = models.UserInfo.objects.filter(username=username).first()

    headers = {
        'typ': 'JWT',
        'alg': 'HS256'
    }

    # payloads = {
    #     'id': user_obj.pk,
    #     'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=timeout),
    #     'username': user_obj.username
    # }

    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=timeout)

    # result = jwt.encode(payload=payloads, key=JWT_SALT, algorithm="HS256", headers=headers)
    result = jwt.encode(payload=payload, key=JWT_SALT, algorithm="HS256", headers=headers)

    return result


def parse_payload(token):
    """
    对token进行校验和发行校验并获取payload
    :param token:
    :return:
    """
    result = {'code': False, 'data': None, 'error': None}

    try:
        verified_payload = jwt.decode(token, JWT_SALT, algorithms="HS256")
        result['status'] = True
        result['data'] = verified_payload
    except exceptions.ExpiredSignatureError:
        result['error'] = 'Token 已经过期'
    except jwt.DecodeError:
        result['error'] = 'Token 认证失败'
    except jwt.InvalidTokenError:
        result['error'] = '非法的Token'
    return result
