from .models import Cat, Zombie


def poison_burst():
    Cat.objects.update(life=F('life')-15)


def spawn_zombie(dying_zombie):
    dying_zombie.pk = None

    # same object being renamed for comprehension purposes
    # moving pk to None will create a new DB object upon save
    new_zombie = dying_zombie

    new_zombie.name = '{}_{}'.format(
        dying_zombie.name,
        random.randint(1, 1000)
        )
    new_zombie.alive = True
    new_zombie.life = random.randint(50, 100)
    new_zombie.save()
