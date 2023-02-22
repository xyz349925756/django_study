#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: xyz34
# Filer: router.py
# Time: 2023年1月19日

from rest_framework.routers import Route, DynamicRoute, SimpleRouter as DRFSimpleRouter


# 重写simplerouter方法
class SimpleRouter(DRFSimpleRouter):
    routes = [
        # list route
        Route(
            url=r'^{prefix}{trailing_slash}$',
            mapping={
                'get': 'list',  # 群查
                'post': 'create',  # 单增,群增
                'put': 'multiple_update',  # 群整改
                'patch': 'multiple_partial_update',  # 群局改
                'delete': 'multip_destroy',  # 群删
            },
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),

        # Dynamically generated list routes. Generated using
        # @action(detail=False) decorator on methods of the viewset.
        DynamicRoute(
            url=r'^{prefix}/{url_path}{trailing_slash}$',
            name='{basename}-{url_name}',
            detail=False,
            initkwargs={}
        ),

        # detail route  /资源s/(pk)/
        Route(
            url=r'^{prefix}/{lookup}{trailing_slash}$',
            mapping={
                'get': 'retrieve',  # 单查
                'put': 'update',  # 单整改
                'patch': 'partial_update',  # 单局改
                'delete': 'destroy'  # 单删
            },
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Instance'}
        ),

        # Dynamically generated detail routes. Generated using
        # @action(detail=True) decorator on methods of the viewset.
        DynamicRoute(
            url=r'^{prefix}/{lookup}/{url_path}{trailing_slash}$',
            name='{basename}-{url_name}',
            detail=True,
            initkwargs={}
        ),
    ]


# 对外提供十大接口的router对象
router = SimpleRouter()
# eg: router.register('users', UserModelViewSet, basename='user')
"""
/users/
'get': 'list',  # 群查
'post': 'create',  # 单增、群增
'put': 'multiple_update',  # 群整改
'patch': 'multiple_partial_update',  # 群局改
'delete': 'multiple_destroy',  # 群删

'get': 'retrieve',  # 单查
'put': 'update',  # 单整改
'patch': 'partial_update',  # 单局改
'delete': 'destroy'  # 单删
"""