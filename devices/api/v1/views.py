from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.conf import settings
from devices.api.v1.serializers import DeviceSerializer


class DeviceView(APIView):
    http_method_names = ('get',)
    serializer_class = DeviceSerializer

    def get(self, request):
        serializer = self.serializer_class(settings.DEVICES, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
