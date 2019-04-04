from django.shortcuts import render, reverse
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView
)
from django.db.models import Q

from datetime import date

from .models import Product, ProductInstance
from .helpers import set_product_availability


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


class ProductInstanceBorrowView(CreateView):
    model = ProductInstance
    template_name = 'product/product_create.html'
    fields = ('rental_start', 'rental_end')

    def get_success_url(self):
        return reverse('all-products')

    def form_valid(self, form):
        related_product = Product.objects.get(pk=self.kwargs.get('pk'))

        set_product_availability(related_product, "o")
        form.instance.borrower = self.request.user
        form.instance.product = related_product
        return super().form_valid(form)


class ProductInstanceReturnView(UpdateView):
    model = ProductInstance
    template_name = 'product/product_create.html'
    fields = ('return_note', 'returned_to')

    def get_success_url(self):
        return reverse('all-products')

    def form_valid(self, form):
        related_product = Product.objects.get(
            pk=form.instance.product.id
        )

        set_product_availability(related_product, "a")
        today = date.today().strftime("%Y-%m-%d")
        form.instance.returned = today
        return super().form_valid(form)

