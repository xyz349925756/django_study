# Generated by Django 4.1.3 on 2022-12-17 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authordetail',
            name='phone',
            field=models.BigIntegerField(max_length=11),
        ),
    ]
