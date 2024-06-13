from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from .forms import LogInForm
from django.views.generic.edit import CreateView, FormView
from .models import Customer

def homepage(request):
    return render(request, 'index/index.html', {})

class SignUpView(CreateView):
    model = Customer
    template_name= "signup/signup.html"
    fields = ['email', 'first_name', 'last_name', 'phone_number', 'password']

class LogInView(FormView):
    template_name = 'login/login.html'
    form_class = LogInForm
    success_url = reverse_lazy('customer_list')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=email, password=password)

        if user is not None:
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            form.add_error(None, "Invalid email or password")
            return self.form_invalid(form)
        
# def logout_view(request):
#     logout(request)
#     return redirect('login/login.html')
