# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.forms import UserCreationForm
# from .models import Customer


# class LogInForm(AuthenticationForm):
#     user = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


# class SignUpForm(UserCreationForm):
#     user = forms.CharField(max_length=200, help_text='ضروری')
#     first_name = forms.CharField(max_length=200, help_text='ضروری')
#     last_name = forms.CharField(max_length=200)
#     phone_number = forms.IntegerField(max_length=11, help_text='اختیاری')
#     password = forms.PasswordInput()

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'phone_number', 'password')
    
#     def save(self, commit=True):
#         if commit:
#             profile = Customer.objects.create(**forms.cleaned_data)
#             profile.save()
#         return user

# class MakeOrderForm(forms.Form):
#     pass


# class AddProductForm(forms.Form):
#     pass


# class AddMaterialForm(forms.Form):
#     pass

