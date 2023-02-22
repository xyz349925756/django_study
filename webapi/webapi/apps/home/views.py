from django.shortcuts import render, HttpResponse

# Create your views here.
from django.core.mail import send_mail
from webapi.settings import dev


def send_email(request):
    send_mail(
        subject='邮件标题',
        message='Email 内容',
        from_email=dev.EMAIL_HOST_USER,
        recipient_list=dev.ADMINS,
        fail_silently=False
    )
    return HttpResponse('ok')


def index(request):
    return HttpResponse('index')