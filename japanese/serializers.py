from rest_framework import serializers

class NagisaSerializer(serializers.Serializer):
    name = serializers.CharField()

