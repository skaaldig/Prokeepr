from django.shortcuts import reverse
from product.models import Product

from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, View, RedirectView
)

from .forms import CreateProductForm

class ProductCreate(CreateView):
    model = Product
    form_class = CreateProductForm
    template_name = 'manager/create_product.html'

    def get_success_url(self):
        return reverse('all-products')


class ProductUpdate(UpdateView):
    model = Product
    form_class = CreateProductForm
    template_name = 'manager/create_product.html'

    def get_success_url(self):
        return reverse('all-products')
