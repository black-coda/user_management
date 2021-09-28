from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from . forms import SignUpForm

# Create your views here.

def dashboard(request):
    return render(request,"user/home.html")


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username = username, password = password)
        login(request, user)
        return redirect('dashboard')

    else:
        SignUpForm()
    return render(request, 'registration/signup.html', {'form':form})
    
