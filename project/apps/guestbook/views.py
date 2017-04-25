# coding: utf-8
from django.views.generic import ListView
from django.db.models import Prefetch

from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .serializers import ReviewSerializer, ReplySerializer, UserSerializer
from .models import Review, Reply, CustomUser as User
from .permissions import IsAuthorOrReadOnly, IsSuperuserOrReadOnly


class ReviewListView(ListView):
    queryset = Review.objects.prefetch_related(Prefetch("reply_set"))
    paginate_by = 10


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)


class ReplyViewSet(ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsSuperuserOrReadOnly)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsSuperuserOrReadOnly)
