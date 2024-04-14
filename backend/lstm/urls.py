from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LSTMViewSet, LSTMEmailSend

app_name = "lstm"


router = DefaultRouter()
router.register("lstm", LSTMViewSet, basename="lstm")
router.register("send-email", LSTMEmailSend, basename="send-email")


urlpatterns = [
    path("", include(router.urls))
]
