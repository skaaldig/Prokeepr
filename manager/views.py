from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView

from product.models import Product, ProductInstance


class RentalHistory(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = ProductInstance
    template_name = 'manager/rental_history.html'
    context_object_name = 'rentals'
    paginate_by = 25
    ordering = ('-requested',)
    permission_required = ('product.add_product')
    raise_exception = True

