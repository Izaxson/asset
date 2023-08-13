from django.db import models
from django.contrib.auth.models import User
class StandardAsset(models.Model):
    Asset_Class_choice= [
      ('ICT_Computer_equipment', 'ICT/Computer Equipment'),
      ('Furniture', 'Furniture'),
      ('Fittings', 'Fittings'),
      ('Plant_Machinery', 'Plant & Machinery'),
      ('Portable_Attractive', 'Portable and Attractive'),
                
    ]
    DEPARTMENT_CHOICES = [
        ('CPSB', 'CPSB'),
        ('REVENUE', 'REVENUE SERVICES'),
        # Add more choices as needed
    ]

    Asset_Name=models.CharField(max_length=200)
    Asset_Class = models.CharField(max_length=100,choices=Asset_Class_choice)
    Financed_By=models.CharField(max_length=200)
    Serial_Number =models.CharField(max_length=200)
    Tag_Number=models.CharField(max_length=200)#auto genearte using django tags , 
    Make_Model=models.CharField(max_length=200) 
    Date_of_Delivery=models.DateTimeField(max_length=200) 
    PV_Number=models.CharField(max_length=200)
    Original_Location =models.CharField(max_length=200,choices=DEPARTMENT_CHOICES)#dept
    Current_Location=models.CharField(max_length=200,choices=DEPARTMENT_CHOICES)#dept
    Replacement_Date=models.DateTimeField(max_length=200) 
    Purchase_Amount=models.CharField(max_length=200) 
    Depreciation_rate=models.IntegerField() 
    Annual_depreciation=models.IntegerField() 
    Date_of_disposal=models.DateField(max_length=200) 
    Disposal_value=models.IntegerField() 
    Responsible_officer=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    Department=models.CharField(max_length=200,choices=DEPARTMENT_CHOICES)
    Asset_condition=models.CharField(max_length=200)
    Asset_Description =models.TextField(max_length=200)              

    def __str__(self):
            return self.Asset_Name
