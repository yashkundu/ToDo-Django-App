from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from .forms import LoginForm, SignUpForm

def home_page(request):
    return render(request,'home_page.html',{})


def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = User.objects.create_user(username=username, password=password)
            return HttpResponseRedirect(reverse('login'))
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username, password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('User is not authenticated.')
    return render(request, 'login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
