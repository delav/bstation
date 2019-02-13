# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import mixins
from rest_framework import generics
from django.shortcuts import render
from .models import Video
from .serializers import VideoSerializers

# Create your views here.


class VideoViewSets(generics.ListCreateAPIView):
    """
    get:
        return all instance
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializers
