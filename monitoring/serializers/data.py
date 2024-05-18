from rest_framework import serializers
from monitoring.models import Data

__all__ = ['DataSerializer']


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'
