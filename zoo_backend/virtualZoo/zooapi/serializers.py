from rest_framework import serializers
from .models import Animal


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'
        