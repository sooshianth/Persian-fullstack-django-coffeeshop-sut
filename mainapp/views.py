from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

def homepage(request):
    return render(request, 'index/index.html', {})

class RegisterView(UserCreationForm):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/registration.html"