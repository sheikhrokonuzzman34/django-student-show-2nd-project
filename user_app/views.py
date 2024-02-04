from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .forms import *

from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout

# from django.contrib.auth.decorators import login_required
# @login_required(login_url='login')

# Create your views here.


def register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password ase not Same!!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'user_app/register.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            auth_login(request, user)
            return redirect('user_dashboard')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'user_app/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')



def user_dashboard(request):
    return render(request, 'user_app/user_dashboard.html')



@login_required
def profileupdate(request):
    p_form = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        p_form = UpdateProfileForm(
            request.POST, request.FILES, instance=p_form)
        if p_form.is_valid():
            p_form.save()
            return redirect('/')

    context = {
        'p_form': p_form,
    }

    return render(request, 'user_app/profileupdate.html', context)
