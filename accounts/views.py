from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth import login, authenticate, logout
from django.conf import settings

from accounts.forms import ExtendedUserCreationForm
from .decorators import unauthenticated_user

#
# HOME / LOGIN 
#
@unauthenticated_user
def home(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')     
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('cultivation_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@unauthenticated_user
def register(request):
    if request.method == "POST":
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return redirect('cultivation_list')
    else:
        form = ExtendedUserCreationForm()
    return render(request, 'register.html', {'form': form})

@unauthenticated_user
def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(from_email=settings.DEFAULT_FROM_EMAIL, request=request)
            return redirect('home')
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset.html', {'form': form})    