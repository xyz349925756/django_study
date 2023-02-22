from django.db import models


# Create your models here.

# class User(models.Model):
#     name = models.CharField(max_length=32)
#     age = models.IntegerField()
#     # register_time = models.DateTimeField()  #　年月日
#     register_time = models.DateField()  # 年月日
#
#     def __str__(self):
#         return f'Object Is :{self.name}'

class MyCharField(models.Field):
    def __init__(self, max_length, *args, **kwargs):
        self.max_length = max_length
        # 调用父类的init方法
        super().__init__(max_length=max_length, *args, **kwargs)
        # 参数是关键字形式传入

    def db_type(self, connection):
        """
        返回真正的数据类型及各种约束条件
        :param connection:
        :return:
        """
        return f'char {self.max_length}'


class Book(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publish_date = models.DateField(auto_now_add=True)

    # 库存
    kucun = models.IntegerField(default=1000)
    # 卖出
    maichu = models.IntegerField(default=1000)

    # 自定义字段使用
    myfield = MyCharField(max_length=16, null=True)

    # 一对多
    publish = models.ForeignKey(to='Publish', on_delete=models.CASCADE)
    # 多对多
    authors = models.ManyToManyField(to='Author')

    def __str__(self):
        return self.name


class Publish(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    email = models.EmailField()

    # 这里的字段是varchar(254) 该字段是给校验性组件看的。

    def __str__(self):
        return f'对象: {self.name}'


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    # 一对一
    author_detail = models.OneToOneField(to='AuthorDetail', on_delete=models.CASCADE)


class AuthorDetail(models.Model):
    phone = models.BigIntegerField()
    addr = models.CharField(max_length=64)

