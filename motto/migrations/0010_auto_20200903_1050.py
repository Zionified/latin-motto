# Generated by Django 3.0.8 on 2020-09-03 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motto', '0009_auto_20200903_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mottoword',
            name='extra',
            field=models.TextField(default='', verbose_name='补充说明'),
        ),
    ]
