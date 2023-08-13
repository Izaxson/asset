from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Biological(models.Model):
    DEPARTMENT_CHOICES = [
        ('CPSB', 'CPSB'),
        ('REVENUE', 'REVENUE SERVICES'),
        # Add more choices as needed
    ]
    AssetDescription = models.CharField(max_length=200)
    CategoryOfAsset = models.CharField(max_length=200)
    UnitOfMeasurement = models.IntegerField()  # (Pieces, acreage, etc)
    Quantity = models.IntegerField()
    Unitcost = models.IntegerField()
    FairValue = models.IntegerField()
    UsefulLife = models.IntegerField()  # in years
    AnnualDepreciation = models.IntegerField()#depreciation rate
    Responsible_officer=models.ForeignKey(User,on_delete=models.DO_NOTHING)#user model
    #ministry
    Department=models.CharField(max_length=200, choices=DEPARTMENT_CHOICES)
    Status=models.CharField(max_length=200) #dropdown
    Remarks = models.TextField(max_length=200)
      

    def __str__(self):
        return self.AssetDescription