# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from apps.author.models import Author
import uuid
# Create your models here.


class Video(models.Model):
    # define the fields for your item here like:
    id = models.CharField(max_length=50, primary_key=True, blank=False, unique=True, verbose_name='视频ID')
    url = models.CharField(max_length=100, default='', verbose_name='视频地址')
    title = models.CharField(max_length=300, default='', verbose_name='视频标题')
    types = models.CharField(max_length=100, default='动漫', verbose_name='视频类型')
    public_time = models.DateTimeField(verbose_name='发布时间', default=datetime.now())
    author_name = models.CharField(max_length=300, default='未知', verbose_name='作者昵称')
    author_url = models.CharField(max_length=100, default='', verbose_name='作者主页')
    views = models.IntegerField(default=0, verbose_name='播放数量')
    danmaku = models.IntegerField(default=0, verbose_name='弹幕数量')
    reply = models.IntegerField(default=0, verbose_name='评论数量')
    favorite = models.IntegerField(default=0, verbose_name='收藏数量')
    coin = models.IntegerField(default=0, verbose_name='硬币数量')
    share = models.IntegerField(default=0, verbose_name='分享数量')
    likes = models.IntegerField(default=0, verbose_name='点赞数量')

    class Meta:
        verbose_name = '视频信息表'
        verbose_name_plural = verbose_name
        ordering = ['public_time']
