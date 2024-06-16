from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import Member
# from django.contrib.auth.models import User

class MemberRegisterForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Member
        fields = UserCreationForm.Meta.fields + ('first_name','last_name','phone_number')

class MemberChangeForm(UserChangeForm):

    class Meta:
        model = Member
        fields = UserChangeForm.Meta.fields

