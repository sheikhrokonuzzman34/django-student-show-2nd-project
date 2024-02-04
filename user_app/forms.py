from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class UserReristrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'profile_image', 'address']
