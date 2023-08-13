from django.db import models

# Create your models here.
class Railway(models.Model):
    Description=models.CharField(max_length=200) 
    RailwayID=models.CharField(max_length=200) 
    Length=models.IntegerField() 
    DateOfCommissioning=models.DateField(max_length=200) 
    TypeOfRail=models.CharField(max_length=200) 
    AmenitiesAvailable=models.CharField(max_length=200) 
    LandRegistryID=models.CharField(max_length=200) 
    UsefulLife=models.CharField(max_length=200) 
    Cost=models.CharField(max_length=200) 
    AnnualDepreciation=models.IntegerField() 
    Remarks=models.TextField(max_length=200) 
    def __str__(self):
            return self.RailwayID 