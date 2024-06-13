# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from django.contrib import messages
# from .forms import SignUpForm, LogInForm
from django.views.generic.edit import CreateView
from .models import Customer

def homepage(request):
    return render(request, 'index/index.html', {})

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')  # Redirect to a home page or a dashboard after successful signup
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})

class SignUpView(CreateView):
    model = Customer
    template_name= "signup.html"
    fields = ['user', 'first_name', 'last_name', 'phone_number', 'password']


# def login(request):
#     if request.method == 'POST':
#         form = LogInForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.cleaned_data.get('user')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=user, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')  # Redirect to a home page or a dashboard after successful login
#     else:
#         form = LogInForm()
#     return render(request, 'login.html', {'form': form})

# def logout_view(request):
#     logout(request)
#     return redirect('login/login.html')
