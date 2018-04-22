from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name

class From(models.Model):
    name = models.ForeignKey(Location, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.name  
    
class To(models.Model):
    name = models.ForeignKey(Location, on_delete=models.CASCADE)   
    
    def __str__(self):
        return self.name    

class RouteDetails(models.Model):
    routeDistance = models.IntegerField()
    routeFromId = models.ForeignKey(From, on_delete=models.CASECADE)
    routeToId = models.ForeignKey(To, on_delete=models.CASECADE)
     
class Bus(models.Model):
    bus_no = models.CharField(max_length=10)
    route = models.ManyToManyField(RouteDetails)
    from_loacation = models.ForeignKey(From, on_delete= models.CASCADE)
    to_loacation = models.ForeignKey(To, on_delete= models.CASCADE)
    
    
