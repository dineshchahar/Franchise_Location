from django.db import models

class SourceLocation(models.Model):
    Source_lat = models.FloatField()
    Source_lon = models.FloatField()
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['Source_lat', 'Source_lon'], name='unique_source_location')
        ]
    def __str__(self):
        return f"lat:{self.Source_lat},long:{self.Source_lon}"
    
class Competitor(models.Model):
    # Burger king / KFC/pizza Hut/MacD/domino'z
    name = models.CharField(max_length=255)
    status= models.CharField(max_length=25,default='default')
    address = models.CharField(max_length=300)
    coordinates = models.TextField(max_length=300)
    types = models.TextField(max_length=500)
    rating = models.CharField(max_length=10)
    user_rating = models.CharField(max_length=10)
    Travel_Distance = models.CharField(max_length=10)
    Travel_Time = models.CharField(max_length=10)
    source_location = models.ForeignKey(SourceLocation,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return f"Name:{self.name},Address:{self.address},Coordinates:{self.coordinates},Types:{self.types},Rating:{self.rating},User_Rating:{self.user_rating},Travel_Distance:{self.Travel_Distance},Travel_Time:{self.Travel_Time}"
    
class SuperMarket(models.Model):
    # Mall / supermarket / vishal mega mart/ reliance digital/croma/D-mart/Trends/smart bazaar
    name = models.CharField(max_length=255)
    status= models.CharField(max_length=25,default='default')
    address = models.CharField(max_length=300)
    coordinates = models.TextField(max_length=300)
    types = models.TextField(max_length=500)
    rating = models.CharField(max_length=10)
    user_rating = models.CharField(max_length=10)
    Travel_Distance = models.CharField(max_length=10)
    Travel_Time = models.CharField(max_length=10)
    source_location = models.ForeignKey(SourceLocation,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return f"Name:{self.name},Address:{self.address},Coordinates:{self.coordinates},Types:{self.types},Rating:{self.rating},User_Rating:{self.user_rating},Travel_Distance:{self.Travel_Distance},Travel_Time:{self.Travel_Time}"

class PublicServices(models.Model):
    # School/ College/BUS stand/ Metro Station / university/Cinema/movie/multiplex
    name = models.CharField(max_length=255)
    status= models.CharField(max_length=25,default='default')
    address = models.CharField(max_length=300)
    coordinates = models.TextField(max_length=300)
    types = models.TextField(max_length=500)
    rating = models.CharField(max_length=10)
    user_rating = models.CharField(max_length=10)
    Travel_Distance = models.CharField(max_length=10)
    Travel_Time = models.CharField(max_length=10)
    source_location = models.ForeignKey(SourceLocation,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return f"Name:{self.name},Address:{self.address},Coordinates:{self.coordinates},Types:{self.types},Rating:{self.rating},User_Rating:{self.user_rating},Travel_Distance:{self.Travel_Distance},Travel_Time:{self.Travel_Time}"

class Hotels(models.Model):
    name = models.CharField(max_length=255)
    status= models.CharField(max_length=25,default='default')
    address = models.CharField(max_length=300)
    coordinates = models.TextField(max_length=300)
    types = models.TextField(max_length=500)
    rating = models.CharField(max_length=10)
    user_rating = models.CharField(max_length=10)
    Travel_Distance = models.CharField(max_length=10)
    Travel_Time = models.CharField(max_length=10)
    source_location = models.ForeignKey(SourceLocation,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return f"Name:{self.name},Address:{self.address},Coordinates:{self.coordinates},Types:{self.types},Rating:{self.rating},User_Rating:{self.user_rating},Travel_Distance:{self.Travel_Distance},Travel_Time:{self.Travel_Time}"

class Residentials(models.Model):
    name = models.CharField(max_length=255)
    status= models.CharField(max_length=25,default='default')
    address = models.CharField(max_length=300)
    coordinates = models.TextField(max_length=300)
    types = models.TextField(max_length=500)
    rating = models.CharField(max_length=10)
    user_rating = models.CharField(max_length=10)
    Travel_Distance = models.CharField(max_length=10)
    Travel_Time = models.CharField(max_length=10)
    source_location = models.ForeignKey(SourceLocation,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return f"Name:{self.name},Address:{self.address},Coordinates:{self.coordinates},Types:{self.types},Rating:{self.rating},User_Rating:{self.user_rating},Travel_Distance:{self.Travel_Distance},Travel_Time:{self.Travel_Time}"
class Retails(models.Model):
    name = models.CharField(max_length=255)
    status= models.CharField(max_length=25,default='default')
    address = models.CharField(max_length=300)
    coordinates = models.TextField(max_length=300)
    types = models.TextField(max_length=500)
    rating = models.CharField(max_length=10)
    user_rating = models.CharField(max_length=10)
    Travel_Distance = models.CharField(max_length=10)
    Travel_Time = models.CharField(max_length=10)
    source_location = models.ForeignKey(SourceLocation,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return f"Name:{self.name},Address:{self.address},Coordinates:{self.coordinates},Types:{self.types},Rating:{self.rating},User_Rating:{self.user_rating},Travel_Distance:{self.Travel_Distance},Travel_Time:{self.Travel_Time}"

class Restaurants(models.Model):
    name = models.CharField(max_length=255)
    status= models.CharField(max_length=25,default='default')
    address = models.CharField(max_length=300)
    coordinates = models.TextField(max_length=300)
    types = models.TextField(max_length=500)
    rating = models.CharField(max_length=10)
    user_rating = models.CharField(max_length=10)
    Travel_Distance = models.CharField(max_length=10)
    Travel_Time = models.CharField(max_length=10)
    source_location = models.ForeignKey(SourceLocation,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return f"Name:{self.name},Address:{self.address},Coordinates:{self.coordinates},Types:{self.types},Rating:{self.rating},User_Rating:{self.user_rating},Travel_Distance:{self.Travel_Distance},Travel_Time:{self.Travel_Time}"

class Education(models.Model):
    name = models.CharField(max_length=255)
    status= models.CharField(max_length=25,default='default')
    address = models.CharField(max_length=300)
    coordinates = models.TextField(max_length=300)
    types = models.TextField(max_length=500)
    rating = models.CharField(max_length=10)
    user_rating = models.CharField(max_length=10)
    Travel_Distance = models.CharField(max_length=10)
    Travel_Time = models.CharField(max_length=10)
    source_location = models.ForeignKey(SourceLocation,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return f"Name:{self.name},Address:{self.address},Coordinates:{self.coordinates},Types:{self.types},Rating:{self.rating},User_Rating:{self.user_rating},Travel_Distance:{self.Travel_Distance},Travel_Time:{self.Travel_Time}"
class Tourist(models.Model):
    name = models.CharField(max_length=255)
    status= models.CharField(max_length=25,default='default')
    address = models.CharField(max_length=300)
    coordinates = models.TextField(max_length=300)
    types = models.TextField(max_length=500)
    rating = models.CharField(max_length=10)
    user_rating = models.CharField(max_length=10)
    Travel_Distance = models.CharField(max_length=10)
    Travel_Time = models.CharField(max_length=10)
    source_location = models.ForeignKey(SourceLocation,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return f"Name:{self.name},Address:{self.address},Coordinates:{self.coordinates},Types:{self.types},Rating:{self.rating},User_Rating:{self.user_rating},Travel_Distance:{self.Travel_Distance},Travel_Time:{self.Travel_Time}"
