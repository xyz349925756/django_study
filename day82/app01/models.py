from django.db import models


# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    repeat_password = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    gender_choices = (
        (1, 'male'),
        (2, 'woman'),
        (3, 'other')
    )
    gender = models.IntegerField(choices=gender_choices)


class LoginUser(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    UserType = (
        (1, '超级管理员'),
        (2, '管理员'),
        (3, '普通用户'),
        (4, '受限用户')
    )
    usertype = models.IntegerField(choices=UserType)


class UserToken(models.Model):
    user = models.OneToOneField(to='LoginUser', on_delete=models.CASCADE)
    token = models.CharField(max_length=64)
