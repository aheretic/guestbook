# coding: utf-8
from django.contrib.auth import get_user_model

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope

from .serializers import ReviewSerializer, ReplySerializer, UserSerializer
from .models import Review, Reply
from .permissions import IsAuthorOrReadOnly, IsThisUserOrReadOnly


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (TokenHasReadWriteScope, IsAuthorOrReadOnly)


class ReplyViewSet(ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = (TokenHasReadWriteScope, IsAuthorOrReadOnly)


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (TokenHasReadWriteScope, IsThisUserOrReadOnly)

    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = (AllowAny, )

        return super(UserViewSet, self).get_permissions()
