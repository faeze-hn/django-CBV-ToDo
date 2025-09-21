from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import redirect
from django.shortcuts import render

# Create your views here.
class LoginView(LoginView):
    template_name = "accounts/login.html"
    fields = "username","password"
    redirect_authentication_user = True
    success_url = "/task-list/"

    
class RegisterPage(FormView):
    pass