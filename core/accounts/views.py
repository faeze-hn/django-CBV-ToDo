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
    def get_success_url(self):
        return reverse_lazy("task_list")


class RegisterPage(FormView):
    template_name = "accounts/register.html"
    form_class = UserCreationForm
    redirect_authentication_user = True
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)