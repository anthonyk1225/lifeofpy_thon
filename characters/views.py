import random
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import View
from characters.models import Character, HeroAttribute
from attacks.models import Attack
from users.models import User

# Create your views here.
attacks = Attack.objects.all()
class WelcomeView(View):
    template = 'characters/welcome.html'

    def get(self,request):
        if not request.session.get('key', False):
            return redirect('/users/')
        user = User.objects.get(key=request.session['key'])
        return render(request, self.template,{'username': user.username})

class ListHeroView(View):

    def get(self, request):
        user_characters = Character.objects.filter(user__key=request.session['key'])
        characters = [{'id':character.id,'name':character.name} for character in user_characters]
        return JsonResponse({'characters': characters})

class HeroView(View):
    template_name = 'characters/hero.html'

    def get(self,request,character_id):
        character = Character.objects.get(id=character_id)
        attributes = HeroAttribute.objects.get(character__pk=character_id)
        attacks = character.attack.all()
        return render(request, self.template_name, {'character':character, 'attributes': attributes, 'attacks': attacks})

class CreateHeroView(View):

    def post(self, request):
        current_user = User.objects.filter(key=request.session['key'])
        new_char = Character.objects.create(race=request.POST['race'], name=request.POST['name'], user=current_user[0])
        new_char.attack = [random.choice(attacks)]
        new_char.save()
        HeroAttribute.objects.create(hit_points=40,power=5,character=new_char)
        return redirect('/characters/')

class EditHeroView(View):
    template_name = 'characters/hero_edit.html'

    def get(self, request):
        character = Character.objects.filter(id=request.GET['character_id'],user__key=request.session['key'])
        if len(character) == 1:
            return render(request, self.template_name, {'character': character[0], 'attacks':character[0].attack.all(),'attributes': character[0].heroattribute_set.all()})
        return redirect('/characters/')

    def post(self, request):
        character = Character.objects.filter(id=request.POST['character_id'],user__key=request.session['key'])
        if len(character) == 1:
            character[0].name = request.POST['name']
            character[0].save()
            return redirect('/characters/%s/' % character[0].id)
        return redirect('/characters/')

class DeleteHeroView(View):

    def post(self, request):
        character = Character.objects.filter(id=request.POST['character_id'],user__key=request.session['key'])
        if len(character) == 1:
            character[0].delete()
            return redirect('/characters/')
        return redirect('/users/')