# -*- coding: utf-8 -*-
from .models import Chart
from rest_framework import serializers


class ChartSerializers(serializers.ModelSerializer):

    class Meta:
        model = Chart
        fields = ['img_path', 'img_name']

