# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-17 09:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sentence', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('Achievement_ID', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('UID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sentence.User')),
            ],
        ),
    ]
