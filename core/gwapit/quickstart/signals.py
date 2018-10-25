import random

from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Zombie, Cat
from .zombie_actions import poison_burst, spawn_zombie


@receiver(post_save, sender=Zombie)
def kill_zombie(sender, instance, **kwargs):
    if instance.alive is True and instance.life <= 0:
        instance.alive = False
        instance.save()

        poison_burst()
        spawn_zombie(instance)


@receiver(post_save, sender=Cat)
def kill_cat(sender, instance, **kwargs):
    if instance.alive is True and instance.life <= 0:
        instance.alive = False
        instance.save()