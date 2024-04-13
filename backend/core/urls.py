from django.contrib import admin
from django.urls import path, include

from .spectacular import urlpatterns as spectacular_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("lstm.urls", namespace="lstm")),
] + spectacular_urls
