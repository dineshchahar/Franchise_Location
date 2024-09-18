from django.db import models

class SourceLocation(models.Model):
    Source_lat = models.FloatField(max_length=100)
    Source_lon = models.FloatField(max_length=100)
    


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=300)
    coordinates = models.TextField(max_length=300)
    types = models.TextField(max_length=500)
    rating = models.FloatField(max_length=10)
    user_rating = models.FloatField(max_length=10)
    Distance = models.FloatField(max_length=10)
