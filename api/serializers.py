from re import U
from django.db import models
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post

class PostSerializer(ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "body",
            "owner",
        ]


class UserSerializer(ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "posts",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user



