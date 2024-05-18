from django.urls import path

from monitoring.views import EquipmentViewSet, EquipmentTypeListView, AlertViewSet

urlpatterns = [
    path('equpipments/types/', EquipmentTypeListView.as_view(), name='equpipment-type-list'),
    path('equipments/', EquipmentViewSet.as_view({"get": "list", "post": "create"}), name='equipment-list'),
    path('equipments/<int:pk>', EquipmentViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name='equipment-detail'),

    path('alerts/', AlertViewSet.as_view({"get": "list", "post": "create"}), name='alerts-list'),
    path('alerts/<int:pk>', AlertViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name='alerts-detail'),
]
