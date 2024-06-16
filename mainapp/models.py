from django.db import models
from django.core import validators
from members.models import Member


class Storage(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField(default=0, validators=[validators.MinValueValidator(0)])

    # other fields as needed

    def __str__(self):
        return self.name
    
  
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[validators.MinValueValidator(0)])
    timeNeeded = models.IntegerField(default=0, validators=[validators.MaxValueValidator(60)])
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    raw_materials = models.ManyToManyField(Storage, through='ProductStorage')
    vertical = models.BinaryField(auto_created=True, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name
    
class ProductStorage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    raw_materials = models.ForeignKey(Storage, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.raw_materials.name} for {self.product.name}"


class Order(models.Model):
    customer = models.ForeignKey(Member, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct')
    order_date = models.DateTimeField(auto_now_add=True)
    Type = models.BinaryField(blank=True, null=True) 

    def __str__(self) -> str:
        return str(self.pk)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, validators=[validators.MinValueValidator(1)])

    def __str__(self) -> str:
        return f"{self.quantity} of {self.product.name} for {self.order.customer}"

class CustomerOrder(models.Model):
    customer = models.ForeignKey(Member, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.pk)
    
