from django.shortcuts import render
from server.utils import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

class RegisterPage(MyView):
    template_name = 'index/register.html'
    form_user = UserForm
    form_profile = ProfileForm
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index-page')
        
        self.context.update({
            'form_user': self.form_user,
            'form_profile': self.form_profile,
        }) 
        
        return self.render(request)
    def post(self, request, *args, **kwargs):
        data = request.POST.copy()
        act = data.get('act')
        if act == 'register':
            form1 = self.form_user(data)
            form2 = self.form_profile(data)
            if form1.is_valid and form2.is_valid:
                if User.objects.filter(username=data['username']).exists():
                    messages.warning(request, 'duplicate username')
                    return redirect('register-page')
                new_user = User.objects.create_user(
                    username = data['username'],
                    password = data['password'],
                )
                new_user.save()
                new_profile = form2.save(commit=False)
                new_profile.user = new_user
                new_profile.save()
                
        user = authenticate(username=data['username'], password=data['password'])
        if user is not None:
            login(request, user)
            return redirect('index-page')
        
        return redirect('login-page')
    
class LoginPage(MyView):
    template_name = 'index/login.html'
    def get(self, request, *args, **kwargs):
        self.context.update({
            'users': User.objects.all(),
            'profiles': Profile.objects.all(),
        })
        if request.user.is_authenticated:
            return redirect('index-page')
        return self.render(request)
    
    def post(self, request, *args, **kwargs):
        data = request.POST.copy()
        user = authenticate(username=data['username'], password=data['password'])
        if user is not None:
            login(request, user)
            return redirect('index-page')
        messages.warning(request, 'not correct!')
        return redirect('login-page')
        

class LogoutPage(MyView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login-page')
        
class IndexPage(MyView):
    template_name = 'index/index.html'
    permission = 9999
    
    @has_perm
    def get(self, request, *args, **kwargs):
        return self.render(request)
    

    