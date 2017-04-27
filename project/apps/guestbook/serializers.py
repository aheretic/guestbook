# coding: utf-8
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Review, Reply


class BaseSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S %Z", read_only=True)

    class Meta:
        abstract = True
        read_only_fields = ("id", )


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


class UserSerializer(BaseSerializer):

    class Meta:
        model = get_user_model()
        fields = ("id", "username", "password", "email", "created_at")
        write_only_fields = ("password", )

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        if "password" in validated_data:
            instance.set_password(validated_data.pop("password"))

        return super(UserSerializer, self).update(instance, validated_data)
