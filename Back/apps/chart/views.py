# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Chart
from rest_framework import generics
from .serializers import ChartSerializers
from django.shortcuts import render


# Create your views here.
class ChartViewSets(generics.RetrieveAPIView, generics.ListAPIView):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializers
