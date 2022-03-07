from rest_framework import serializers

class NagisaSerializer(serializers.Serializer):
    text = serializers.CharField()

