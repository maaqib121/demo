from django.urls import path
from devices.api.v1.views import DeviceView, DeviceDetailView


urlpatterns = [
    path('devices', DeviceView.as_view()),
    path('devices/<int:device_id>', DeviceDetailView.as_view())
]
