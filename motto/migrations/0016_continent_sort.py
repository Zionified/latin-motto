# Generated by Django 3.0.8 on 2020-09-20 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motto', '0015_auto_20200920_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='continent',
            name='sort',
            field=models.IntegerField(default=0, verbose_name='排序'),
        ),
    ]