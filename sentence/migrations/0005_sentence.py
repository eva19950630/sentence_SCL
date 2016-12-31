# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-26 02:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sentence', '0004_auto_20161225_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('SID', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('Date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Content', models.TextField()),
                ('Sentence_tag', models.TextField()),
                ('Topic_tag', models.TextField()),
                ('UID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sentence.User')),
            ],
        ),
    ]