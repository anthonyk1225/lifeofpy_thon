from characters.models import EnemyAttribute, Enemy
from attacks.models import Attack
import random

def create_enemies():
    name = ['Simple Peon', 'Thrall', 'Lich King', 'Ganon']
    race = ['orge', 'humanoid', 'demon', 'hybrid']
    for i in range(5):
        attacks = Attack.objects.all()
        attack = [random.choice(attacks)]
        new_enemy = Enemy.objects.create(name=random.choice(name), race=random.choice(race))
        new_enemy.attack = attack
        new_enemy.save()
        EnemyAttribute.objects.create(hit_points=random.randint(20,40), power=random.randint(2,7), character=new_enemy)
