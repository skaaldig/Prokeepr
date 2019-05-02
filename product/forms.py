from django.forms import ModelForm

from .models import ProductInstance, Product


class ReturnProductForm(ModelForm):
    class Meta:
        model = ProductInstance
        fields = ('returned_to', 'return_note')


class CreateProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('current_borrower', 'loan_status', 'created')

