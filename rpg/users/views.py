from django.views.generic import View
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from users.forms import UserForm
from users.models import User

# Create your views here.
class IndexView(View):
    template = 'users/index.html'
    def get(self,request):
        request.session.flush()
        return render(request, self.template)

class LogInView(View):
    form_class = UserForm
    template_name = 'users/log_in.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username)
        if len(user) == 1 and check_password(password,user[0].password):
            user[0].save()
            request.session['user_id']=user[0].id
            return redirect('/rpg/welcome/')
        return render(request, self.template_name, {'error': 'Invalid Username or Password','form': self.form_class()})
    
class LogOutView(View):
    def get(self, request):
        request.session.flush()
        return redirect('/rpg/')

class RegisterView(View):
    form_class = UserForm
    template_name = 'users/register.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        new_user = UserForm(request.POST)
        if new_user.is_valid():
            hashed = make_password(request.POST['password'])
            user = User(username=request.POST['username'], password=hashed)
            user.save()
            request.session['user_id'] = user.id
            return render(request, 'users/welcome.html',{'username': user.username})
        return redirect('/rpg/log_in/')

class WelcomeView(View):
    template = 'users/welcome.html'

    def get(self, request):
        if not request.session.get('user_id', False):
            return redirect('/rpg/')
        # request.session.set_expiry(120)
        user = User.objects.get(id=request.session['user_id'])
        return render(request, self.template, {'username': user.username})

class ChooseCharView(View):
    template_name = 'characters/characters.html'

    def get(self, request):
        return render(request, self.template_name)





