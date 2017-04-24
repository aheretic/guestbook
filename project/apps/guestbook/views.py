# coding: utf-8
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Prefetch

from rest_framework import viewsets
from rest_framework import permissions

from .serializers import ReviewSerializer, ReplySerializer
from .models import Review, Reply, CustomUser as User
from .permissions import IsOwnerOrReadOnly


class ReviewListView(ListView):
    queryset = Review.objects.prefetch_related(Prefetch("reply_set"))
    paginate_by = 10


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.exclude(is_superuser=True)
    serializer_class = ReplySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )