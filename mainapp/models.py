from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext as _

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

class CustomerManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Customer(AbstractUser):
    email = models.EmailField(_("ایمیل"), max_length=255, unique=True) # either user or email
    first_name = models.CharField(_("نام") ,max_length=255)
    last_name = models.CharField(_("نام خانوادگی"),max_length=255)
    datetime_signed_up = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(_("شماره همراه"),max_length=11, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = CustomerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']

    def __str__(self):
        return self.first_name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
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
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.pk)
    
