# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-01 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentence', '0022_auto_20161231_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentence',
            name='Link',
            field=models.TextField(default='unknown'),
        ),
    ]
