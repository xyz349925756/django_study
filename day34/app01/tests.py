from django.test import TestCase

# Create your tests here.
import os
import sys
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'day34.settings')
    import django
    django.setup()

    import importlib
    res = 'myfile.a'
    res1 = importlib.import_module(res)
    print(res1)