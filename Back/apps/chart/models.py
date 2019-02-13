# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.db import models


# Create your models here.
class Chart(models.Model):
    id = models.UUIDField(auto_created=True, default=uuid.uuid1, primary_key=True)
    img_path = models.FilePathField(verbose_name='图表路径')
    img_name = models.CharField(max_length=30, verbose_name='图表名称')
