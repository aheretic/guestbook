# coding: utf-8
from django.conf.urls import url
from django.contrib.auth.views import login, logout

from .views import ReviewListView

urlpatterns = [
    # url(r"^login/$", login, {"template_name": "login.html", "redirect_authenticated_user": True}, name="login"),
    # url(r"^logout/$", logout, name="logout"),
    url(r"^$", ReviewListView.as_view(), name="review_list"),
]
