# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 08:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sentence', '0037_auto_20170105_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='UserIcon',
        ),
    ]
