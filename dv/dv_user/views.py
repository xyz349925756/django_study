from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from dv_user import models
from utils.bookserializer import BookSerializer


# Create your views here.


class BookView(APIView):

    def get(self, request):
        back_dic = {"code": 0, "message": "success"}
        book = models.Books.objects.all()
        book_ser = BookSerializer(book,many=True)
        back_dic["data"] = book_ser.data
        return Response(back_dic)
