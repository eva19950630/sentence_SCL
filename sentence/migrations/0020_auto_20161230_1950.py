# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-30 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentence', '0019_auto_20161230_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='UID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
