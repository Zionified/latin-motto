# Generated by Django 3.0.8 on 2020-09-03 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motto', '0011_auto_20200903_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='mottoword',
            name='word_info_id',
            field=models.IntegerField(db_index=True, default=0, verbose_name='单词详情ID'),
        ),
    ]
