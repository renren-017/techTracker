from rest_framework import serializers
from monitoring.models import Equipment, EquipmentType, Data

__all__ = ['EquipmentTypeSerializer', 'EquipmentSerializer']


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'


class EquipmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentType
        fields = '__all__'


class EquipmentSerializer(serializers.ModelSerializer):
    parameters = DataSerializer(many=True, read_only=True)

    class Meta:
        model = Equipment
        fields = '__all__'
