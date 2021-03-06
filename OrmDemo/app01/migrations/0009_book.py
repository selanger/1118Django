# Generated by Django 2.2.1 on 2020-02-13 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='书名')),
                ('pub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Publish')),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
