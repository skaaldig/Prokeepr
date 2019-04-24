from django.forms import ModelForm, Select

from .models import ProductInstance, Product


class ReturnProductForm(ModelForm):
    class Meta:
        model = ProductInstance
        fields = ('returned_to', 'return_note')
        widgets = {
            'returned_to': Select(attrs={'class': 'borrow__returned-to'})
        }


class CreateProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('current_borrower', 'loan_status', 'created')
        widgets = {
            'manufacturer': Select(attrs={'class': 'create__dropdown'}),
            'warehouse': Select(attrs={'class': 'create__dropdown'})
        }
