# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from .models import Message
from .serializers import MessageSerializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


# Create your views here.
class MessageViewSets(generics.DestroyAPIView, generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializers
    authentication_classes = (BasicAuthentication,)
    # permission_classes = (IsAuthenticated,)
