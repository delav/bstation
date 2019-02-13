# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-02-01 02:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, default=uuid.uuid1, primary_key=True, serialize=False, unique=True, verbose_name='\u4f5c\u8005ID')),
                ('a_url', models.CharField(blank=True, default='', max_length=100, verbose_name='\u4f5c\u8005\u4e3b\u9875')),
                ('up_name', models.CharField(default='\u672a\u77e5', max_length=300, verbose_name='\u4f5c\u8005\u6635\u79f0')),
                ('sex', models.CharField(default='\u7537', max_length=100, verbose_name='\u6027\u522b')),
                ('register_time', models.DateTimeField(default=datetime.datetime(2019, 2, 1, 10, 53, 34, 447000), verbose_name='\u6ce8\u518c\u65f6\u95f4')),
                ('following', models.IntegerField(default=0, verbose_name='\u7c89\u4e1d\u6570\u91cf')),
                ('follower', models.IntegerField(default=0, verbose_name='\u5173\u6ce8\u6570\u91cf')),
                ('videos', models.IntegerField(default=0, verbose_name='\u6295\u7a3f\u6570\u91cf')),
                ('album', models.IntegerField(default=0, verbose_name='\u76f8\u7c3f\u6570\u91cf')),
                ('views', models.IntegerField(default=0, verbose_name='\u603b\u64ad\u653e\u6570')),
            ],
            options={
                'ordering': ['register_time'],
                'verbose_name': '\u4f5c\u8005\u4fe1\u606f\u8868',
                'verbose_name_plural': '\u4f5c\u8005\u4fe1\u606f\u8868',
            },
        ),
    ]
