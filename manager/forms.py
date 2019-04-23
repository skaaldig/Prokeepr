from django.forms import ModelForm, Select

from product.models import Product


class CreateProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('current_borrower', 'loan_status', 'created')
        widgets = {
            'manufacturer': Select(attrs={'class': 'create__dropdown'}),
            'warehouse': Select(attrs={'class': 'create__dropdown'})
        }
