from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import Member
from django.contrib.auth import password_validation
from django.utils.translation import gettext as _

# from django.contrib.auth.models import User

class MemberRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("رمز عبور"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("تایید رمز عبور"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("لطفا جهت صحت سنجی رمز عبور خود را مجدد وارد کنید"),
    )

    class Meta(UserCreationForm):
        model = Member
        fields = UserCreationForm.Meta.fields + ('first_name','last_name','phone_number', 'password1', 'password2')

class MemberChangeForm(UserChangeForm):

    class Meta:
        model = Member
        fields = UserChangeForm.Meta.fields

class PasswordResetForm(forms.Form):
    username = forms.CharField(label=_("نام کاربری یا ایمیل"),max_length=150)
    first_name = forms.CharField(label=_("نام"),max_length=30)
    phone_number = forms.CharField(label=_("شماره همراه"),max_length=15)
    new_password = forms.CharField(label=_("رمز عبور جدید"),widget=forms.PasswordInput)
