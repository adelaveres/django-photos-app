# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 12:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20170727_1526'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='color',
            new_name='colors',
        ),
    ]
