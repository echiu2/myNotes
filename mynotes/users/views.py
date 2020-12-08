from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.conf import settings
from .forms import signupForm, loginForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = signupForm()
    context = {'form': form}
    return render(request, 'users/signup.html', context)

def login_user(request):
    form = loginForm()

    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username or Password is incorrect!')

    context = {'form': form}
    return render(request, 'users/login.html', context)

def logout_user(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)
