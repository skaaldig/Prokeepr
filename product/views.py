from django.shortcuts import render, reverse
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView
)
from django.db.models import Q

from .models import Product, ProductInstance


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
        borrowed_product = Product.objects.get(pk=self.kwargs.get('pk'))
        borrowed_product.loan_status = "o"
        borrowed_product.save()

        form.instance.borrower = self.request.user
        form.instance.product = borrowed_product
        return super().form_valid(form)

