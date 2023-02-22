from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,render,redirect

class MyMiddleware1(MiddlewareMixin):

    def process_request(self, request):
        print('第一个中间件的process_request方法')
        # return HttpResponse('第一个process_request,return Httpresponse')

    def process_response(self,request,response):
        print('第一个process-response方法')
        # return response
        return HttpResponse('第一个 process-respose方法')



class MyMiddleware2(MiddlewareMixin):

    def process_request(self,request):
        print('第2个中间件的process_request方法')
        # return HttpResponse('第二个 return Httpresponse ')

    def process_response(self,request,response):
        print('第二个process_response方法')
        return HttpResponse('第二个process-response方法')