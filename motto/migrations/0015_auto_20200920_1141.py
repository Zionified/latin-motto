# Generated by Django 3.0.8 on 2020-09-20 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motto', '0014_grammarabbreviation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chinese_name', models.CharField(max_length=128, unique=True, verbose_name='中文名')),
                ('english_name', models.CharField(max_length=128, unique=True, verbose_name='英语名')),
                ('status', models.CharField(choices=[('DELETED', '删除'), ('NORMAL', '正常'), ('HIDDEN', '隐藏')], db_index=True, default='NORMAL', max_length=32, verbose_name='状态')),
            ],
            options={
                'db_table': 'continent',
            },
        ),
        migrations.AlterField(
            model_name='grammarabbreviation',
            name='chinese_name',
            field=models.CharField(blank=True, max_length=64, verbose_name='中文名'),
        ),
        migrations.AlterField(
            model_name='grammarabbreviation',
            name='english_name',
            field=models.CharField(blank=True, max_length=64, verbose_name='英文名'),
        ),
        migrations.AddField(
            model_name='region',
            name='continent',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='motto.Continent'),
        ),
        migrations.AddField(
            model_name='school',
            name='continent',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='motto.Continent'),
        ),
    ]
