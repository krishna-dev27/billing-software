from django import forms
from inventory.models import *




class ProductMF(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'