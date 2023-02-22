from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=11)
    avatar = models.ImageField(upload_to='icon',default='icon/default.png')

    class Meta:
        verbose_name_plural = '用户表'

    def __str__(self):
        return self.username


class Books(models.Model):
    name = models.CharField(max_length=128)
    publish = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    author = models.CharField(max_length=64)
    book_image = models.ImageField(upload_to='book_image',default='book_image/default.png')

    class Meta:
        verbose_name_plural = '书'

    def __str__(self):
        return self.name
