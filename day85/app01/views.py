from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from rest_framework.response import Response

from app01.ser import BookModelSerializer, BookListSerializer
from app01 import models


class BookAPIView(APIView):
    """
    get:
    返回所有或者单一book信息

    post:
    创建新的数据,使用列表可以创建多条数据,使用json格式单条.

    put:
    修改单条数据或者多条数据,修改数据必须带上id

    delete:
    删除单条或批量删除数据,删除的数据你无法查看,但是紧急情况下可以恢复.

    """

    def get(self, request, *args, **kwargs):
        # print(kwargs)  #{'pk': '1'}
        if kwargs:
            # print('1')
            book_list = models.Book.objects.filter(is_delete=False).filter(id=kwargs['pk']).first()
            book_list_ser = BookModelSerializer(book_list)
            return Response(data=book_list_ser.data)

        else:
            # print('2')
            book_list = models.Book.objects.all().filter(is_delete=False)  # 过滤没有标记is_delete的field
            book_list_ser = BookModelSerializer(book_list, many=True)
            return Response(data=book_list_ser.data)

    def post(self, request, *args, **kwargs):
        if isinstance(request.data, dict):  # 判断对象是否是一个已知类型
            book_ser = BookModelSerializer(data=request.data)
            # book_ser.is_valid(raise_exception=True)
            # book_ser.save()
            # return Response(data=book_ser.data)
        elif isinstance(request.data, list):
            book_ser = BookModelSerializer(data=request.data, many=True)
            # print(type(book_ser)) #<class 'rest_framework.serializers.ListSerializer'>
        book_ser.is_valid(raise_exception=True)
        book_ser.save()
        return Response(data=book_ser.data)

    def put(self, request, *args, **kwargs):
        # print(kwargs)  #{'pk': '4'}
        # print(request.data)  # {'name': '红女', 'price': '30.02', 'publish': '3', 'author': [2]}
        # print(kwargs.get('pk',None)) # 判断key的type  #4

        if kwargs.get('pk', None):  # 如果pk 不存在返回None
            book = models.Book.objects.filter(id=kwargs.get('pk')).first()
            book_ser = BookModelSerializer(instance=book, data=request.data, partial=True)
            book_ser.is_valid(raise_exception=True)
            book_ser.save()
            return Response(data=book_ser.data)
        else:
            # 怎么修改多个?像create那样?数据传入是[{},{}]字典里面是对应的id ,name price,publish,author
            # 批量修改不能确定当前修改的ID是是不是被修改对象的.
            # 第一种方法
            book_list = []
            modify_data = []
            for item in request.data:
                # print(item) #{'name': '调大仙2', 'price': '333.33', 'publish': '1', 'author': [2]}
                # 从上面可知想要修改就必须携带ID一起传过来,有误差存在?肯定有的.这种方法只能用来加深理解.现实中批量修改的情况很少
                pk = item.pop('id')
                book = models.Book.objects.get(pk=pk)
                book_list.append(book)
                print('views', book_list)  # [<Book: 红尘女>]
                modify_data.append(item)
                print('views data', modify_data)  # [{'name': '红尘', 'price': '6.02', 'publish': '1', 'author': [2]}]

                # 这种方法必须重写listserializer的update方法
            book_ser = BookModelSerializer(instance=book_list, data=modify_data, many=True)
            book_ser.is_valid(raise_exception=True)
            book_ser.save()
            return Response(book_ser.data)

    def delete(self, request, *args, **kwargs):
        # if kwargs:
        #     pk = kwargs.get('pk')
        #     models.Book.objects.filter(pk=pk,is_delete=False).update(is_delete=True)
        #     return Response('删除成功')
        # else:
        #     return Response('不能批量删除')
        pk = kwargs.get('pk')
        pks = []
        if pk:
            pks.append(pk)
        else:
            # 让前端传入{'pks':[1,2,3]} 这种格式的数据
            pks = request.data.get('pks')

        ret = models.Book.objects.filter(pk__in=pks, is_delete=False).update(is_delete=True)

        if ret:
            return Response('删除成功')
        else:
            return Response('没有要删除的数据')


from rest_framework.generics import ListAPIView,GenericAPIView
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class Paginations(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
    page_size_query_param = 'size' #http://127.0.0.1:8000/api/book2/?size=5
    max_page_size = 4
    # default_limit = 3  # 每页显示的条数
    # limit_query_param = 'limit'  # 限制拿几条数据
    # offset_query_param = 'offset'   # 偏移查询
    # max_limit = None  # 每页最大多少
    # cursor_query_param = 'cursor'
    # page_size = 2
    # ordering = '-id'

# class BookView(ListAPIView):
#     queryset = models.Book.objects.all().filter(is_delete=False)
#     serializer_class = BookModelSerializer
#
#     pagination_class = Paginations

from app01.Throttle import Throttle
class BookView(APIView):
    throttle_classes = [Throttle]

    def get(self,request,*args,**kwargs):
        book_list = models.Book.objects.all().filter(is_delete=False)
        page_cursor = Paginations()

        book_list = page_cursor.paginate_queryset(book_list,request,view=self)
        next_url = page_cursor.get_next_link()
        pr_url = page_cursor.get_previous_link()
        book_ser = BookModelSerializer(book_list,many=True)
        data1 ={}
        data1['next_url'] = next_url
        data1['pr_url'] = pr_url
        data1['data'] = book_ser.data
        return Response(data=data1)




