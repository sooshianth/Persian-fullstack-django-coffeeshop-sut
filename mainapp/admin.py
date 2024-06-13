from django.contrib import admin
from .models import Product, RawMaterial, ProductRawMaterial

class ProductRawMaterialInline(admin.TabularInline):
    model = ProductRawMaterial
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    inlines = (ProductRawMaterialInline,)

class RawMaterialAdmin(admin.ModelAdmin):
    list_display = ['name', 'stock']


admin.site.register(Product, ProductAdmin)
admin.site.register(RawMaterial)
