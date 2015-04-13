from django.views.generic import View
from django.shortcuts import render,redirect
from django.http import JsonResponse,Http404
from django.contrib.auth.hashers import make_password,check_password
from users.forms import UserForm
from users.models import User

# Create your views here.
class IndexView(View):
    form_class = UserForm
    template = 'users/index.html'

    def get(self,request):
        request.session.flush()
        return render(request, self.template,{'form': self.form_class()})

class LogInView(View):
    form_class = UserForm

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username)
        if len(user) == 1 and check_password(password,user[0].password):
            user[0].save()
            request.session['user_id']=user[0].id
            return redirect('/characters/')
        return redirect('/characters/')
        # return JsonResponse({'error': 'Invalid Username or Password'})

class LogOutView(View):
    def get(self, request):
        request.session.flush()
        return redirect('/users/')

class RegisterView(View):
    form_class = UserForm

    def post(self, request):
        new_user = UserForm(request.POST)
        if new_user.is_valid():
            hashed = make_password(request.POST['password'])
            user = User(username=request.POST['username'], password=hashed)
            user.save()
            request.session['user_id'] = user.id
            return redirect('/characters/')
        return redirect('/users/')
