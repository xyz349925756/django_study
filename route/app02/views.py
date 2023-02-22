from django.shortcuts import render,redirect,reverse,HttpResponse

# Create your views here.

def test(request):
    return HttpResponse('test_app02')
