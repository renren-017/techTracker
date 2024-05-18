from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from monitoring.models import Equipment, EquipmentType
from monitoring.serializers import EquipmentSerializer, EquipmentTypeSerializer

__all__ = ['EquipmentTypeListView', 'EquipmentViewSet']


class EquipmentTypeListView(ListAPIView):
    """
    get:
    Return a list of all the existing equipment types.
    """
    queryset = EquipmentType.objects.all()
    serializer_class = EquipmentTypeSerializer
    authentication_classes = [JWTAuthentication]


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    authentication_classes = [JWTAuthentication]
