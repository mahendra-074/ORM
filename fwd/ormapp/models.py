from django.db import models
from django.contrib import admin

class Swiggy(models.Model):
    sid = models.IntegerField()
    sname = models.CharField(max_length=100)
    price = models.IntegerField()
    restaurant = models.CharField(max_length=100)
    rating = models.FloatField()
    delivery_time = models.CharField(max_length=50)

class SwiggyAdmin(admin.ModelAdmin):
    list_display = ('sid', 'sname', 'price', 'restaurant', 'rating', 'delivery_time')