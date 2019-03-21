from django.db import models
from borrowing.users.models import User

from .states import STATES


class WarehouseManager(models.Model):
    manager = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.manager.username


class Warehouse(models.Model):
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2, choices=STATES)
    manager = models.ForeignKey('WarehouseManager', on_delete=models.CASCADE)

    def __str__(self):
        return self.city
