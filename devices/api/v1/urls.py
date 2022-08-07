from django.urls import path
from devices.api.v1.views import DeviceView


urlpatterns = [
    path('devices', DeviceView.as_view())
]
