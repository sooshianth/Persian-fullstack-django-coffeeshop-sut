from django.shortcuts import render
from django.views import generic
from .forms import MemberRegisterForm 
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseNotAllowed


class RegisterView(generic.CreateView):
    form_class = MemberRegisterForm
    success_url = reverse_lazy('login')
    template_name = "registration/register.html"

class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])