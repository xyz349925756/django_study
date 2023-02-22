from django.shortcuts import render

# Create your views here.

# from rest_framework.viewsets import ModelViewSet
# from .models import Book,Student
# from app01.apis.books_api import BookModelSerializer,StudentSerializer
#
# from django.views import View
# from rest_framework.views import APIView
# from rest_framework.request import Request
#
# class BooksViewSet(ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookModelSerializer
#
# class StudentViewSet(ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

from rest_framework.views import APIView
from app01 import models
from app01.apis.books_api import StuSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


class StuView(APIView):

    def get(self, request, pk):  # pk 就是url中返回的stus/pk
        stu = models.Student.objects.filter(id=pk).first()
        stu_ser = StuSerializer(stu)  # 要序列化那个就传入那个实例化对象,调用class __init__方法
        # print(stu_ser.data)
        return Response(stu_ser.data)

    def put(self, request, pk):
        response_msg = {'status': 100, 'msg': '成功'}
        stu = models.Student.objects.filter(id=pk).first()
        stu_ser = StuSerializer(stu, request.data)
        # 用request.data 数据修改stu
        if stu_ser.is_valid():
            stu_ser.save()
            response_msg['data'] = stu_ser.data
        else:
            response_msg['status'] = 400
            response_msg['msg'] = "失败"
            # response_msg['data'] = stu_ser.errors
            response_msg['data'] = stu_ser.errors
        return Response(response_msg)

    def delete(self, request, pk):
        res = models.Student.objects.filter(pk=pk).delete()
        return Response({'code': 100, 'msg': '删除成功'})


class StusView(APIView):
    def get(self, request):
        response_msg = {'code': 10, 'msg': 'success'}
        stus = models.Student.objects.all()
        stus_ser = StuSerializer(stus, many=True)
        response_msg['data'] = stus_ser.data
        return Response(response_msg)

    def post(self, request):
        response_msg = {'code': 10, 'msg': 'success'}
        # ;instance 的因为只有修改才有instance的,这里需要添加data 默认位置参数是instance
        stu_ser = StuSerializer(data=request.data)

        if stu_ser.is_valid():
            stu_ser.save()
            response_msg['data'] = stu_ser.data
        else:
            response_msg['code'] = 11
            response_msg['msg'] = stu_ser.errors
        return Response(response_msg)


from app01.apis.books_api import StuModelSerializer
from app01.models import Student


class SstuView(APIView):

    def get(self, request):
        back_dic = {'code': 10, 'msg': 'success'}
        stu = Student.objects.all()
        stu_ser = StuModelSerializer(stu, many=True)
        back_dic['data'] = stu_ser.data
        return Response(back_dic)


from app01.utils.MyStaticCode import MyStaticCode
from rest_framework.generics import GenericAPIView
from app01.apis.books_api import StuSerializer


class Stu1View(GenericAPIView):
    queryset = models.Student.objects
    serializer_class = StuSerializer

    def get(self, request):
        res = MyStaticCode()
        stu1_list = self.get_queryset()
        stu1_ser = self.get_serializer(stu1_list, many=True)
        res.data = stu1_ser.data
        return Response(res.get_dict)

    def post(self, request):
        res = MyStaticCode()
        stu1_ser = self.get_serializer(data=request.data)
        if stu1_ser.is_valid():
            stu1_ser.save()
            res.data = stu1_ser.data
            return Response(res.get_dict)
        else:
            res.status = 101
            res.msg = stu1_ser.errors  # 使用默认field字段属性了.
            return Response(res.get_dict)


class Stu1DetailView(GenericAPIView):
    queryset = models.Student.objects
    serializer_class = StuSerializer

    def get(self, request, pk):
        res = MyStaticCode()
        stu1 = self.get_object()
        stu1_ser = self.get_serializer(stu1)
        res.data = stu1_ser.data
        return Response(res.get_dict)

    def put(self, request, pk):
        res = MyStaticCode()
        stu1 = self.get_object()
        stu1_ser = self.get_serializer(instance=stu1, data=request.data)
        if stu1_ser.is_valid():
            stu1_ser.save()
            res.data = stu1_ser.data
            return Response(res.get_dict)
        else:
            res.status = 102
            res.msg = stu1_ser.errors
            return Response(res.get_dict)

    def delete(self, request, pk):
        res = MyStaticCode()
        stu1 = self.get_object()
        stu1_ser = self.get_serializer(stu1)
        self.get_object().delete()
        res.status = 600
        res.msg = f'{stu1_ser.data["name"]} 删除成功!'
        return Response(res.get_dict)


from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, \
    RetrieveModelMixin


class Stu2View(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = models.Student.objects
    serializer_class = StuSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class Stu3View(GenericAPIView,UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin):
    queryset = models.Student.objects
    serializer_class = StuSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.delete(request, pk)

from rest_framework.viewsets import ModelViewSet
class Stu4View(ModelViewSet):
    queryset = models.Student.objects
    serializer_class = StuSerializer

from rest_framework.viewsets import ViewSetMixin
class Stu5Views(ViewSetMixin,APIView):
    def get_all_stu(self,request):
        stu_list = models.Student.objects
        stu_ser = StuSerializer(stu_list,many=True)
        print('xx')
        return Response(stu_ser.data)

