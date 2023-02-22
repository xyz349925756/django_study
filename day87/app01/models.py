from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_num = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.username


class Book(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
