from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required
from .forms import CreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


def signup(request):
    if request.method == 'GET':
        return render(request, 'users/signup.html',
                      {'form': CreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'],
                                                first_name=request.POST['first_name'],
                                                last_name=request.POST['last_name'])
                user.save()
                login(request, user)
                return redirect('purposes:index')
            except IntegrityError:
                return render(request, 'users/signup.html',
                              {'form': CreationForm(), 'error': 'Этот пользователь уже существует!'})
        else:
            return render(request, 'users/signup.html',
                          {'form': CreationForm(), 'error': 'Пароли не совпадают!'})


@login_required
def logged_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('users:login')


def log_in(request):
    if request.method == 'GET':
        return render(request, 'users/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'users/login.html', {'form': AuthenticationForm(),
                                                        'error': 'Пароль или логин не верен!'})
        else:
            login(request, user)
            return redirect('purposes:index')
