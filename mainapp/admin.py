from django.contrib import admin
from .models import CustomerAccount, Storage

@admin.register(CustomerAccount)
class AdminCustomerAccount(admin.ModelAdmin):
    list_display = ['pk', 'user', 'first_name', 'last_name', 'datetime_signed_up']

@admin.register(Storage)
class AdminStorage(admin.ModelAdmin):
    list_display = ['pk', 'name', 'amount']
