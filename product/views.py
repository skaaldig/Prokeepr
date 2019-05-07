from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, View, RedirectView, DeleteView
)
from django.db.models import Q

from .forms import ReturnProductForm, CreateProductForm, BorrowProductForm
from .models import Product, ProductInstance
from .helpers import set_product_availability, set_current_borrower


class ProductList(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'
    paginate_by = 25
    ordering = ["-human_readable_name"]

    def get_queryset(self):
        queryset = super(ProductList, self).get_queryset()
        search = self.request.GET.get("q")

        if search:
            return queryset.filter(
                Q(manufacturer__name__icontains=search) |
                Q(human_readable_name__icontains=search)  |
                Q(model_number__icontains=search)
            )
        return queryset


class ProductInstanceBorrow(CreateView):
    model = ProductInstance
    form_class = BorrowProductForm
    template_name = 'product/product_borrow.html'

    def dispatch(self, request, *args, **kwargs):
        self.product = get_object_or_404(Product, pk=kwargs["pk"], loan_status="a")
        return super().dispatch(request, *args, **kwargs)

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


class ProductInstanceReturn(UpdateView):
    model = ProductInstance
    context_object_name = 'rental'
    template_name = 'product/product_return.html'
    form_class = ReturnProductForm
    today = date.today()

    def get_queryset(self):
        query = super(ProductInstanceReturn, self).get_queryset()
        query = query.filter(borrower=self.request.user)
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = self.today
        return context

    def get_success_url(self):
        return reverse('all-products')

    def form_valid(self, form):
        related_product = Product.objects.get(
            pk=form.instance.product.id
        )
        set_product_availability(related_product, "a")
        set_current_borrower(related_product, None)
        form.instance.returned = self.today.strftime("%Y-%m-%d")
        return super().form_valid(form)


class BorrowedProductList(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super(BorrowedProductList, self).get_queryset()
        borrowed_products = queryset.filter(
            current_borrower=self.request.user
        )
        return borrowed_products


class ProductInstanceRedirect(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'], loan_status="o")
        product_instance = get_object_or_404(
            ProductInstance, product=product,
            borrower=self.request.user,
            returned=None
        )
        return reverse('product-return', args=[product_instance.id])


class ProductCreate(CreateView):
    model = Product
    form_class = CreateProductForm
    template_name = 'product/product_create_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form_type'] = 'create'
        return context

    def get_success_url(self):
        return reverse('all-products')


class ProductUpdate(UpdateView):
    model = Product
    form_class = CreateProductForm
    template_name = 'product/product_create_update.html'

    def get_success_url(self):
        return reverse('all-products')


class ProductDelete(DeleteView):
    model = Product
    template_name = 'product/product_delete.html'
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('all-products')
