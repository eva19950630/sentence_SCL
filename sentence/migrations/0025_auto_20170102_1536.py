# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 07:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sentence', '0024_auto_20170102_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentence',
            name='TopicID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sentence.Topic'),
        ),
    ]
