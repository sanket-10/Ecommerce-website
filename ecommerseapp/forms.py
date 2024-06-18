from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["user","product","quantity","address","pincode","city","country","contact_no"]