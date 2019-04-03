from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView
)
from django.db.models import Q

from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'
    paginate_by = 25

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        search = self.request.GET.get("q")

        if search:
            return queryset.filter(
                Q(manufacturer__name__icontains=search) |
                Q(description__icontains=search)  |
                Q(model_number__icontains=search)
            )
        return queryset


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/product_create.html'
    fields = '__all__'

class ProductUpdateView(UpdateView):
    model= Product
    template_name = 'product/product_create.html'
    fields = '__all__'
