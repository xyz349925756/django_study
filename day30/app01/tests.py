from django.test import TestCase

# Create your tests here.
import os

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'day30.settings')
    import django

    django.setup()

    from app01 import models

    # res = models.User.objects.create(name='Tom',age=36,register_time='2019-2-28')
    # print(res)
    # import datetime
    # ctime = datetime.datetime.now()
    # user_obj = models.User(name='jack',age=77,register_time=ctime)
    # user_obj.save()
    # user_obj = models.User.objects.filter(pk=5)

    # res = models.User.objects.filter(pk=102).delete()
    # print(res)

    # res = models.User.objects.filter(pk=101).first()
    # res.delete()

    # models.User.objects.filter(pk=2).update(name='Tom')

    # user_obj = models.User.objects.get(pk=3)
    # user_obj.name = 'jack'
    # user_obj.save()
    # print(user_obj)

    # user_obj = models.User.objects.filter(pk=5)
    # print(user_obj)  #<QuerySet [<User: Object Is :Brenda Olson>]>

    # res = models.User.objects.all()
    # res = models.User.objects.filter(pk=2)
    # res = models.User.objects.get(pk=2)
    # res = models.User.objects.first()
    # res = models.User.objects.last()
    # res = models.User.objects.values('name','age')  #<QuerySet [{'name': 'Kao Yun Fat', 'age': 97}...
    # res = models.User.objects.values_list('name','age')  #<QuerySet [('Kao Yun Fat', 97)...
    # res = models.User.objects.values('name','age').distinct()
    # res = models.User.objects.order_by('age') # 升序
    # res = models.User.objects.order_by('-age').reverse()  #降序
    # res = models.User.objects.count()
    # res = models.User.objects.exclude('Tom')
    # res = models.User.objects.values('name','age')
    # print(res)

    # 年龄大于35的
    # res = models.User.objects.filter(age__gt=35)
    # print(res)

    # 年龄小于35
    # res = models.User.objects.filter(age__lt=35)
    # print(res)

    # 大于等于80，小于等于10
    # res = models.User.objects.filter(age__gte=80)
    # res1 = models.User.objects.filter(age__lte=10)
    # print(res,'\n',res1)

    # 年龄在是40 或者50 或者60
    # res = models.User.objects.filter(age__in=[40,50,60])
    # print(res)

    # 年龄在40-60之间的
    # res = models.User.objects.filter(age__range=[40,60])
    # print(res)

    # 查询名字中含有's'的数据，模糊查询
    # res = models.User.objects.filter(name__contains='s')
    # print(res.count())

    # 区分大小写
    # res = models.User.objects.filter(name__contains='T')
    # print(res)

    # 忽略大小写
    # res = models.User.objects.filter(name__icontains='t')
    # print(res.count())

    # 以T开头的name
    # res = models.User.objects.filter(name__startswith='T')
    # 以m结尾的name
    # res1 = models.User.objects.filter(name__endswith='m')
    # print(res,'\n',res1)

    # 查询2005-11 出生的人
    # res = models.User.objects.filter(register_time__year='2005',register_time__month='11') # 可以单开指定某年，某月，某日
    # print(res)

    # 增
    # 第一种
    # models.Book.objects.create(name='铁齿铜牙纪晓岚',price=54.36,publish_id=1)
    # models.Book.objects.create(name='九五至尊',price='24.5',publish_id=2)
    # models.Book.objects.create(name='康熙王朝',price='48.32',publish_id=1)
    # 第二种 object
    # publish_obj = models.Publish.objects.filter(pk=2).first()  # pk这里是固定的。
    # models.Book.objects.create(name='红楼梦',price=75.63,publish=publish_obj)

    # 删
    # models.Publish.objects.filter(pk=1).delete() # 可以看出book中的1对应的出版社的书全部被级联删除了。

    # 改
    # models.Book.objects.filter(pk=2).update(publish_id=3)

    # publish_obj = models.Publish.objects.filter(pk=2).first()
    # models.Book.objects.filter(pk=2).update(publish=publish_obj)

    # 如何给书籍添加作者
    # book_obj = models.Book.objects.filter(pk=2).first()
    # print(book_obj.authors)   # 类似于进入book_authors表
    # book_obj.authors.add(1)  #书籍id=2的书籍绑定一个主键为1的作者
    # book_obj.authors.add(2,3)

    # author_obj = models.Author.objects.filter(pk=2).first()
    # author_obj1 = models.Author.objects.filter(pk=3).first()
    # author_obj2 = models.Author.objects.filter(pk=1).first()
    # book_obj.authors.add(author_obj2)
    # book_obj.authors.add(author_obj,author_obj1)

    # 删
    # book_obj.authors.remove(1)   # 可以传多个参数

    # author_obj = models.Author.objects.filter(pk=2).first()
    # author_obj1 = models.Author.objects.filter(pk=3).first()
    # book_obj.authors.remove(author_obj,author_obj1)

    # 修改
    # book_obj.authors.set([1,2])  # 括号内必须给一个可迭代对象
    # book_obj.authors.set([3])

    # author_obj = models.Author.objects.filter(pk=2).first()
    # author_obj1 = models.Author.objects.filter(pk=3).first()
    # book_obj.authors.set([author_obj,author_obj1])

    # clear
    # book_obj.authors.clear()  # 清空书籍与作者的绑定关系

    # 查询书籍主键为1的出版社
    # book_obj = models.Book.objects.filter(pk=2).first()
    # # 书查出版社 正向
    # res = book_obj.publish
    # print(res)
    # print(res.name)
    # print(res.addr)

    # 查询书籍主键为2的作者
    # book_obj = models.Book.objects.filter(pk=2).first()
    # 书查作者
    # res = book_obj.authors  #app01.Author.None
    # res = book_obj.authors.all() #<QuerySet [<Author: Author object (1)>, <Author: Author object (2)>]>
    # print(res)

    # 查询作者的电话号码
    # author_obj =  models.Author.objects.filter(name='王璐').first()
    # res = author_obj.author_detail
    # print(res)
    # print(res.addr)
    # print(res.phone)

    # 查出版社是 秦記电脑有限责任公司 的书
    # publish_obj = models.Publish.objects.filter(name='秦記电脑有限责任公司').first()
    # 出版社 反向
    # res = publish_obj.book_set  #app01.Book.None
    # res = publish_obj.book_set.all()
    # print(res)

    # 查询作者是王璐写过的书
    # author_obj = models.Author.objects.filter(name='王璐').first()
    # 作者查书 反向
    # res = author_obj.book_set  #app01.Book.None
    # res = author_obj.book_set.all()  #<QuerySet [<Book: Book object (2)>]>
    # print(res)

    # 查询手机号是15933873485的作者姓名
    # author_obj = models.AuthorDetail.objects.filter(phone=15933873485).first()
    # res = author_obj.author
    # print(res)  # Author object (3)
    # print(res.name)

    # 查询王璐的手机号和姓名
    # res = models.Author.objects.filter(name='王璐').values('name','author_detail__phone')
    # print(res)

    # 反向
    # res = models.AuthorDetail.objects.filter(author__name='王璐')
    # <QuerySet [<AuthorDetail: AuthorDetail object (5)>]>
    # res = models.AuthorDetail.objects.filter(author__name='王璐').values('author__name','phone')
    # print(res)

    # 查询书籍主键为2的出版社名称和书名
    # res = models.Book.objects.filter(pk=2).values('publish__name','name')
    # print(res)

    # 反向
    # res = models.Publish.objects.filter(book__id=2).values('name','book__name')
    # print(res)

    # 查询书籍主键为2的作者姓名
    # 正向
    # res = models.Book.objects.filter(pk=2).values('name', 'authors__name')
    # print(res)
    # 反向
    # res = models.Author.objects.filter(book__id=2).values('name', 'book__name')
    # print(res)

    # 查询书籍主键是2 的作者的手机号
    # res = models.Book.objects.filter(pk=2).values('authors__name','authors__author_detail__phone')
    # print(res)

    # res = models.Author.objects.filter(book__id=2).values('name','author_detail__phone')
    # print(res)

    # res = models.AuthorDetail.objects.filter(author__book__id=2).values('author__name','phone')
    # print(res)

    # from django.db.models import  Max,Min,Avg,Sum,Count
    """
    跟数据库有关的在db里面
    """

    # 书的平均价格
    # res = models.Book.objects.aggregate(Avg('price'))
    # res = models.Book.objects.aggregate(Avg('price'),Max('price'),Min('price'),Sum('price'),Count('pk'))
    # print(res)

    # from  django.db.models import Max,Min,Sum,Avg,Count
    # 统计每一本书的作者个数
    # res = models.Book.objects.annotate() #<QuerySet [<Book: Book object (2)>,
    # res = models.Book.objects.annotate(author_num=Count('authors')).values('name','author_num')
    # <QuerySet [{'name': '九五至尊', 'author_num': 2},
    # print(res)
    """
    author_num 是自定义的字段,目的是用来存放统计出来的每本书的作者数
    """
    # res1 = models.Book.objects.annotate(author_num=Count('authors__id')).values('name','author_num')
    # print(res1)

    # 统计每个出版社最便宜的价格
    # res = models.Publish.objects.annotate(min_price=Min('book__price')).values('name','min_price')
    # print(res)

    # 统计不止一个作者的图书
       # 1. 先按照图书分组 求每一本对应的作者个数
       # 2. 过滤出不止一个作者的图书
    # res = models.Book.objects.annotate(author_num=Count('authors')).filter(author_num__gt=1).values('name','author_num')
    # print(res)
    # SELECT `app01_book`.`name`, COUNT(`app01_book_authors`.`author_id`) AS `author_num` FROM `app01_book` LEFT OUTER JOIN `app01_book_authors` ON (`app01_book`.`id` = `app01_book_authors`.`book_id`) GROUP BY `app01_book`.`id` HAVING COUNT(`app01_book_authors`.`author_id`) > 1 ORDER BY NULL LIMIT 21; args=(1,); alias=default
    """
    只要ORM语句得出的结果还是一个queryset对象,那么就可以继续无限制的queryset对象封装的方法
    """

    # 查询每个作者出的总价格
    # res = models.Author.objects.annotate(sum_price=Sum('book__price')).values('name','sum_price')
    # print(res)

    from django.db.models import F
    res = models.Book.objects.filter(maichu__gt=F('kucun'))
    print(res)




