from django.test import TestCase, Client, override_settings
from django.contrib.auth.models import User
from .models import Seller, Item, Message
from django.urls import reverse, resolve
from . import views
from . import urls
from .views import index, detail, add_item
from .filters import ItemFilter


# Create your tests here.
# use search bar
# add an item
# view a detailed

class addItemTest(TestCase):
    #1
    def test_to_add_item(self):
        i = Item()

        auser = User.objects.create_user('ch6yg', 'ch6yg@virginia.edu', 'password')
        auser.save()


        i.item_name = "Big Table"
        i.seller = auser
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

class searchTest(TestCase):
    #5
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_search(self):
        i = Item()


        auser = User.objects.create_user('ch6yg', 'ch6yg@virginia.edu', 'password')
        auser.save()
        i.item_name = "Big Table"
        i.seller = auser
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

        auser = User.objects.create_user('ch6yg', 'ch6yg@virginia.edu', 'password')
        auser.save()

        i.item_name = "Big Table"
        i.seller = auser
        i.item_description = "wooden, large table for sale"
        i.item_price = "100"
        i.item_location = "uva"
        i.item_condition = 'GOOD'
        i.item_categories = "FURNITURE"
        i.item_preferred_payment_method ="venmo"
        i.save()


        resp = self.client.get('/marketplace/search/', {'q' : 'table'} )
        self.assertContains(resp, 'table')
    #7
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_search_3(self):
        i = Item()

        auser = User.objects.create_user('ch6yg', 'ch6yg@virginia.edu', 'password')
        auser.save()

        i.item_name = "Big Table"
        i.seller = auser
        i.item_description = "wooden, large table for sale"
        i.item_price = "100"
        i.item_location = "uva"
        i.item_condition = 'GOOD'
        i.item_categories = "FURNITURE"
        i.item_preferred_payment_method ="venmo"
        i.save()

        i2 = Item()
        i2.item_name = "Tshirt"
        i2.seller = auser
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

        auser = User.objects.create_user('ch6yg', 'ch6yg@virginia.edu', 'password')
        auser.save()

        i.item_name = "Big Table"
        i.seller = auser
        i.item_description = "wooden, large table for sale"
        i.item_price = "300"
        i.item_location = "uva"
        i.item_condition = 'NEW'
        i.item_categories = "FURNITURE"
        i.item_preferred_payment_method ="cash"
        i.save()

        i2 = Item()
        i2.item_name = "blue shirt"
        i2.seller = auser
        i2.item_description = "large  blue tshirt "
        i2.item_price = "100"
        i2.item_location = "uva"
        i2.item_condition = 'NEW'
        i2.item_categories = "CLOTHING"
        i2.item_preferred_payment_method ="venmo"
        i2.save()
    #8
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_filter(self):
        resp = self.client.get('/marketplace/advFilter/')
        self.assertEquals(resp.status_code, 200)
    #9
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_filter2(self):

        qs = Item.objects.all()
        f = ItemFilter(data = {'item_name': 'table'}, queryset = qs)
        count = 0
        for item in f.qs :
            count +=1
        self.assertEquals(count, 1)
    #10
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_filter3(self):
        resp = self.client.get('/marketplace/advFilter/')
        qs = Item.objects.all()
        f = ItemFilter(data = {'item_price__lt': '200'}, queryset = qs)
        count = 0
        for item in f.qs :
            count +=1
        self.assertEquals(count, 1)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_filter4(self):

        qs = Item.objects.all()
        f = ItemFilter(data = {'item_description': 'blue'}, queryset = qs)
        count = 0
        for item in f.qs :
            count +=1
        self.assertEquals(count, 1)


class detailTest(TestCase):
    #11
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_detail(self):
        i = Item()

        auser = User.objects.create_user('ch6yg', 'ch6yg@virginia.edu', 'password')
        auser.save()

        i.item_name = "Big Table"
        i.seller = auser
        i.item_description = "wooden, large table for sale"
        i.item_price = "100"
        i.item_location = "uva"
        i.item_condition = 'GOOD'
        i.item_categories = "FURNITURE"
        i.item_preferred_payment_method ="venmo"
        i.save()

        i2 = Item()
        i2.item_name = "Tshirt"
        i2.seller = auser
        i2.item_description = "large  blue tshirt "
        i2.item_price = "100"
        i2.item_location = "uva"
        i2.item_condition = 'GOOD'
        i2.item_categories = "CLOTHING"
        i2.item_preferred_payment_method ="venmo"
        i2.save()


        resp = self.client.get(reverse('marketplace:detail', args = (i.id,)))
        self.assertEquals(resp.status_code, 200)
        #self.assertContains(resp, 'table')
    #12
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_detail2(self):
        i = Item()


        auser = User.objects.create_user('ch6yg', 'ch6yg@virginia.edu', 'password')
        auser.save()

        i.item_name = "Big Table"
        i.seller = auser
        i.item_description = "wooden, large table for sale"
        i.item_price = "100"
        i.item_location = "uva"
        i.item_condition = 'GOOD'
        i.item_categories = "FURNITURE"
        i.item_preferred_payment_method ="venmo"
        i.save()

        i2 = Item()
        i2.item_name = "Tshirt"
        i2.seller = auser
        i2.item_description = "large  blue tshirt "
        i2.item_price = "100"
        i2.item_location = "uva"
        i2.item_condition = 'GOOD'
        i2.item_categories = "CLOTHING"
        i2.item_preferred_payment_method ="venmo"
        i2.save()
        resp = self.client.get(reverse('marketplace:detail', args = (i2.id,)))
        self.assertEquals(resp.status_code, 200)
        self.assertFalse('table' in resp)

class messageTest(TestCase):
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_message(self):
        auser = User.objects.create_user('ch6yg', 'ch6yg@virginia.edu', 'password')
        auser.save()
        user = User.objects.create_user('abc1ds', 'abc1ds@virginia.edu', 'password')
        m = Message()
        m.sender = auser
        m.receiver = user
        m.subject = 'hello'
        m.text = 'i want to buy'
        m.save()

        record = Message.objects.get(pk=1)
        self.assertEquals(record, m)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_messageOK(self):
        resp = self.client.get('/marketplace/message/')

        self.assertEquals(resp.status_code, 200)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_inbox(self):
        resp = self.client.get('/marketplace/inbox/')

        self.assertEquals(resp.status_code, 200)


class mapTest(TestCase):
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_map(self):
        resp = self.client.get('/marketplace/map/')
        self.assertEquals(resp.status_code, 200)

class logTest(TestCase):
    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_logout(self):
        auser = User.objects.create_user('ch6yg', 'ch6yg@virginia.edu', 'password')
        auser.save()
        resp = self.client.get('/marketplace/logout/')
        self.assertEquals(resp.status_code, 302) #redirected

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_profile(self):
        resp = self.client.get('/marketplace/profile/')
        self.assertEquals(resp.status_code, 200)

