# coding: utf-8
from django.views.generic import ListView
from django.db.models import Prefetch

from rest_framework.viewsets import ModelViewSet
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope

from .serializers import ReviewSerializer, ReplySerializer
from .models import Review, Reply
from .permissions import IsAuthorOrReadOnly


class ReviewListView(ListView):
    queryset = Review.objects.prefetch_related(Prefetch("reply_set"))
    paginate_by = 10


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (TokenHasReadWriteScope, IsAuthorOrReadOnly)


class ReplyViewSet(ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = (TokenHasReadWriteScope, IsAuthorOrReadOnly)
