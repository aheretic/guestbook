# coding: utf-8
from django.conf.urls import url, include
from rest_framework import routers

from guestbook import views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"reviews", views.ReviewViewSet)
router.register(r"replies", views.ReplyViewSet)
router.register(r"users", views.UserViewSet)


urlpatterns = [
    url(r"^api/", include(router.urls)),
]
