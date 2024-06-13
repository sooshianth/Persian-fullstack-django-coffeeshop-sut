from django.contrib import admin
from .models import Product, Storage, ProductStorage, Order, OrderProduct, Customer, CustomerOrder

class ProductStorageInline(admin.TabularInline):
    model = ProductStorage
    extra = 1

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1

class CustomerOrderInline(admin.TabularInline):
    model = CustomerOrder
    extra = 1

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'datetime_signed_up']
    inlines = (CustomerOrderInline,)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'customer', 'order_date']
    inlines = (OrderProductInline,)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    inlines = (ProductStorageInline,)

class StorageAdmin(admin.ModelAdmin):
    list_display = ['name', 'stock']


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Storage)
admin.site.register(Customer, CustomerAdmin)
