from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializers import *

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.clock.models import clock
from apps.clock.serializers import clockSerializer

class clockApi(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.DestroyModelMixin):
    queryset = clock.objects.all()
    serializer_class = clockSerializer