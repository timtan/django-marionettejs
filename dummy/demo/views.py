from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import serializers

from . import models

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Todo

class TodoViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = TodoSerializer
    queryset = models.Todo.objects.all()
