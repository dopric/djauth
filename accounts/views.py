from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterUserForm

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        psw = request.POST.get('password')

        user = authenticate(username=username, password=psw)
        if user is not None:
            print("KNOWN USER")
            login(request, user)
            print("USER LOGGED IN, redirect")
            return redirect('main:index')
        else:
            messages.error(request, ('Invalid credentials'))

    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('main:index')


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
       
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
            return redirect('accounts:login')
    else:
        form = RegisterUserForm()

    return render(request, 'accounts/register.html', {'form': form})