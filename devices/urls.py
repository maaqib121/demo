from django.urls import path, include


urlpatterns = [
    path('api/', include('devices.api.urls'))
]
