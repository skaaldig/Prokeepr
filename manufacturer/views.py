from django.shortcuts import reverse, redirect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Manufacturer

# Create your views here.
class ManufacuterCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Manufacturer
    fields = '__all__'
    template_name = 'manufacturer/manufacturer_create_update.html'
    permission_required = ('manufacturer.can_add_manufacturer',)
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


class ManufacturerUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Manufacturer
    fields = '__all__'
    template_name = 'manufacturer/manufacturer_create_update.html'
    permission_required = ('manufacturer.can_change_manufacturer',)
    raise_exception = True
