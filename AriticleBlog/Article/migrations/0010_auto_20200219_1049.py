# Generated by Django 2.2.1 on 2020-02-19 10:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0009_article_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='内容'),
        ),
    ]
