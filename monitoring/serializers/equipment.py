from rest_framework import serializers
from monitoring.models import Equipment, EquipmentType

__all__ = ['EquipmentTypeSerializer', 'EquipmentSerializer']


class EquipmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentType
        fields = '__all__'


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'
