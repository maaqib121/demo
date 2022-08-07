from rest_framework import serializers


class DeviceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    connect_status = serializers.BooleanField()
