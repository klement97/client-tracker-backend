from django.db import IntegrityError
from rest_framework import serializers

from clients.models import Client


class ClientSerializer(serializers.Serializer):
    number = serializers.IntegerField()
    name = serializers.CharField()

    def create(self, validated_data):
        try:
            return Client.objects.create(**validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                {'number': ['Client with this number already exists.']}
            )

    def update(self, instance, validated_data):
        instance.number = validated_data.get('number', instance.number)
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        return instance
