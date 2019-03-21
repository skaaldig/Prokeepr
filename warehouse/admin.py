from django.contrib import admin

from .models import Warehouse, WarehouseManager

# Register your models here.
admin.site.register(Warehouse)
admin.site.register(WarehouseManager)
