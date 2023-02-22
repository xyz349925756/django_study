from django.test import TestCase

# Create your tests here.
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'day32.settings')
    import django
    django.setup()

    from app01 import models

    # models.User.objects.create(username='tom', age=24, gender=1, score='A')
    # models.User.objects.create(username='jack',age=67,gender=1,score='D')
    # models.User.objects.create(username='rocky',age=99,gender=3,score='C')

    # res = models.User.objects.filter(pk=1).values()
    res = models.User.objects.all()
    # print(res.get_gender_display(),res.get_score_display())
    # 使用get_字段名_display()  就可以获取对应的信息

    res.filter(pk=8)
    print(res.filter(pk=8).first().username)