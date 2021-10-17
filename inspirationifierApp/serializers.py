from.models import Image
from rest_framework import serializers


class ImageSerializer(serializers.Serializer):
    quotes = serializers.CharField(required=False, allow_blank=True, max_length=100)
    imageUrl = serializers.CharField(max_length=100000)
    
    def create(self, validated_data):
        return Image.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.quotes = validated_data.get('quotes', instance.quotes)
        instance.imageUrl = validated_data.get('imageUrl', instance.imageUrl)
        instance.save()
        return instance