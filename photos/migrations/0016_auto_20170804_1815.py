# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-04 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0015_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='color1',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='photo',
            name='color2',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='photo',
            name='color3',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_id',
            field=models.CharField(default='', max_length=20),
        ),
    ]