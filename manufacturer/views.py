from django.shortcuts import render

from .models import Manufacturer

# Create your views here.
class ManufacuterCreate(CreateView):
    model = Manufacturer
    template_name = 'product/manufacturer_create_update.html'


class ManufacturerUpdate(UpdateView):
    model = Manufacturer
    template_name = 'product/manufacturer_create_update.html'
