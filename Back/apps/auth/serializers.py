# coding: utf-8
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings
from datetime import datetime
from django.db import models
from .models import User


class RegisterSerializers(serializers. ModelSerializer):
    # mobile = serializers.CharField()
    # code = serializers.CharField(max_length=4, help_text='验证码')
    date_joined = serializers.DateTimeField(default=datetime.now(), help_text='注册时间', read_only=True)
    password = serializers.CharField(min_length=6, max_length=100, trim_whitespace=False, allow_blank=False,
                                     help_text='密码')
    confirm_password = serializers.CharField(min_length=6, max_length=100, trim_whitespace=False, allow_blank=False,
                                             help_text='确认密码', write_only=True)
    email = serializers.EmailField(help_text='邮箱', allow_blank=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password', 'is_staff', 'is_active', 'date_joined',
                  'email')
        extra_kwargs = {
            'username': {
                'min_length': 5,
                'max_length': 30,
                'error_messages': {
                    'min_length': 'username only allows 5-30 characters',
                    'max_length': 'username only allows 5-30 characters',
                }
            },
            'password': {
                'write_only': True,
                'min_length': 6,
                'max_length': 16,
                'error_messages': {
                    'min_length': 'password only allows 6-16 characters',
                    'max_length': 'password only allows 6-16 characters',
                }
            }
        }

    def validate(self, attrs):
        del attrs['confirm_password']
        return attrs

    # def validate_code(self, value):
    #     # 获取请求中的验证码
    #     correct_verify_code = self.context['request'].session['code']
    #     verify_code = self.context['request'].data.get('code')
    #     if not verify_code:
    #         raise serializers.ValidationError("验证码为空")
    #     # 验证验证码
    #     if verify_code != correct_verify_code:
    #         raise serializers.ValidationError("验证码错误")
    # def create(self, validated_data):
    #     username = validated_data['username']
    #     password = validated_data['password']
    #     user = User.objects.filter(username=username)
    #     if user.count() < 1:
    #         validated_data['password'] = make_password(password)
    #         return User.objects.create(**validated_data)
    #     else:
    #         raise serializers.ValidationError('该用户已注册！')


class LoginSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')
