# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Message
from apps.auth.models import User


class MessageSerializers(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('name', 'words', 'public_time')

    # def validate(self, attrs):
    #     user = attrs['name']
    #     if not user:
    #         raise serializers.ValidationError('用户未登录')
    #     return attrs

