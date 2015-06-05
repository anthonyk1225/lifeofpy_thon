from attacks.models import Attack

def create_attacks():
	attacks = {"Swing":"Physical", "Ice Blast":"Frost", "Sword of Righteousness":"Holy"}
	for attack in attacks:
		Attack.objects.create(name=attack, element=attacks[attack])