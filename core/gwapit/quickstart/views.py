from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from .fights import attack_strongest
from .models import Cat, Zombie
from .serializers import CatSerializer, ZombieSerializer


class FighterViewSetMixin(object):

    @list_route(methods=['post'])
    def test(self, request):
        method = self.fight_method
        method()
        return Response({'done': 'done'})


class CatViewSet(FighterViewSetMixin, viewsets.ModelViewSet):
    serializer_class = CatSerializer
    queryset = Cat.objects.all()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fight_method = cat_fight

    @detail_route(methods=['post'])
    def regen(self, request, pk):
        cat = get_object_or_404(Cat, pk=pk)
        cat.life += 35
        cat.save()
        return Response({'pk': cat.pk, 'life': cat.life})


class ZombieViewSet(FighterViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ZombieSerializer
    queryset = Zombie.objects.all()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fight_method = zombie_fight
