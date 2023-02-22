from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='主键')
    #等价于mysql的 id int primary_key auto_increment
    username = models.CharField(max_length=32,verbose_name='用户名')
    # 等价于 username varchar(32)
    password = models.IntegerField(verbose_name='密码')
    # 等价于 password int

class Author(models.Model):
    username = models.CharField(max_length=32)
    password = models.IntegerField()
    info = models.CharField(max_length=32,verbose_name='备注',null=True)
    hobby = models.CharField(max_length=32,verbose_name='兴趣',default='games')
