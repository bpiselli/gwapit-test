from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import authentication, permissions
from gwapit.quickstart.models import Cat, Zombie
from gwapit.quickstart.serializers import CatSerializer, ZombieSerializer
# Create your views here.


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

class ZombieViewSet(viewsets.ModelViewSet):
    queryset = Zombie.objects.all()
    serializer_class = ZombieSerializer
