from django.contrib import admin

from .models import Product, Manufacturer, ProductInstance

# Register your models here.
admin.site.register(Product)
admin.site.register(Manufacturer)
admin.site.register(ProductInstance)
