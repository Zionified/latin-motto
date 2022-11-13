# Generated by Django 3.0.8 on 2020-08-26 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0002_auto_20200708_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatinWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('words', models.CharField(max_length=255, verbose_name='单词列表')),
                ('word_class', models.CharField(db_index=True, max_length=64, verbose_name='词类')),
                ('main_attr', models.CharField(choices=[('I Declension', '第一变格'), ('I and II Declension', '第一/第二变格'), ('II Declension', '第二变格'), ('III Declension', '第三变格'), ('IV Declension', '第四变格'), ('V Declension', '第五变格'), ('Indeclinable', ''), ('Irregular Declension', ''), ('Irregular', ''), ('I Conjugation', '第一变位'), ('II Conjugation', '第二变位'), ('III Conjugation', '第三变位'), ('IV Conjugation', '第四变位'), ('', '')], db_index=True, max_length=64, verbose_name='变位/变格')),
                ('other_attrs', models.CharField(choices=[('Masculine', '阳性'), ('Feminine', '阴性'), ('Neuter', '中性'), ('Common', ''), ('All/Other', ''), ('Positive', ''), ('Distributive', ''), ('Ablative', ''), ('Accusative', ''), ('Adverbial', ''), ('Cardinal', ''), ('Ordinal', ''), ('Genitive', ''), ('Superlative', ''), ('Comparative', ''), ('', '')], db_index=True, max_length=64, verbose_name='其他属性')),
                ('raw_meanings', models.TextField(verbose_name='原始释义')),
                ('translated_meanings', models.TextField(verbose_name='翻译释义')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'db_table': 'latin_word',
            },
        ),
    ]
