import smtplib
from email.header import Header
from email.mime.text import MIMEText
from http import HTTPStatus

from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from core.settings import EMAIL_LOGIN, SMTP_HOST, SMTP_PORT, EMAIL_PASSWORD
from .models import LSTM_Neural_Model
from .serializers import LSTMReadSerializer, LSTMCreateSerializerRead, LSTMEmailSerializer


class LSTMViewSet(viewsets.ModelViewSet):
    queryset = LSTM_Neural_Model.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return LSTMReadSerializer
        return LSTMCreateSerializerRead

class LSTMEmailSend(mixins.CreateModelMixin,
                    GenericViewSet):
    queryset = LSTM_Neural_Model.objects.all()
    serializer_class = LSTMEmailSerializer

    def create(self, request, *args, **kwargs):
        serializer = LSTMEmailSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        emails = serializer.data.get("emails")
        message = serializer.data.get("lstm_data")

        msg = MIMEText(f'{message}', _subtype='utf-8')
        msg['Subject'] = Header('Важно!!!', 'utf-8')
        msg['From'] = EMAIL_LOGIN
        msg['To'] = ', '.join(emails)

        s = smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=10)

        try:
            s.starttls()
            s.login(EMAIL_LOGIN, EMAIL_PASSWORD)
            s.sendmail(msg['From'], emails, msg.as_string())
        except Exception as ex:
            print(ex)
            return Response(data={"message": "Cant connect to SMTP"}, status=HTTPStatus.BAD_GATEWAY)
        finally:
            s.quit()
        return Response(data={"message": "Message successfully sent"})
