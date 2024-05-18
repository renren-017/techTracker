
from django_filters import rest_framework as filters
from monitoring.models import Equipment, EquipmentType


class EquipmentFilter(filters.FilterSet):
    manufacturer = filters.CharFilter(lookup_expr='icontains')
    status = filters.ChoiceFilter(choices=Equipment.STATUS_CHOICES)
    equipment_type = filters.ModelChoiceFilter(
        queryset=EquipmentType.objects.all(),
        field_name='equipment_type__name',
        to_field_name='name',
        label='Equipment Type'
    )

    class Meta:
        model = Equipment
        fields = ['equipment_type', 'manufacturer', 'status']
