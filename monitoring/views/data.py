from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import viewsets, filters

from monitoring.models import Data
from monitoring.serializers import DataSerializer

__all__ = ['DataViewSet']


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['equipment', 'timestamp']
    ordering_fields = ['timestamp']
