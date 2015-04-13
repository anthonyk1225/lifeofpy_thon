from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import View
from characters.models import Character, HeroAttribute
from attacks.models import Attack
import random
from users.models import User

# Create your views here.
attacks = Attack.objects.all()
class WelcomeView(View):
    template = 'characters/welcome.html'

    def get(self,request):
        if not request.session.get('user_id', False):
            return redirect('/users/')
        # request.session.set_expiry(120)
        user = User.objects.get(id=request.session['user_id'])
        return render(request, self.template,{'username': user.username})

class CharacterListView(View):
    def get(self, request):
        user_characters = Character.objects.filter(user__pk=request.session['user_id'])
        characters = [{'id':character.id,'name':character.name} for character in user_characters]
        return JsonResponse({'characters':characters})

class ChooseCharView(View):
    template_name = 'characters/characters.html'

    def get(self, request):
        return render(request, self.template_name)

def create_warrior(request):
    current_user = User.objects.filter(id=request.session['user_id'])
    new_char = Character.objects.create(race='warrior', name=request.POST['name'], user=current_user[0])
    new_char.attack = [random.choice(attacks)]
    new_char.save()
    HeroAttribute.objects.create(hit_points=40,power=5,character=new_char)
    return redirect('/characters/')

def create_mage(request):
    current_user = User.objects.filter(id=request.session['user_id'])
    new_char = Character.objects.create(race='mage', name=request.POST['name'], user=current_user[0])
    new_char.attack = [random.choice(attacks)]
    new_char.save()
    HeroAttribute.objects.create(hit_points=22,power=8,character=new_char)
    return redirect('/characters/')

def create_paladin(request):
    print(request.POST)
    current_user = User.objects.filter(id=request.session['user_id'])
    new_char = Character.objects.create(race='paladin', name=request.POST['name'], user=current_user[0])
    new_char.attack = [random.choice(attacks)]
    new_char.save()
    HeroAttribute.objects.create(hit_points=54,power=3,character=new_char)
    return redirect('/characters/')

class HeroView(View):
    template_name = 'characters/hero.html'

	def get(self,request,name):
		character = Character.objects.get(name=name)
		character_attributes = Attribute.objects.filter(character_id=character.id)
		attributes = [attribute for attribute in character_attributes]
		return render(request, self.template_name, {'character':character, 'attributes':attributes})
