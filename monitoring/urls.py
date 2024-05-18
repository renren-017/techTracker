from django.urls import path

from monitoring.views import EquipmentViewSet, EquipmentTypeListView

urlpatterns = [
    path('equpipments/types/', EquipmentTypeListView.as_view(), name='equpipment-type-list'),
    path('equipments/', EquipmentViewSet.as_view({"get": "list", "post": "create"}), name='equipment-list'),
    path('equipments/<int:pk>', EquipmentViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name='equipment-detail'),
]
