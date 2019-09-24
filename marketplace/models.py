from django.db import models
from datetime import datetime
from multiselectfield import MultiSelectField

#default choice values
PAYMENT_METHODS = (
    ('venmo', 'VENMO'),
    ('cash', 'CASH'),
    ('check', 'CHECK'),
    ('paypal', 'PAYPAL'),
    ('applePay', 'APPLEPAY'),
    ('none', 'NONE'),
    ('other', 'OTHER')
)
CONDITION_CHOICES = (
    ('new', 'NEW'),
    ('like new', 'LIKE NEW'),
    ('very good', 'VERY GOOD'),
    ('good', 'GOOD'),
    ('acceptable', 'ACCEPTABLE')
)
CATEGORIES = (
    ('furniture', 'FURNITURE'),
    ('textbooks', 'TEXTBOOKS'),
    ('clothing', 'CLOTHING'),
    ('class supplies', 'CLASS SUPPLIES'),
    ('kitchen', 'KITCHEN'),
    ('dorm', 'DORM'),
    ('uva gear', 'UVA GEAR'),
    ('electronics', 'ELECTRONICS'),
    ('other', 'OTHER')
)


# Create your models here.
class Seller(models.Model):
    seller_name = models.CharField (max_length = 50)
    seller_computing_id = models.CharField(max_length=7, default="")
    def __str__(self):
        return self.seller_name

class Item(models.Model):
    item_name = models.CharField (max_length=200)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    item_description = models.CharField (max_length=1000)
    item_price = models.PositiveIntegerField(default=0)
    item_delivery = models.BooleanField(default=False)
    #needs a picture field. Look this up.
    item_location = models.CharField(max_length=200)
    item_preferred_payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS, default='venmo')
    item_condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, default='good')
    item_sold = models.BooleanField(default=False) #private for admins and seller
    item_categories = MultiSelectField(max_length=75, choices=CATEGORIES)
    item_add_date = models.DateTimeField('date published', default=datetime.now)
    def __str__(self):
        return self.item_name
