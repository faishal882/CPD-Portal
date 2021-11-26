from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import  CustomUserCreationForm, LoginForm
from django.shortcuts import render, redirect

# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.models import User
# from django.urls import reverse
# from django.http import HttpResponse
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.core.exceptions import ValidationError
 

# @login_required(login_url='/login/')
# return HttpResponseRedirect(reverse('core:HomeView'))


def  user_register_view(request):
    form = CustomUserCreationForm(request.POST or None)
    if  request.POST and form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect("/")
    return render(request, 'users/register_user.html', {'form':form})

def login_view(request, *args, **kwargs):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return HttpResponseRedirect("/")
    return render(request, 'users/login.html', {'form':form})
    


def logout_view(request, *args, **kwargs):
    logout(request)
    return HttpResponseRedirect("/auth/login/")

