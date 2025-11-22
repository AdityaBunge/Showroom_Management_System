# inventory/forms.py
from django import forms
from .models import Inventory

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['car', 'quantity', 'min_stock', 'location']
        widgets = {
            'car': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'min_stock': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }
