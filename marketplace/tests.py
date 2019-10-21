from django.test import TestCase
from .models import Seller, Item
from django.urls import reverse, resolve
from . import views
from . import urls
from .views import index, detail, add_item



# Create your tests here.
# use search bar
# add an item
# view a detailed

class addItemTest(TestCase):
    def test_to_add_item(self):
        i = Item()
        s = Seller()

        s.seller_name = "Caroline"
        s.seller_computing_id = "ch6yg"
        s.save()
        i.item_name = "Big Table"
        i.seller = s
        i.item_description = "wooden, large table for sale"
        i.item_price = "100"
        i.item_location = "uva"
        i.item_condition = 'GOOD'
        i.item_categories = "FURNITURE"
        i.item_preferred_payment_method ="venmo"
        i.save()
        record = Item.objects.get(pk=1)
        self.assertEquals(record, i)

class homeTest(TestCase):
    def test_home(self):
        resp = self.client.get('')
        self.assertEquals(resp.status_code, 200)
