from django.shortcuts import render, redirect
from django.views.generic import View
from characters.models import Character, Attribute
from users.models import User

# Create your views here.
def create_warrior(request):
	current_user = User.objects.filter(id=request.session['user_id'])
	new_char = Character.objects.create(race='warrior', name=request.POST['name'], user=current_user[0])
	Attribute.objects.create(hit_points=40,attack=5,character=new_char)
	return redirect('/rpg/welcome')

def create_mage(request):
	current_user = User.objects.filter(id=request.session['user_id'])
	new_char = Character.objects.create(race='mage', name=request.POST['name'], user=current_user[0])
	Attribute.objects.create(hit_points=22,attack=8,character=new_char)
	return redirect('rpg/welcome')

def create_paladin(request):
	current_user = User.objects.filter(id=request.session['user_id'])
	new_char = Character.objects.create(race='paladin', name=request.POST['name'], user=current_user[0])
	Attribute.objects.create(hit_points=54,attack=3,character=new_char)
	return redirect('rpg/welcome')

class HeroView(View):
	template_name = 'characters/hero.html'

	def get(self,request,name):
		character = Character.objects.get(name=name)
		character_attributes = Attribute.objects.filter(character_id=character.id)
		attributes = [attribute for attribute in character_attributes]
		# return render(request, self.template, {'username': user.username, 'characters':characters})
		return render(request, self.template_name, {'character':character, 'attributes':attributes})
