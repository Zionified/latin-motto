# Generated by Django 3.0.8 on 2020-09-27 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motto', '0018_region_extra'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='image1',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='uploads/image1/', verbose_name='image1'),
        ),
        migrations.AddField(
            model_name='school',
            name='image2',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='uploads/image2/', verbose_name='image1'),
        ),
        migrations.AlterField(
            model_name='region',
            name='continent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='motto.Continent'),
        ),
    ]
