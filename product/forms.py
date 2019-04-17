from django.forms import ModelForm, Select

from .models import ProductInstance


class ReturnProductForm(ModelForm):
    class Meta:
        model = ProductInstance
        fields = ('returned_to', 'return_note')
        widgets = {
            'returned_to': Select(attrs={'class': 'borrow__returned-to'})
        }
