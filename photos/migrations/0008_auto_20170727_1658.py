# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_auto_20170727_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='photos',
            field=models.ManyToManyField(related_name='color', related_query_name='color', to='photos.Photo'),
        ),
    ]
