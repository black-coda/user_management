from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=20)
    email = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2',)
