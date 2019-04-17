from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, View, RedirectView
)
from django.db.models import Q

from datetime import date

from .forms import ReturnProductForm
from .models import Product, ProductInstance
from .helpers import set_product_availability, set_current_borrower


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
                Q(human_readable_name__icontains=search)  |
                Q(model_number__icontains=search)
            )
        return queryset


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/product_create.html'
    fields = '__all__'


class ProductUpdateView(UpdateView):
    model= Product
    template_name = 'product/product_create.html'
    fields = '__all__'


class ProductInstanceBorrowView(LoginRequiredMixin, CreateView):
    model = ProductInstance
    template_name = 'product/product_borrow.html'
    fields = ('rental_end',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.get(pk=self.kwargs['pk'])
        context['product'] = product
        return context

    def get_success_url(self):
        return reverse('all-products')

    def form_valid(self, form):
        related_product = Product.objects.get(pk=self.kwargs.get('pk'))
        set_product_availability(related_product, "o")
        set_current_borrower(related_product, self.request.user)

        form.instance.borrower = self.request.user
        form.instance.product = related_product
        return super().form_valid(form)


class ProductInstanceReturnView(UpdateView):
    model = ProductInstance
    context_object_name = 'product'
    template_name = 'product/return_form.html'
    form_class = ReturnProductForm

    def get_success_url(self):
        return reverse('all-products')

    def form_valid(self, form):
        related_product = Product.objects.get(
            pk=form.instance.product.id
        )
        set_product_availability(related_product, "a")
        set_current_borrower(related_product, None)

        today = date.today().strftime("%Y-%m-%d")
        form.instance.returned = today
        return super().form_valid(form)


class ProductRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'], loan_status="o")
        product_instance = get_object_or_404(
            ProductInstance, product=product,
            borrower=self.request.user,
            returned=None
        )
        return reverse('product-return', args=[product_instance.id])


class BorrowedProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super(BorrowedProductListView, self).get_queryset()
        borrowed_products = queryset.filter(
            current_borrower=self.request.user
        )
        return borrowed_products
