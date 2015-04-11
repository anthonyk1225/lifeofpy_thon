from django.shortcuts import render, redirect
from django.views.generic import View
from characters.models import Character, Attribute
from users.models import User

# Create your views here.
def create_warrior(request):
	current_user = User.objects.filter(id=request.session['user_id'])
	new_char = Character(race='warrior', name=request.POST['name'], user=current_user[0])
	return redirect('/rpg/')

def create_mage(request):
	current_user = User.objects.filter(id=request.session['user_id'])
	new_char = Character(race='mage', name=request.POST['name'], user=current_user[0])
	return redirect('rpg')

def create_paladin(request):
	current_user = User.objects.filter(id=request.session['user_id'])
	new_char = Character(race='paladin', name=request.POST['name'], user=current_user[0])
	return redirect('rpg')
