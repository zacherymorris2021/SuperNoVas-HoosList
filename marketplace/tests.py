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
    #1
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

    #2
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_to_add_page(self):
        resp = self.client.get('/marketplace/add-item/')

        self.assertEquals(resp.status_code, 200)


class homeTest(TestCase):
    #3
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_home(self):
        resp = self.client.get('')
        self.assertEquals(resp.status_code, 200)

    #4
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_index(self):
        resp = self.client.get('/marketplace/')
        self.assertTemplateUsed(resp, 'marketplace/index.html')
        self.assertContains(resp, "Items currently for sale")

class searchTest(TestCase):
    #5
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

        #6
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
    #7
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_search_3(self):
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

        i2 = Item()
        i2.item_name = "Tshirt"
        i2.seller = s
        i2.item_description = "large  blue tshirt "
        i2.item_price = "100"
        i2.item_location = "uva"
        i2.item_condition = 'GOOD'
        i2.item_categories = "CLOTHING"
        i2.item_preferred_payment_method ="venmo"
        i2.save()
        resp = self.client.get('/marketplace/search/', {'q' : 'table'} )
        self.assertFalse('tshirt' in resp)
        #self.assertContains(resp, 'tshirt')

class filterTest(TestCase):

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def setUp(self):
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

        i2 = Item()
        i2.item_name = "Tshirt"
        i2.seller = s
        i2.item_description = "large  blue tshirt "
        i2.item_price = "100"
        i2.item_location = "uva"
        i2.item_condition = 'GOOD'
        i2.item_categories = "CLOTHING"
        i2.item_preferred_payment_method ="venmo"
        i2.save()
    #8
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_filter(self):
        resp = self.client.get('/marketplace/filter/', {'f': 'FURNITURE'})
        self.assertContains(resp, "Big Table")
    #9
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_filter2(self):
        resp  = self.client.get('/marketplace/filter/', {'f': 'CLOTHING'})
        self.assertContains(resp, "Tshirt")
    #10
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_filter3(self):
        resp = self.client.get('/marketplace/filter/', {'f': 'CLOTHING'})
        self.assertFalse("table" in resp)




class detailTest(TestCase):
    #11
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_detail(self):
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

        i2 = Item()
        i2.item_name = "Tshirt"
        i2.seller = s
        i2.item_description = "large  blue tshirt "
        i2.item_price = "100"
        i2.item_location = "uva"
        i2.item_condition = 'GOOD'
        i2.item_categories = "CLOTHING"
        i2.item_preferred_payment_method ="venmo"
        i2.save()


        resp = self.client.get(reverse('marketplace:detail', args = (i.id,)))
        self.assertContains(resp, 'table')
    #12
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_detail2(self):
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

        i2 = Item()
        i2.item_name = "Tshirt"
        i2.seller = s
        i2.item_description = "large  blue tshirt "
        i2.item_price = "100"
        i2.item_location = "uva"
        i2.item_condition = 'GOOD'
        i2.item_categories = "CLOTHING"
        i2.item_preferred_payment_method ="venmo"
        i2.save()
        resp = self.client.get(reverse('marketplace:detail', args = (i2.id,)))
        self.assertFalse('table' in resp)


# login tests?

#messaging tests
