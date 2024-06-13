from django.contrib import admin
from .models import Product, RawMaterial, ProductRawMaterial, Order, OrderProduct, CustomerAccount

class CustomerAccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'datetime_signed_up']

class ProductRawMaterialInline(admin.TabularInline):
    model = ProductRawMaterial
    extra = 1

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    inlines = (ProductRawMaterialInline,)

class RawMaterialAdmin(admin.ModelAdmin):
    list_display = ['name', 'stock']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'customer', 'order_date']
    inlines = (OrderProductInline,)

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(RawMaterial)
admin.site.register(CustomerAccount, CustomerAccountAdmin)
