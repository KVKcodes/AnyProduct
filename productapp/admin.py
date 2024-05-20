from django.contrib import admin
from .models import Product_cart, Shopping_cart

# Register your models here.
admin.site.register(Product_cart)
admin.site.register(Shopping_cart)