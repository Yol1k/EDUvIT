from datetime import datetime
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login

from .forms import AuthUserForm, UserCreationForm

class Login(LoginView):
    fields = ['username', 'password']
    template_name = 'users/login.html'
    form_class = AuthUserForm

class Logout(LogoutView):
    template_name = 'users/logout.html'

def register(request):
    regform = UserCreationForm(request.POST)
    if request.method=="POST":
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_active = True
            reg_f.is_staff = False
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()
            reg_f.save()

            reg_f.backend= 'django.contrib.auth.backends.ModelBackend'
            login(request, reg_f)
            return redirect('blog:index')
    else:
        regform = UserCreationForm()
    return render(request, "users/registration.html", {"regform": regform})

