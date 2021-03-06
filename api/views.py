from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import serializers
from rest_framework.generics import (
    ListCreateAPIView,
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    CommentSerializer,
    UserSerializer,
    PostSerializer,
    CatgorySerializer,
)
from .models import Post, Comment, Category


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


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def perform_create(self, serializer):
        if self.request.user:
            serializer.save(owner=self.request.user)


class PostDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]


class CommentList(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class CategoryList(ListCreateAPIView):
    serializer_class = CatgorySerializer
    queryset = Category.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = CatgorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
