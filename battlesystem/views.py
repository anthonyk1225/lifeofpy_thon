import random

from django.shortcuts import render, redirect
from django.views.generic import View

from battlesystem.models import Battle
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
	template_name = 'battlesystem/battle_summary.html'

	def get(self, request, character_id):
		battles = Battle.objects.filter(character_id=character_id)
		return render(request, self.template_name, {'character': battles[0].character,'battles': battles})

	def post(self, request, character_id):
		winner = Character.objects.get(pk=request.POST['winner'])
		loser = Character.objects.get(pk=request.POST['loser'])
		Battle.objects.create(
			opponent_name=loser.name,
			opponent_race=loser.race,
			was_victorious=True,
			character=winner
		)
		Battle.objects.create(
			opponent_name=winner.name,
			opponent_race=winner.race,
			was_victorious=False,
			character=loser
		)
		return redirect('battlesystem:battle_log', character_id=character_id)