# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentence', '0031_auto_20170103_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='UserIcon',
            field=models.ImageField(default='/static/images/fish.png', upload_to='UserIcon_folder'),
        ),
    ]