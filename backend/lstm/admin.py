from django.contrib import admin

from .models import LSTM_Neural_Model


@admin.register(LSTM_Neural_Model)
class LSTM_Neural_ModelAdmin(admin.ModelAdmin):
    pass
