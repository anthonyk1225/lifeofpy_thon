import random
from django.shortcuts import render
from battlesystem.models import Battle
from django.views.generic import View
from characters.models import Character
from users.models import User

# Create your views here.

class BattleStart(View):
	template = 'battlesystem/index.html'

	def get(self, request, character_id):
		toons = Character.objects.filter(pk=character_id,user__key=request.session.get('key',False))
		chosen_toon = toons[0]
		enemy_toon = random.choice(Character.objects.filter(user__isnull=True))
		data = {
			"hero": chosen_toon, 
			"villian": enemy_toon, 
			"herostats":chosen_toon.attribute_set.filter()[0], 
			"villianstats":enemy_toon.attribute_set.filter()[0],
			"heroattack":chosen_toon.attack.filter()[0], 
			"villianattack": enemy_toon.attack.filter()[0]
		}
		return render(request, self.template, data)

class BattleLog(View):
	template_name = 'battlesystem/battle_log.html'

	def get(self, request):
		pass

	def post(self, request):
		pass