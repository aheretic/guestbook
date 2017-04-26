# coding: utf-8
from rest_framework import serializers

from .models import Review, Reply


class BaseSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S %Z", read_only=True)

    class Meta:
        abstract = True


class ReplySerializer(BaseSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Reply
        fields = ("id", "text", "author", "review", "created_at")


class ReviewSerializer(BaseSerializer):
    # reply_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    reply_set = ReplySerializer(many=True, read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = ("id", "text", "author", "reply_set", "created_at")
