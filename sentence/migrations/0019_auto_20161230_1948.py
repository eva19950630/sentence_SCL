# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-30 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentence', '0018_auto_20161230_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='UID',
            field=models.AutoField(default=1, primary_key=True, serialize=False, unique=True),
        ),
    ]
