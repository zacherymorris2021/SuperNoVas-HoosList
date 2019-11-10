from django.db import models
from datetime import datetime
import os
from multiselectfield import MultiSelectField
from .choices import CATEGORIES, CONDITION_CHOICES, PAYMENT_METHODS

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your models here.
class Seller(models.Model):
    seller_name = models.CharField (max_length = 50)
    seller_computing_id = models.CharField(max_length=7, default="")
    num_transactions = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.seller_name

class Item(models.Model):
    item_name = models.CharField (max_length=200)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    item_description = models.CharField (max_length=1000)
    item_price = models.PositiveIntegerField(default=0)
    item_delivery = models.BooleanField(default=False)
    item_photo = models.ImageField(upload_to=os.path.join(BASE_DIR, 'media/'), default = os.path.join(BASE_DIR, 'static/marketplace/default.png'))
    item_location = models.CharField(max_length=200)
    item_preferred_payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS, default='venmo')
    item_condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, default='good')
    item_sold = models.BooleanField(default=False) #private for admins and seller
    item_categories = MultiSelectField(max_length=75, choices=CATEGORIES)
    item_add_date = models.DateTimeField('date published', default=datetime.now)
    def __str__(self):
        return self.item_name

class RatingInfo(models.Model):
    seller = models.ForeignKey(Seller, on_delete = models.CASCADE)
    info_field = models.CharField (max_length=200)
    count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.seller.seller_name+"\'s "+self.info_field+" votes"

class Conversation(models.Model):
    message = models.CharField(max_length = 1000)
    time_sent = models.DateTimeField('time sent', default= datetime.now)
    sender = models.ForeignKey(Seller, on_delete = models.CASCADE)
