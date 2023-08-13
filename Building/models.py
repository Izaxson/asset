from django.db import models
from django.contrib.auth.models import User

class Building(models.Model):
  CATEGORY_CHOICES = [
        ('Building', 'Building'),
        ('Investment Property', 'Investment Property'),
        # Add more choices as needed
    ]
  
  OWNERSHIP_CHOICES = [
        ('Freehold', 'Freehold'),
        ('Leasehold', 'Leasehold'),
        
    ]
  DEPARTMENT_CHOICES = [
        ('CPSB', 'CPSB'),
        ('REVENUE', 'REVENUE SERVICES'),
        # Add more choices as needed
    ]
  TYPE_CHOICES = [
        ('Permanent', 'Permanent'),
        ('Temporary', 'Temporary'),
        # Add more choices as needed
    ]
  SOURCE_CHOICES = [
        ('Donor_Funds', 'Donor Funds'),
        ('Development Fund', 'Development Fund'),
        # Add more choices as needed
    ]
  Description=models.TextField(max_length=200) #Name of building
  BuildingOwnership=models.CharField(max_length=200) 
  Category = models.CharField(max_length=200, choices=CATEGORY_CHOICES)
  BuildingNo=models.CharField(max_length=200) 
  InstitutionNo=models.CharField(max_length=200)
  NearestTown=models.CharField(max_length=200)# Shopping centre
  Street=models.CharField(max_length=200)
  County = models.CharField(max_length=200, default='Mandera')
  LRNo=models.CharField(max_length=200) 
  SizeOfLand=models.IntegerField #in  (ha)
  OwnershipStatus=models.CharField(max_length=200, choices=OWNERSHIP_CHOICES)
  SourceOfFunds=models.CharField(max_length=200, choices=SOURCE_CHOICES)
  ModeOfAcquisition=models.CharField(max_length=200)#-choice field
  DateOfPurchase=models.DateField # Building commisssioning (for constructed buildings)
  TypeOfBuilding=models.CharField(max_length=200, choices=TYPE_CHOICES)# (Permanent/ temporary)-choice field
  DesignatedUse=models.CharField(max_length=200)
  EstimatedUsefulLife=models.IntegerField()# in years
  NumberOfFloors=models.IntegerField()
  PlinthArea=models.CharField(max_length=200)
  CostOfConstruction=models.CharField(max_length=200)# Valuation
  Responsible_officer=models.ForeignKey(User,on_delete=models.DO_NOTHING)#user model
  Department=models.CharField(max_length=200, choices=DEPARTMENT_CHOICES)
  Status=models.CharField(max_length=200) 
  Remarks = models.TextField(max_length=200)

  def __str__(self):
            return self.Location 
