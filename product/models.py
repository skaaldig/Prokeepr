from django.db import models
from django.shortcuts import reverse
from django.core.exceptions import ValidationError

from borrowing.users.models import User
from warehouse.models import Warehouse

class Manufacturer(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Product(models.Model):
    model_number = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    bin_location = models.CharField(max_length=25)

    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    warehouse = models.ForeignKey('warehouse.Warehouse', null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.model_number

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.pk])


class ProductInstance(models.Model):
    requested = models.DateField(auto_now_add=True)
    rental_start = models.DateField()
    rental_end = models.DateField()
    returned = models.DateField(blank=True, null=True)

    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    borrower = models.ForeignKey('users.User', blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product} {self.borrower} {self.requested}"


