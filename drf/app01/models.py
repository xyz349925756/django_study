from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=64,verbose_name='BookName')
    publishing = models.CharField(max_length=64,verbose_name='Publishing Company')
    price = models.DecimalField(max_digits=5,decimal_places=2)
    author = models.CharField(max_length=32)


class Student(models.Model):
    name = models.CharField(max_length=32,verbose_name="姓名", error_messages={
                                     'max_length':'最大值不能超过16位',
                                     'min_lenght':'最小不能低于3位',
                                     'required':'name 不能为空',
                                 })
    age = models.IntegerField(verbose_name="年龄",error_messages={
        'required':'age 不能为空',
    })
    score_choices = {
        (1,'A'),
        (2,'B'),
        (3,'C'),
        (4,'D'),
        (5,'E')
    }
    score = models.IntegerField(choices=score_choices,error_messages={
        'required':'score 不能为空'
    })
