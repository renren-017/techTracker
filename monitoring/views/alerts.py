from rest_framework import viewsets

from monitoring.models import Alert
from monitoring.serializers import AlertSerializer

__all__ = ['AlertViewSet']


class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
