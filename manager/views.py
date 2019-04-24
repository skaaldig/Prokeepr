from product.models import Product, ProductInstance

from django.views.generic import ListView


class RentalHistory(ListView):
    model = ProductInstance
    template_name = 'manager/rental_history.html'
    context_object_name = 'rentals'
    paginate_by = 10
    ordering = ('-requested',)
