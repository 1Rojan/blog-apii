from re import U
from django.db import models
from django.db.models import fields
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Comment, Post


class PostSerializer(ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "body",
            "owner",
            "comments",
        ]


class UserSerializer(ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "posts",
            "comments",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class CommentSerializer(ModelSerializer):
    post = serializers.ReadOnlyField(source="post.title")

    class Meta:
        model = Comment
        fields = [
            "id",
            "body",
            "post",
        ]


    

