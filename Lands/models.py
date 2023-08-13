from django.db import models
from django.contrib.auth.models import User
class Land(models.Model):
  ModeOfAcquisition = [
        ('Purchase', 'Purchase'),
        ('Transfer', 'Transfer'),
        ('Donation', 'Donation'),
        # Add more choices as needed
    ]
  CategoryOfLand = [
        ('Land', 'Land'),
        ('Investment', 'Investment'),
        
        # Add more choices as needed
    ]
  DocumentOfOwnership = [
        ('Title Deed', 'Title Deed'),
        ('Certificate', 'Certificate'),
        ('Allotment Letter', 'Allotment Letter'),
        
        # Add more choices as needed
    ]
  OWNERSHIP_CHOICES = [
        ('Freehold', 'Freehold'),
        ('Leasehold', 'Leasehold'),
        
    ]
  Statuschoice= [
    ('Disputed','Disputed'),
    ('Undisputed','Undisputed'),
  ]
  PlanningStatus= [
    ('Planned','Planned'),
    ('Unplanned','Unplanned'),
  ]
  SurveyStatus= [
    ('Surveyed','Surveyed'),
  ]
  LandIndex= [
    ('Fair_Value','Fair Value'),
    ('Ministry_Zonal_Map','Ministry Zonal Map'),
     ('Land_Index','Land Index'),
  ]
  DEPARTMENT_CHOICES = [
        ('CPSB', 'CPSB'),
        ('REVENUE', 'REVENUE SERVICES'),
        # Add more choices as needed
    ]
  ModeOfAcquisition=models.CharField(max_length=200, choices=ModeOfAcquisition) #e.g. choice field -purchase, transfer, donation etc.
  CategoryOfLand=models.CharField(max_length=200, choices=CategoryOfLand)# choice field (Land or investment property)
  County=models.CharField(max_length=200) #default mandera -choice 
  Nearest_Location=models.CharField(max_length=200)
  GPS=models.CharField(max_length=200)
  Polygon=models.CharField(max_length=200)
  LRCertifcateNo=models.CharField(max_length=200)
  DocumentOfOwnership=models.CharField(max_length=200,choices=DocumentOfOwnership)# held (Title deed, certificate, allotment letter, etc.)
  OwnershipDetails=models.CharField(max_length=200) # as per document of title
  Size=models.IntegerField()  #(ha)
  OwnershipStatus=models.CharField(max_length=200,choices=OWNERSHIP_CHOICES) # (Freehold /leasehold)
  AcquisitionDate=models.DateField(max_length=200) 
  RegistrationDate=models.DateField(max_length=200) 
  Status=models.CharField(max_length=200,choices=Statuschoice)# Disputed/ Undisputed
  Encumberances=models.CharField(max_length=200)
  PlanningStatus=models.CharField(max_length=200,choices=PlanningStatus)#Planned/ Unplanned
  UseOfLand=models.CharField(max_length=200)
  SurveyStatus=models.CharField(max_length=200,choices=SurveyStatus)#Surveyed/ Not surveyed
  AcquisitionAmount=models.IntegerField() 
  LandIndex=models.CharField(max_length=200,choices=LandIndex)#Fair value/ Ministry of Lands zonal maps or land index
  DisposalDate=models.DateField(max_length=200) 
  ChangeOfUseDate=models.DateField(max_length=200) 
  DisposalValue=models.IntegerField() 
  AnnualRentalIncome=models.IntegerField() # (for investment property)
  DescriptionOfLand=models.TextField(max_length=200) 
  Responsible_officer=models.ForeignKey(User,on_delete=models.DO_NOTHING)
  Department=models.CharField(max_length=200, choices=DEPARTMENT_CHOICES)
  Remarks=models.TextField(max_length=200)
 

  def __str__(self):
            return self.LRCertifcateNo