import datetime
from django.forms import ModelForm, DateInput

from .models import ProductInstance, Product


class ReturnProductForm(ModelForm):
    class Meta:
        model = ProductInstance
        fields = ('returned_to', 'return_note')

class BorrowProductForm(ModelForm):
    class Meta:
        model = ProductInstance
        fields = ('rental_end',)
        widgets = {
            'rental_end': DateInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#id_rental_end'
            })
        }


class CreateProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('current_borrower', 'loan_status', 'created')

