from rest_framework import serializers
from monitoring.models import Alert

__all__ = ['AlertSerializer']


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'
