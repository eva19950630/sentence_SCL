# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-21 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentence', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='SocialID',
            field=models.BigIntegerField(default=-1, null=True),
        ),
    ]
