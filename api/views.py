from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import serializers
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import UserSerializer, PostSerializer
from .models import Post


class Home(TemplateView):
    template_name = "home.html"


class UserRegister(CreateAPIView):
    serializer_class = UserSerializer


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreate(CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def perform_create(self, serializer):
        if self.request.user:
            serializer.save(owner=self.request.user)


class PostDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [
        IsAdminUser,
        IsAuthenticated,
    ]
