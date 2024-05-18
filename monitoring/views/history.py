from rest_framework import viewsets
from monitoring.models import MaintenanceRecord
from monitoring.serializers import MaintenanceRecordSerializer


__all__ = ['MaintenanceRecordViewSet']


class MaintenanceRecordViewSet(viewsets.ModelViewSet):
    serializer_class = MaintenanceRecordSerializer
    queryset = MaintenanceRecord.objects.all().order_by('-id')

    def get_queryset(self):
        equipment_id = self.request.query_params.get('equipment_id')
        if equipment_id is not None:
            return self.queryset.filter(equipment__id=equipment_id).order_by('-id')
        return self.queryset
