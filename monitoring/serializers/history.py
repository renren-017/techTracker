from rest_framework import serializers
from monitoring.models import MaintenanceRecord

__all__ = ['MaintenanceRecordSerializer']


class MaintenanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRecord
        fields = '__all__'
