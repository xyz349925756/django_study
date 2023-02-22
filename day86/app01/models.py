from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    is_delete = models.BooleanField(default=False, verbose_name='删除功能', help_text='删除功能')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='注册时间后期不能更改')
    last_update = models.DateTimeField(auto_now=True, verbose_name='最后一次更新')
