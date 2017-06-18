# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-17 16:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sentence', '0003_auto_20170617_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.TextField()),
                ('Date', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('RoomUID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Room_owner', to='sentence.User')),
                ('VisiterUID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Visiter', to='sentence.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='messege',
            name='Room',
        ),
        migrations.DeleteModel(
            name='Messege',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
