from django.http.response import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import  CustomUserCreationForm
from django.shortcuts import render, redirect

# from django.contrib.auth.models import User
# from django.urls import reverse
# from django.http import HttpResponse
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.core.exceptions import ValidationError
 

# @login_required(login_url='/login/')

def user_register_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")

    if request.method == "POST":
        print(request.POST)
        form = CustomUserCreationForm(request.POST)
        print("register form....", form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            # return HttpResponseRedirect(reverse('core:HomeView'))
            return HttpResponseRedirect("/")
        return render(request, 'users/register_user.html', {'form':form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'users/register_user.html', {'form':form})


def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/")
        return render(request, 'users/login.html', {'form':form})
    else:
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form':form})
    
        
    


def logout_view(request, *args, **kwargs):
    print("logout....")
    logout(request)
    return HttpResponseRedirect("/auth/login/")
