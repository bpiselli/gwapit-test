from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Fighter(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=255)
    life = models.IntegerField()
    attack = models.IntegerField()
    defence = models.IntegerField()
    class Meta:
        abstract = True

class Cat(Fighter):
    pass

class Zombie(Fighter):
    pass
