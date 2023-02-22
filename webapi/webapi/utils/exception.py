#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: xyz34
# Filer: exception.py
# Time: 2023年1月18日

from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.views import Response
from rest_framework import status
from utils.logging import logger
import logging

logging.getLogger('django')

def exception_handler(exc, context):
    response = drf_exception_handler(exc, context)
    if response is None:
        # 记录服务器异常
        logger.critical(f'{exc}')
        response = Response({
            'detail': '服务器异常,请重试...',
        },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        return response
