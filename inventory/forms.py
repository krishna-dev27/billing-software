from django import forms
from inventory.models import *




class ProductMF(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'


class InvoiceForm(forms.ModelForm):
    class Meta:
        model=Invoice
        fields=['customer']


class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model=InvoiceItem
        fields=['product','quantity']