from django.shortcuts import render
from battlesystem.models import Battle
from django.views.generic import View
from characters.models import Character
from users.models import User

# Create your views here.

class BattleStart(View):
	template = 'battlesystem/index.html'

	def get(self,request):
		current_player = User.objects.filter(id= request.session['user_id'])
		players_characters = Character.objects.filter(user=current_player[0])
		return render(request, self.template, {"characters":[character.name for character in players_characters]})

