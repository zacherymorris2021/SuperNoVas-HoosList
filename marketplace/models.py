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
    item_price = models.IntegerField(default=0)
    item_delivery = models.BooleanField(default=False)
    item_photo = models.ImageField(upload_to='media/', default = 'static/marketplace/default.png')
    item_preferred_payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS, default='venmo')
    item_condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, default='good')
    item_sold = models.BooleanField(default=False) #private for admins and seller
    item_categories = models.CharField(max_length=100, choices=CATEGORIES)
    item_add_date = models.DateTimeField('date published', default=datetime.now)
    latitude = models.FloatField(default=38.035618)
    longitude =  models.FloatField(default=-78.503415)
    def __str__(self):
        return self.item_name


class RatingInfo(models.Model):
    seller = models.ForeignKey(Seller, on_delete = models.CASCADE)
    info_field = models.CharField (max_length=200)
    count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.seller.seller_name+"\'s "+self.info_field+" votes"



class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = "sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = "receiver", on_delete=models.CASCADE)
    subject = models.CharField(max_length = 75)
    text = models.CharField(max_length = 2500)
    timesent = models.DateTimeField('time sent', default=datetime.now)

    def __str__(self):
        return self.subject

