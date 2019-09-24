from django import forms
from .models import Item

class ItemAddForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
        'item_name',
        'seller',
        'item_description',
        'item_price',
        'item_delivery',
        'item_location',
        'item_preferred_payment_method',
        'item_condition',
        'item_categories'
        ]
