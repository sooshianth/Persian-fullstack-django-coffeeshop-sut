from django import forms
from django.utils.translation import gettext as _
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import AuthenticationForm
# from .models import Customer

class LogInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class MakeOrderForm(forms.Form):
    pass


class AddProductForm(forms.Form):
    pass


class AddMaterialForm(forms.Form):
    pass

