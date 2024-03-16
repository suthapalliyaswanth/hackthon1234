
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('home') 

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # Redirect to a success page.
            return redirect('home')  # Change 'home' to your desired URL name
    else:
        form = UserCreationForm()
    return render(request, 'signup/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')  # Change 'home' to your desired URL name
        else:
            # Return an 'invalid login' error message.
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    else:
        return render(request, 'login/login.html')

def home(request):
    print(request.user.is_authenticated)
    return render(request, 'home/home.html')

def dummy_view(request):
    return HttpResponse("This is a dummy page.")

def dashboard(re):
    return render(re, 'dashboard.html')

