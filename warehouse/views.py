from django.shortcuts import reverse
from .models import Warehouse

from django.views.generic import CreateView, DeleteView, UpdateView


class WarehouseCreate(CreateView):
    model = Warehouse
    fields = '__all__'
    template_name = 'warehouse/warehouse_create_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form_type'] = 'create'
        context['from'] = self.request.GET.get('from')
        return context

    def get_success_url(self, **kwargs):
        next_url = self.request.GET.get('next', None)
        if next_url:
            return next_url
        else:
            return reverse('all-products')


class WarehouseUpdate(UpdateView):
    model = Warehouse
    fields = '__all__'
    template_name = 'warehouse/warehouse_create_update.html'
