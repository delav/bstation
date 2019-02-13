# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import mixins
from rest_framework import generics
from django.shortcuts import render
from .models import Author
from .serializers import AuthorSerializers


# Create your views here.


class AuthorViewSets(generics.ListCreateAPIView):
    """
    get:
        return all instance
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
