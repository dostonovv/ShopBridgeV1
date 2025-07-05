# orders/forms.py
from django import forms

class OrderForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        label="Nechta dona?",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': '1'
        })
    )
