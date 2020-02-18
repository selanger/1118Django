# Generated by Django 2.2.1 on 2020-02-18 03:03

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0004_auto_20200218_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='recommend',
            field=models.IntegerField(default=0, verbose_name='推荐'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='描述'),
        ),
    ]
