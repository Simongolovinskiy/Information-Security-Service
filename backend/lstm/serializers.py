from rest_framework import serializers

from lstm.models import LSTM_Neural_Model


class LSTMReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = LSTM_Neural_Model
        fields = "__all__"


class LSTMCreateSerializerRead(serializers.ModelSerializer):
    class Meta:
        model = LSTM_Neural_Model
        exclude = ("id",)
