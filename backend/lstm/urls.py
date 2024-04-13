from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LSTMViewSet

app_name = "lstm"


router = DefaultRouter()
router.register("lstm", LSTMViewSet, basename="lstm")


urlpatterns = [
    path("", include(router.urls))
]
