# Generated by Django 2.2.1 on 2020-02-27 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0002_auto_20200227_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payorder',
            name='order_number',
            field=models.CharField(max_length=36, unique=True, verbose_name='订单号'),
        ),
    ]