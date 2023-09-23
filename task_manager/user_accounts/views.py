from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout


def user_registration(request):
    """ Register a new user account. """
    if not request.user.is_authenticated:
        if request.method == "POST":
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                messages.success(request, 'Congratulation!!. Please Login.')
                registration_form.save()
                return redirect('login')
        else:    
            registration_form = RegistrationForm()
        context = {'registration_form':registration_form}    
        return render(request, 'user_accounts/registration.html', context)
    else:
        return redirect('tasks')


def user_login(request):
    """  Authenticate a user and log them in. """
    if not request.user.is_authenticated:
        if request.method == 'POST':
            uname = request.POST.get('username')
            upass = request.POST.get('password')
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in Successfully !')
                return redirect('tasks')
            else:
                messages.info(request, 'Invalid username or password. Please try again.') # Fix the typo here
                return redirect('login')
        else:
            login_form = LoginForm()
        context = {'login_form': login_form}
        return render(request, 'user_accounts/login.html', context)
    else:
        return redirect('tasks')
    

def user_logout(request):
    """ Log out the currently authenticated user. """
    logout(request)
    return redirect('login') 