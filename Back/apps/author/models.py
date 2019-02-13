# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
import uuid
# Create your models here.


class Author(models.Model):

    id = models.BigIntegerField(auto_created=True, primary_key=True, default=uuid.uuid1, blank=False,
                                unique=True, verbose_name='作者ID')
    a_url = models.CharField(max_length=100, default='', blank=True, verbose_name='作者主页')
    up_name = models.CharField(max_length=300, default='未知', verbose_name='作者昵称')
    sex = models.CharField(max_length=100, default='男', verbose_name='性别')
    register_time = models.DateTimeField(verbose_name='注册时间', default=datetime.now())
    following = models.IntegerField(default=0, verbose_name='粉丝数量')
    follower = models.IntegerField(default=0, verbose_name='关注数量')
    videos = models.IntegerField(default=0, verbose_name='投稿数量')
    album = models.IntegerField(default=0, verbose_name='相簿数量')
    views = models.IntegerField(default=0, verbose_name='总播放数')

    class Meta:
        verbose_name = '作者信息表'
        verbose_name_plural = verbose_name
        ordering = ['register_time']
