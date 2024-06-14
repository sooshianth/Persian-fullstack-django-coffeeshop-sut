from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import Customer
# from django.contrib.auth.models import User

class CustomerRegisterForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Customer
        fields = UserCreationForm.Meta.fields + ('first_name','last_name','phone_number')

class CustomerChangeForm(UserChangeForm):

    class Meta:
        model = Customer
        fields = UserChangeForm.Meta.fields

