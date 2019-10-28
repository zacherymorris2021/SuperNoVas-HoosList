from django.contrib import admin
from .models import Seller, Item, RatingInfo

# Register your models here.
admin.site.register(Seller)
admin.site.register(Item)
admin.site.register(RatingInfo)
