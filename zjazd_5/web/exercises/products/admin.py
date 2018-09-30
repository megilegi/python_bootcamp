from django.contrib import admin
from products.models import Products


# Register your models here.


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'description', 'is_available']
    search_fields = ['name', 'description']
    list_filter = ['is_available']


admin.site.register(Products, ProductsAdmin)
