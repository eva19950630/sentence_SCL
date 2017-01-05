# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 07:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sentence', '0023_sentence_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('TopicID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Topic_tag', models.TextField(default='unknown')),
                ('Link', models.TextField(default='unknown')),
            ],
        ),
        migrations.RemoveField(
            model_name='sentence',
            name='Link',
        ),
        migrations.RemoveField(
            model_name='sentence',
            name='Topic_tag',
        ),
        migrations.AddField(
            model_name='sentence',
            name='TopicID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sentence.Topic'),
            preserve_default=False,
        ),
    ]