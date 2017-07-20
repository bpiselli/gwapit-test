from rest_framework import serializers
from gwapit.quickstart.models import Cat, Zombie

class ZombieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zombie
        fields = "__all__"

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = "__all__"
