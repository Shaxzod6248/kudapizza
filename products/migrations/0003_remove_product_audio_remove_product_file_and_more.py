# Generated by Django 4.1 on 2022-08-17 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_order_detail_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='audio',
        ),
        migrations.RemoveField(
            model_name='product',
            name='file',
        ),
        migrations.RemoveField(
            model_name='product',
            name='video',
        ),
    ]
