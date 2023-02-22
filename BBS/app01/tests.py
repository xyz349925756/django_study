from django.test import TestCase

# Create your tests here.
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BBS.settings')
    import django
    django.setup()
    from app01 import models

    article_queryset = models.Article.objects.all()
    res = article_queryset
    print(res)