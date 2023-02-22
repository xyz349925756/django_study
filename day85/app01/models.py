from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


# 写一个基类也就是后面的都共有的field

class BaseMode(models.Model):
    is_delete = models.BooleanField(default=False,verbose_name='是否删除')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    # 记录创建的时间,用途用户创建时间
    last_update = models.DateTimeField(auto_now=True,verbose_name='最近一次修改时间')

    # 记录最近一次修改的时间, 用途用户最后一次登录时间

    class Meta:
        abstract = True  # 声明此表为抽象表,不在数据库中创建表



# 后面的表有上面base中的field就直接继承base
class Book(BaseMode):
    id = models.AutoField(primary_key=True)  # 一般不用写.orm自动会创建
    # verbose_name admin中显示中文
    name = models.CharField(max_length=32, verbose_name='书名', help_text='这里填写书名')
    price = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='价格')

    # 这里其实还有一个默认参数to_field,关联到Publish的主键上primary_key上面...默认是不写的.
    # 这里特别注意on_delete 联动删除,一本书对应一个出版社,反过来,一个出版社有N本书,这里假如删除了一本书,联动了那么
    #    这个出版社publish 也被删除了.所以这里不能联动删除.
    # db_constraint =False 逻辑上的关联,实际上没有外键联系,增删不会受外键影响,查询不受影响,
    #    在视图模型中是看不到那条外键关联的线
    publish = models.ForeignKey(to='Publish', on_delete=models.DO_NOTHING, db_constraint=False,verbose_name='出版社')

    # 书的作者一般是一个人写一本,但是很多是合作的.面对这种清空不能使用OneToOne,逻辑上的关联.
    author = models.ManyToManyField(to='Author', db_constraint=False,verbose_name='作者')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '书'

    @property
    def publish_name(self):
        return self.publish.name

    # author 这里是多对多关系按照上面publish 肯定不行了
    @property
    def author_name(self):
        # 先列出所有author
        author_list = self.author.all()
        # author_name = []
        # for author in author_list:
        #     author_name.append({'name':author.name,'gender':author.get_gender_display()})
        # return author_name

        return [{'name':author.name,'gender':author.get_gender_display()} for author in author_list]


# 关于on_delete 的参数说明:
# 级联关系:
# on_delete = models.CASCADE  级联删除删除书,出版社夜奔删除了.逻辑错误
# on_delete = models.DO_NOTHING 什么也不做
# on_delete = models.SET_NULL  null=True  部门没有了,员工所属部门设置为空
# on_delete = models.SET_DEFAULT default=0  当前部门没有了,员工进入默认部门


class Publish(BaseMode):
    name = models.CharField(max_length=32, verbose_name='出版社名', help_text='出版社')
    addr = models.CharField(max_length=64, verbose_name='出版社地址', help_text='出版社地址')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '出版社'

class Author(BaseMode):
    name = models.CharField(max_length=32, verbose_name='姓名', help_text='作者姓名')
    gender_list = (
        (1, '男'),
        (2, '女'),
        (3, '保密')
    )
    gender = models.IntegerField(choices=gender_list,verbose_name='性别')

    # OneToOne 写在查询频率高的一边,
    # 本质就是Foreign+unique.
    authordetail = models.OneToOneField(to='AuthorDetail', on_delete=models.CASCADE, db_constraint=True,verbose_name='作者详情')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '作者'

class AuthorDetail(BaseMode):
    add = models.CharField(max_length=128,verbose_name='作者地址')
    phone = models.BigIntegerField(verbose_name='电话号码') # max_length 不能限制,后期在校验的时候记得校验电话号码即可

    def __str__(self):
        return self.author.name

    class Meta:
        verbose_name_plural = '作者详情'
