from django.db import models
from django.core import validators    

class RawMaterial(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField(default=0, validators=[validators.MinValueValidator(0)])

    # other fields as needed

    def __str__(self):
        return self.name
    
  
class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[validators.MinValueValidator(0)])
    timeNeeded = models.IntegerField(default=0, validators=[validators.MaxValueValidator(60)])
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    raw_materials = models.ManyToManyField(RawMaterial, through='ProductRawMaterial')

    def __str__(self):
        return self.name
    
class ProductRawMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.raw_material.name} for {self.product.name}"


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

class Order(models.Model):
    customer = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct')
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.pk)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, validators=[validators.MinValueValidator(1)])

    def __str__(self) -> str:
        return f"{self.quantity} of {self.product.name} for {self.order.customer}"
