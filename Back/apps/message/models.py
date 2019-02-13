# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from apps.auth.models import User
from django.db import models
from datetime import datetime
import uuid


# Create your models here.
class Message(models.Model):
    id = models.UUIDField(auto_created=True, default=uuid.uuid1, primary_key=True)
    name = models.ForeignKey(User, to_field='username', verbose_name='用户名')
    words = models.TextField(verbose_name='留言内容', blank=False)
    public_time = models.DateTimeField(default=datetime.now, verbose_name='留言时间')

    class Meta:
        verbose_name = '用户留言表'
        verbose_name_plural = verbose_name
        ordering = ['public_time']
