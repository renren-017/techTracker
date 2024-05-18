from django.db import models

from users.models import User


class EquipmentType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    IN_USE = 'IN_USE'
    DISABLED = 'DISABLED'
    IN_REPAIR = 'IN_REPAIR'

    STATUS_CHOICES = (
        (IN_USE, 'In Use'),
        (DISABLED, 'Disabled'),
        (IN_REPAIR, 'In Repair')
    )

    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)

    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=100)

    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    installed_at = models.DateTimeField(auto_now_add=True)
    last_maintained_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['equipment_type']),
            models.Index(fields=['installed_at']),
            models.Index(fields=['status']),
            models.Index(fields=['serial_number']),
            models.Index(fields=['last_maintained_at']),
        ]

    def __str__(self):
        return f"{self.equipment_type} - {self.name} ({self.serial_number})"


class Data(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='parameters')
    name = models.CharField(max_length=50)
    value = models.FloatField()
    unit = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['equipment', 'timestamp']),
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return f"{self.name} for {self.equipment} at {self.timestamp}: {self.value} {self.unit}"


class Alert(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='alerts')
    timestamp = models.DateTimeField(auto_now_add=True)
    severity = models.CharField(max_length=50, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    description = models.TextField()

    class Meta:
        indexes = [
            models.Index(fields=['equipment', 'timestamp']),
            models.Index(fields=['severity']),
        ]

    def __str__(self):
        return f"Alert for {self.equipment} ({self.severity}) at {self.timestamp}: {self.description}"


class MaintenanceRecord(models.Model):
    INSPECTION = 'INSPECTION'
    REPAIR = 'REPAIR'
    MINOR_SYSTEM_UPDATE = 'MINOR_SYSTEM_UPDATE'
    MAJOR_SYSTEM_UPDATE = 'MAJOR_SYSTEM_UPDATE'

    MAINTENANCE_CHOICES = (
        (INSPECTION, 'Inspection'),
        (REPAIR, 'Repair'),
        (MINOR_SYSTEM_UPDATE, 'Minor System Update'),
        (MAJOR_SYSTEM_UPDATE, 'Major System Update')
    )

    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='maintenance_records')
    date_performed = models.DateTimeField()
    technician = models.ForeignKey(User, on_delete=models.CASCADE, related_name='maintenance_records')
    maintenance_type = models.CharField(max_length=100, choices=MAINTENANCE_CHOICES)
    notes = models.TextField()

    def __str__(self):
        return f"Maintenance {self.maintenance_type} on {self.date_performed.strftime('%Y-%m-%d')}"
