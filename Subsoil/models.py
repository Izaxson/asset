from django.db import models
from django.contrib.auth.models import User
class SubsoilAssets(models.Model):
    DEPARTMENT_CHOICES = [
          ('CPSB', 'CPSB'),
          ('REVENUE', 'REVENUE SERVICES'),
          # Add more choices as needed
      ]
    Location =models.CharField(max_length=200)
    MineralType=models.CharField(max_length=200)#  (Diamond, gold, copper etc)
    UnitOfMeasurement=models.CharField(max_length=200)  #(Pieces, acreage etc)
    Quantity=models.CharField(max_length=200) 
    MonetaryValue=models.IntegerField() 
    UsefulLife=models.IntegerField() #in years
    Annual_depreciation=models.IntegerField() 
    Responsible_officer=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    Department=models.CharField(max_length=200,choices=DEPARTMENT_CHOICES)  
    AssetDescription=models.TextField(max_length=200) 
    Remarks=models.TextField(max_length=200)
        
    def __str__(self):
                return self.Location  
