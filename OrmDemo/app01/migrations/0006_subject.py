# Generated by Django 2.2.1 on 2020-02-13 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20200213_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('start_time', models.DateField()),
            ],
            options={
                'db_table': 'subject',
            },
        ),
    ]