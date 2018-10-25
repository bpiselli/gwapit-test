from __future__ import unicode_literals

from django.db import models

class BaseCharacter(models.Model):

    class Meta:
        abstract=True

    name = models.CharField(max_length=15)
    icon = models.CharField(max_length=140)
    life = models.PositiveSmallIntegerField()
    attack = models.PositiveSmallIntegerField()
    defense = models.PositiveSmallIntegerField()
    alive = models.BooleanField(default=True)

class Cat(BaseCharacter):
    cuteness_level = models.PositiveSmallIntegerField(default=10)

class Zombie(BaseCharacter):
    rot_level = models.PositiveSmallIntegerField(default=10)
