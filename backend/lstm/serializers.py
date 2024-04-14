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


class LSTMEmailSerializer(serializers.Serializer):
    emails = serializers.ListSerializer(child=serializers.EmailField())
    lstm_data = LSTMCreateSerializerRead()

    class Meta:
        fields = ("emails", "lstm_data")
