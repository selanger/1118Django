# Generated by Django 2.2.1 on 2020-02-25 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0003_loginuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginuser',
            name='user_type',
            field=models.IntegerField(default=1, verbose_name='用户身份'),
        ),
    ]