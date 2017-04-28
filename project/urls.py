# coding: utf-8
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^", include("guestbook.urls", namespace="guestbook"), ),
    # url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    url(r"^oauth2/", include("oauth2_provider.urls", namespace="oauth2_provider")),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r"^__debug__/", include(debug_toolbar.urls)),
    ]
