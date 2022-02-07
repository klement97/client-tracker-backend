from rest_framework import serializers

from clients.models import Client


class ClientSerializer(serializers.Serializer):
    number = serializers.IntegerField()
    name = serializers.CharField()

    def create(self, validated_data):
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.number = validated_data.get('number', instance.number)
        instance.name = validated_data.get('name', instance.name)
