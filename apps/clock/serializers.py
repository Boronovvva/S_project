from rest_framework import serializers

from .models import *


class clockSerializer(serializers.ModelSerializer):
    class Meta:
        model = clock
        fields = ['id', 'title', 'description', 'image']


class clockDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = clock
        fields = ['id', 'title', 'description', 'image']