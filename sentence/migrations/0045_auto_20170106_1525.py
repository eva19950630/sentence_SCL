# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 07:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sentence', '0044_merge_20170105_1728'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sentence',
            options={'ordering': ['-Likes']},
        ),
    ]
