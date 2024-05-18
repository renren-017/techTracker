from django.contrib import admin
from monitoring.models import Equipment, EquipmentType, Data, Alert, MaintenanceRecord


@admin.register(EquipmentType)
class EquipmentTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial_number', 'equipment_type', 'manufacturer', 'status', 'installed_at', 'last_maintained_at')
    list_filter = ('equipment_type', 'manufacturer', 'status')
    search_fields = ('name', 'serial_number', 'manufacturer')
    date_hierarchy = 'installed_at'
    ordering = ('-installed_at',)


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('equipment', 'name', 'value', 'unit', 'timestamp')
    list_filter = ('equipment', 'name', 'timestamp')
    search_fields = ('name',)
    date_hierarchy = 'timestamp'
    ordering = ('-timestamp',)


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('equipment', 'timestamp', 'severity', 'description')
    list_filter = ('equipment', 'severity', 'timestamp')
    search_fields = ('description',)
    date_hierarchy = 'timestamp'
    ordering = ('-timestamp',)


@admin.register(MaintenanceRecord)
class MaintenanceRecordAdmin(admin.ModelAdmin):
    list_display = ['equipment', 'date_performed', 'technician', 'maintenance_type']
    list_filter = ['equipment', 'maintenance_type', 'date_performed', 'technician']
