from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MotorVehicle(models.Model):
    DEPARTMENT_CHOICES = [
        ('CPSB', 'CPSB'),
        ('REVENUE', 'REVENUE SERVICES'),
        # Add more choices as needed
    ]
    VehicleRegistrationNo=models.CharField(max_length=20)     
    EngineNo=models.CharField(max_length=200)
    ChassisNo=models.CharField(max_length=200)
    DateOfDisposal=models.DateField(max_length=200)
    Financed_By=models.CharField(max_length=200)
    Serial_Number =models.CharField(max_length=200)
    Tag_Number=models.CharField(max_length=200)
    MakeModel=models.CharField(max_length=200) 
    Date_of_Delivery=models.DateTimeField(max_length=200) 
    PVNumber=models.CharField(max_length=200)
    Original_Location =models.CharField(max_length=200, choices=DEPARTMENT_CHOICES)
    Current_Location=models.CharField(max_length=200, choices=DEPARTMENT_CHOICES)
    YearOfPurchase=models.DateField(max_length=200) 
    Replacement_Date=models.DateField(null=True, blank=True)
    Purchase_Amount=models.CharField(max_length=200) 
    Depreciation_rate=models.IntegerField() 
    Annual_depreciation=models.IntegerField() 
    Accumulated_depreciation=models.IntegerField() 
    DateOfDisposal=models.DateField(max_length=200) 
    Disposal_Value=models.IntegerField() #value
    Responsible_officer=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    Department=models.CharField(max_length=200, choices=DEPARTMENT_CHOICES)
    Assetcondition=models.CharField(max_length=200)
    AssetDescription =models.TextField(max_length=200)     
    Notes=models.CharField(max_length=200)         

    def __str__(self):
            return self.VehicleRegistrationNo  