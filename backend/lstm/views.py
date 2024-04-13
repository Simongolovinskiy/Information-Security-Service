from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS

from .models import LSTM_Neural_Model
from .serializers import LSTMReadSerializer, LSTMCreateSerializerRead


class LSTMViewSet(viewsets.ModelViewSet):
    queryset = LSTM_Neural_Model.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return LSTMReadSerializer
        return LSTMCreateSerializerRead
