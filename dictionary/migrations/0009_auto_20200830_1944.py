# Generated by Django 3.0.8 on 2020-08-30 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0008_auto_20200830_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latinword',
            name='sources',
            field=models.TextField(default='[]', verbose_name='来源'),
        ),
    ]
