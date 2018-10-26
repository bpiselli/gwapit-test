from .models import Cat, Zombie

def attack_strongest(queryset):
    attacker_queryset = queryset
    if queryset.Model is Zombie:
        defender_queryset = Cat.objects
    else:
        defender_queryset = Zombie.objects

    defenders_states = {}

    for attacker in attacker_queryset:
        target = defender_queryset.objects.order_by('-attack').first()
        damages = attacker.attack - target.defense
        if damages < target.life():
            target.life -= damages
        else:
            target.life = 0
        target.save()
        defenders_states[target.name] = target.life
    return defenders_states