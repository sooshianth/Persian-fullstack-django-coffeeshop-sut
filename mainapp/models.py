from django.db import models
from django.core import validators

class CustomerAccount(models.Model):
    user = models.CharField(max_length=255) # either user or email
    password = models.CharField(max_length=255, validators=[validators.RegexValidator(r'^[0-9a-zA-Z ]+$')])
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    datetime_signed_up = models.DateTimeField(auto_now_add=True)
    current_cart = []
    all_products_ever = []

    def __str__(self):
        return self.user

class Storage(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()


    def __str__(self):
        return self.name


