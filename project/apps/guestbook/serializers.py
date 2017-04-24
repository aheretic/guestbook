# coding: utf-8
from rest_framework import serializers

from .models import Review, Reply, CustomUser as User


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ("id", "text", "author", "created_at")


class ReplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Reply
        fields = ("id", "text", "author", "review", "created_at")


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "created_at")