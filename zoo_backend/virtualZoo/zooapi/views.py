from django.shortcuts import render
from rest_framework import generics
from .serializers import ItemSerializer
from .models import Animal

class AnimalList(generics.ListAPIView):
    queryset = Animal.objects.all()
    serializer_class = ItemSerializer


class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = ItemSerializer

class AnimalCreate(generics.CreateAPIView):
    queryset = Animal.objects.all() 
    serializer_class = ItemSerializer