from django.shortcuts import reverse, redirect
from django.views.generic import CreateView, UpdateView

from .models import Manufacturer

# Create your views here.
class ManufacuterCreate(CreateView):
    model = Manufacturer
    fields = '__all__'
    template_name = 'manufacturer/manufacturer_create_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form_type'] = 'create',
        context['from'] = self.request.GET.get('from')
        return context

    def get_success_url(self, **kwargs):
        next_url = self.request.GET.get('next', None)
        if next_url:
            return next_url
        else:
            return reverse('all-products')


class ManufacturerUpdate(UpdateView):
    model = Manufacturer
    fields = '__all__'
    template_name = 'manufacturer/manufacturer_create_update.html'
