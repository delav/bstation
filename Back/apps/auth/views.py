# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from .models import User
from .serializers import RegisterSerializers, LoginSerializers
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework_jwt.settings import api_settings
from django.shortcuts import render

# Create your views here.


class RegisterViewSets(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers

    def create(self, request, *args, **kwargs):
        raw_data = self.request.data
        print('raw_data', raw_data)
        code = raw_data['code']
        session_code = request.session.get('code')
        print('session code', session_code)
        if code == '':
            return Response({'result': False, 'details': '验证码为空'})
        if session_code is None:
            return Response({'result': False, 'details': '验证码已过期'})
        else:
            if str(session_code).upper() != str(code).upper():
                return Response({'result': False, 'details': '验证码错误'})
        # return Response(raw_data)
        serializer = RegisterSerializers(data=raw_data)
        if serializer.is_valid(raise_exception=False):
            data = serializer.data
            print('data', data)
            username = data['username']
            password = data['password']
            user = User.objects.filter(username=username)
            if user.count() < 1:
                data['password'] = make_password(password)
                del data['code']
                user.create(**data)
                return Response({'result': True, 'details': '注册成功'})
            else:
                return Response({'result': False, 'details': '该用户已注册'})
        else:
            return Response({'result': False, 'details': serializer.errors})


class LoginViewSets(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializers

    def create(self, request, *args, **kwargs):
        data = self.request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.is_active:
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            request.session.clear_expired()
            data['token'] = token
            data['details'] = '登录成功'
            return Response(data)
        return Response({'result': False, 'details': '用户名或密码错误！'})
