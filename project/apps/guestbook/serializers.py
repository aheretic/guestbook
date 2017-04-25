# coding: utf-8
from rest_framework import serializers

from .models import Review, Reply, CustomUser as User


class ReviewSerializer(serializers.ModelSerializer):
    reply_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Reply.objects.all())
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S %Z")

    class Meta:
        model = Review
        fields = ("id", "text", "author", "reply_set", "created_at")


class ReplySerializer(serializers.ModelSerializer):
    # review = serializers.HyperlinkedIdentityField(view_name="review-detail")
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S %Z")

    class Meta:
        model = Reply
        fields = ("id", "text", "author", "review", "created_at")


class UserSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S %Z")
    review_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Review.objects.all())
    reply_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Reply.objects.all())

    class Meta:
        model = User
        fields = ("id", "username", "created_at", "review_set", "reply_set")
