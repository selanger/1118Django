# Generated by Django 2.2.1 on 2020-02-27 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0003_auto_20200227_1149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payorder',
            old_name='order_staus',
            new_name='order_status',
        ),
    ]
