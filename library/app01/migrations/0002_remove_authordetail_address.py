# Generated by Django 4.1 on 2022-09-17 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authordetail',
            name='address',
        ),
    ]