from .models import Item
import django_filters
from .choices import CATEGORIES, CONDITION_CHOICES, PAYMENT_METHODS


class ItemFilter(django_filters.FilterSet):
    item_name = django_filters.CharFilter(lookup_expr='icontains')
    item_description = django_filters.CharFilter(lookup_expr='icontains')
    item_categories = django_filters.ChoiceFilter(choices=CATEGORIES)
    item_condition = django_filters.ChoiceFilter(choices=CONDITION_CHOICES)
    item_price__gt = django_filters.NumberFilter(field_name='item_price', lookup_expr='gt')
    item_price__lt = django_filters.NumberFilter(field_name='item_price', lookup_expr='lt')
    item_preferred_payment_method = django_filters.ChoiceFilter(choices=PAYMENT_METHODS)

    class Meta:
        model = Item
        fields = ['item_name', 'item_description', 'item_categories', 'item_price', 'item_condition', 'item_preferred_payment_method',]
