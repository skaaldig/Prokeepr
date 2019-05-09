import datetime
from django.db import models
from django.shortcuts import reverse
from django.core.exceptions import ValidationError


STATUS = (
    ('m', 'Maintenance'),
    ('o', 'On Loan'),
    ('a', 'Available')
)


def manufacturer_directory(instance, filename):
    return f'{instance.manufacturer}/{filename}'


class Product(models.Model):
    image = models.ImageField(upload_to=manufacturer_directory, null=True)
    model_number = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    human_readable_name = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    bin_location = models.CharField(max_length=25)
    loan_status = models.CharField(max_length=1, choices=STATUS, default="a")

    manufacturer = models.ForeignKey('manufacturer.Manufacturer', on_delete=models.CASCADE)
    warehouse = models.ForeignKey('warehouse.Warehouse', null=True, on_delete=models.CASCADE)
    current_borrower = models.ForeignKey('users.User', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_number

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.pk])


def future_dates_only(date):
    if date < datetime.date.today():
        raise ValidationError("Rental End date cannot be in the past.")


class ProductInstance(models.Model):
    requested = models.DateField(auto_now_add=True)
    rental_end = models.DateField(validators=[future_dates_only])
    returned = models.DateField(blank=True, null=True)
    return_note = models.TextField(blank=True, help_text="Where you left the demo and any notes on condition")

    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    borrower = models.ForeignKey('users.User', blank=True, on_delete=models.CASCADE)
    returned_to = models.ForeignKey('warehouse.Warehouse', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"User: {self.borrower} Date: {self.requested} - {self.rental_end} " \
               f"Product: {self.product.human_readable_name}"

    def get_absolute_url(self):
        return reverse('product-instance', args=[self.pk])
