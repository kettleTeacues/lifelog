from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.views.generic import CreateView

from .models import customuser

class customUserCreationForm(UserCreationForm):
    class Meta:
        model = customuser
        fields = [
            'email',
            'password1',
            'password2'
        ]

class customCreateView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = customUserCreationForm
    success_url = '/'

class customLoginView(LoginView):
    redirect_authenticated_user=True
    template_name='accounts/login.html'

class customPasswordChangeView(PasswordChangeView):
    redirect_authenticated_user=True
    template_name='accounts/passwordChange.html'
    success_url = 'accounts/passwordchanged/'

class customPasswordChangeDoneView(PasswordChangeDoneView):
    redirect_authenticated_user=True
    template_name='accounts/passwordChangeDone.html'