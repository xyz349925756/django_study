from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser  # 继承AbstractUser 属性


# 这里继承了Abstractuser 默认已经有username 等字段也就是拥有auth_user中所有的字段了。
class UserInfo(AbstractUser):
    phone = models.BigIntegerField(verbose_name='手机号', null=True, blank=True)
    """
    null=True,   数据库允许为空
    blank=True   admin后台管理该字段可以为空
    """
    avatar = models.FileField(upload_to='avatar/', default='avatar/default.png', verbose_name='用户默认头像')
    create_time = models.DateField(auto_now_add=True)

    blog = models.OneToOneField(to='Blog', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = '用户表'

    def __str__(self):
        return self.username


class Blog(models.Model):
    site_name = models.CharField(verbose_name='站点名称', max_length=32)
    site_title = models.CharField(verbose_name='站点标题', max_length=32)
    site_theme = models.CharField(verbose_name='站点主题', max_length=64)

    class Meta:
        verbose_name_plural = '博客表'

    def __str__(self):
        return self.site_name


class Category(models.Model):
    name = models.CharField(verbose_name='文章分类', max_length=32)

    blog = models.ForeignKey(to='Blog', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = '分类表'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(verbose_name='文章标签', max_length=32)

    blog = models.ForeignKey(to='Blog', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = '标签表'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(verbose_name='文章标题', max_length=64)
    desc = models.CharField(verbose_name='文章简介', max_length=255)

    content = models.TextField(verbose_name='文章内容')
    create_time = models.DateField(auto_now_add=True)

    up_num = models.BigIntegerField(verbose_name='点赞数', default=0)
    down_num = models.BigIntegerField(verbose_name='踩数', default=0)
    comment_num = models.BigIntegerField(verbose_name='评论数', default=0)

    blog = models.ForeignKey(to='Blog', null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(to='Category', null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(
        to='Tag',
        through='Article2Tag',
        through_fields=('article', 'tag')
    )

    class Meta:
        verbose_name_plural = '内容表'

    def __str__(self):
        return self.title


class Article2Tag(models.Model):
    article = models.ForeignKey(to='Article', on_delete=models.CASCADE)
    tag = models.ForeignKey(to='Tag', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = '内容标签对应表'


class UpAndDown(models.Model):
    user = models.ForeignKey(to='UserInfo', on_delete=models.CASCADE)
    article = models.ForeignKey(to='Article', on_delete=models.CASCADE)
    is_up = models.BooleanField()

    class Meta:
        verbose_name_plural = '点赞表'


class Comment(models.Model):
    user = models.ForeignKey(to='UserInfo', on_delete=models.CASCADE)
    article = models.ForeignKey(to='Article', on_delete=models.CASCADE)

    content = models.CharField(verbose_name='评论内容', max_length=255, )
    comment_time = models.DateTimeField(verbose_name='评论时间', auto_now_add=True)
    # 自关联
    parent = models.ForeignKey(to='self', null=True, on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name_plural = '评论表'
