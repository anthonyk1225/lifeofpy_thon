from characters.models import Character, Attribute
from attacks.models import Attack
import random

def create_enemies():
	name = ['Simple Peon', 'Thrall', 'Lich King', 'Ganon']
	race = ['orge', 'humanoid', 'demon', 'hybrid']
	attacks = Attack.objects.all()
	for i in range(5):
		new_enemy = Enemy.objects.create(name=random.choice.name, race=random.choice.race, attack=random.choice.attacks)
		Attribute.objects.create(hit_points=randint(20,40), attack=randint(2,7), character=new_enemy)

