from django.db import models
from datetime import datetime
import os
from multiselectfield import MultiSelectField
from .choices import CATEGORIES, CONDITION_CHOICES, PAYMENT_METHODS
from django.conf import settings
from django.contrib.auth.models import User


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your models here.
class Seller(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    posRate=models.IntegerField(default=0)
    negRate=models.IntegerField(default=0)
    numTransactions = models.IntegerField(default=0)

class Item(models.Model):
    item_name = models.CharField (max_length=200)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item_description = models.CharField (max_length=1000)
    item_price = models.PositiveIntegerField(default=0)
    item_delivery = models.BooleanField(default=False)
    item_photo = models.ImageField(upload_to='media/', default = 'static/marketplace/default.png')
    item_location = models.CharField(max_length=200)
    item_preferred_payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS, default='venmo')
    item_condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, default='good')
    item_sold = models.BooleanField(default=False) #private for admins and seller
    item_categories = MultiSelectField(max_length=83, choices=CATEGORIES)
    item_add_date = models.DateTimeField('date published', default=datetime.now)
    latitude = models.FloatField(default=38.035618)
    longitude =  models.FloatField(default=-78.503415)
    def __str__(self):
        return self.item_name
