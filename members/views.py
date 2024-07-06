from django.shortcuts import render, redirect
from django.views import generic
from .forms import MemberRegisterForm 
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseNotAllowed
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import PasswordResetForm


class RegisterView(generic.CreateView):
    form_class = MemberRegisterForm
    success_url = reverse_lazy('login')
    template_name = "registration/register.html"

class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])
    

User = get_user_model()

def password_reset_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            phone_number = form.cleaned_data['phone_number']
            new_password = form.cleaned_data['new_password']

            try:
                user = User.objects.get(username=username, first_name=first_name, phone_number=phone_number)
                user.set_password(new_password)
                user.save()
                messages.success(request, 'رمز با موفقیت تغییر یافت')
                return redirect('login')
            except User.DoesNotExist:
                messages.error(request, 'چنین کاربری یافت نشد.')
    else:
        form = PasswordResetForm()

    return render(request, 'registration/forget_password.html', {'form': form})
