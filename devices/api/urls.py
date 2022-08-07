from django.urls import path, include


urlpatterns = [
    path('v1/', include('devices.api.v1.urls'))
]
