# sales/forms.py
from django import forms
from .models import Sale

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        # sale_date is auto_now_add in model so we don't include it for create.
        fields = ['car', 'customer', 'sale_price']
        widgets = {
            'car': forms.Select(attrs={'class': 'form-control', 'id': 'id_car'}),
            'customer': forms.Select(attrs={'class': 'form-control', 'id': 'id_customer'}),
            'sale_price': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_sale_price', 'step': '0.01'}),
        }
