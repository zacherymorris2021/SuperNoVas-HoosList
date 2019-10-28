from django.test import TestCase, Client, override_settings
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

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_to_add_page(self):
        resp = self.client.get('/marketplace/add-item/')

        self.assertEquals(resp.status_code, 200)


class homeTest(TestCase):
    def test_home(self):
        resp = self.client.get('')
        self.assertEquals(resp.status_code, 200)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_index(self):
        resp = self.client.get('/marketplace/')
        self.assertTemplateUsed(resp, 'marketplace/index.html')

class searchTest(TestCase):
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_search(self):
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

        resp = self.client.get('/marketplace/search/', {'q' : 'table'} )
        self.assertEquals(resp.status_code, 200)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_search_2(self):
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


        resp = self.client.get('/marketplace/search/', {'q' : 'table'} )
        self.assertContains(resp, 'Big Table')
