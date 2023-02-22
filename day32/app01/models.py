from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=32)
    age = models.IntegerField()
    gender_choices = (
        (1, '男'),
        (2, '女'),
        (3, '其他'),
    )
    gender = models.IntegerField(choices=gender_choices)

    score_choices = (
        ('A', '优秀'),
        ('B', '良好'),
        ('C', '及格'),
        ('D', '不合格'),
    )

    score = models.CharField(max_length=32, choices=score_choices, null=True)

    te = models.ForeignKey(to='Te', on_delete=models.CASCADE)


class Te(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=32)
    phone = models.BigIntegerField(verbose_name='手机号码', unique=True, null=True)
    job = models.CharField(max_length=32, verbose_name='职业', blank=True, null=True, default='IT')  # blank表单认证,字段填写不为空
    date = models.DateField(verbose_name='date', help_text='yyyy-mm-dd', blank=True, null=True)


class Book(models.Model):
    name = models.CharField(verbose_name='书名', max_length=64)
    publish = models.CharField(verbose_name='出版社名', max_length=32)
    authors = models.ManyToManyField(to='Author',
                                     through='Book2Author',
                                     through_fields=('book', 'author')
                                     )


class Publish(models.Model):
    name = models.CharField(max_length=32)


class Book2Publish(models.Model):
    book_id = models.ForeignKey(to='Book', on_delete=models.CASCADE)
    publish_id = models.ForeignKey(to='Publish', on_delete=models.CASCADE)


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()


class Book2Author(models.Model):
    book = models.ForeignKey(to='Book', on_delete=models.CASCADE)
    author = models.ForeignKey(to='Author', on_delete=models.CASCADE)


