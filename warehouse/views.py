from django.shortcuts import reverse
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Warehouse, WarehouseManager


class WarehouseCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Warehouse
    fields = '__all__'
    template_name = 'warehouse/warehouse_create_update.html'
    permission_required = ('warehouse.can_add_warehouse',)
    raise_exception = True

    def get_context_data(self):
        context = super().get_context_data()
        context['form_type'] = 'create'
        context['from'] = self.request.GET.get('from')
        return context

    def get_success_url(self):
        next_url = self.request.GET.get('next', None)
        if next_url:
            return next_url
        else:
            return reverse('all-products')


class WarehouseUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Warehouse
    fields = '__all__'
    template_name = 'warehouse/warehouse_create_update.html'
    permission_required = ('warehouse.can_change_warehouse',)
    raise_exception = True


class WarehouseManagerCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = WarehouseManager
    fields = '__all__'
    template_name = 'warehouse/warehouse_manager_create_update.html'
    permission_required = ('warehouse.can_add_warehouse_manager',)
    raise_exception = True

    def get_context_data(self):
        context = super().get_context_data()
        context['from'] = self.request.GET.get('from')
        return context

    def get_success_url(self):
        next_url = self.request.GET.get('next', None)
        if next_url:
            return next_url
        else:
            return reverse('all-products')

