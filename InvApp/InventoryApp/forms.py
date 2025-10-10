from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        field = '__all__'
        labels = {
            'product_id': 'Product ID',
            'name': 'Name',
            'sku': 'SKU',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier',
        }
        widgets = {
            'product_id': forms.NumberInput(
                attrs={'placeholder': 'e.g 1', 'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}
            ),
            'name': forms.TextInput(
                attrs={'placeholder': 'e.g. shirt',
                       'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}
            ),
            'sku': forms.TextInput(
                attrs={'placeholder': 'e.g. S12345',
                       'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}
            ),
            'price': forms.NumberInput(
                attrs={'placeholder': 'e.g. 19.99',
                       'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}
            ),
            'quantity': forms.NumberInput(
                attrs={'placeholder': 'e.g. 10', 'class': 'block w-full px-3 py-2     border border-gray-300 rounded-md shadow-sm focus:outline-none        focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}
            ),
            'suplier': forms.TextInput(
                attrs={'placeholder': 'e.g. ABC Corp',
                       'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}
            ),
        }
