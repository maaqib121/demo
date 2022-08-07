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


class DeviceDetailView(APIView):
    def patch(self, request, device_id):
        index, device = next(
            ((index, device) for (index, device) in enumerate(settings.DEVICES) if device['id'] == device_id),
            (False, False)
        )
        if not device:
            return Response(
                {'errors': {'non_field_errors': 'Device object not found.'}},
                 status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

        serializer = DeviceSerializer(device, request.data, partial=True)
        if serializer.is_valid():
            connect_status = serializer.validated_data.get('connect_status', device['connect_status'])
            settings.DEVICES[index]['connect_status'] = connect_status
            return Response(settings.DEVICES[index], status=status.HTTP_200_OK)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
