from django.shortcuts import render
from battlesystem.models import Battle
from django.views.generic import View
from characters.models import Character, Enemy
from users.models import User
import random

# Create your views here.

class BattleStart(View):
	template = 'battlesystem/index.html'

	def get(self,request):
		current_user = User.objects.filter(id= request.session['user_id'])
		toons = Character.objects.filter(user=current_user[0])
		chosen_toon = random.choice(toons)
		enemy_toon = random.choice(Enemy.objects.all())
		return render(request, self.template, {"hero": chosen_toon, "villian": enemy_toon, 
		"herostats":chosen_toon.heroattribute_set.filter()[0], "villianstats":enemy_toon.enemyattribute_set.filter()[0],
		"heroattack":chosen_toon.attack.filter()[0], "villianattack": enemy_toon.attack.filter()[0]})

