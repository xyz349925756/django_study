from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if not response:
        if isinstance(exc, ZeroDivisionError):
            response.data1 = {'status': 888, 'msg': "除以0的错误" + str(exc)} + status.HTTP_400_BAD_REQUEST
            return Response(response.data1)
        response.data2 = {'status': 999, 'msg': str(exc)} + status.HTTP_400_BAD_REQUEST
        return Response(response.data2)
    else:
        response.data3 = {'status': 666, 'msg': response.data.get('detail')} + status.HTTP_400_BAD_REQUEST
        return Response(response.data3)
