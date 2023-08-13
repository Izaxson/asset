from django.db import models
from django.contrib.auth.models import User

class Investments(models.Model):
    SOURCE_CHOICES = [
        ('Donor_Funds', 'Donor Funds'),
        ('Development Fund', 'Development Fund'),
        # Add more choices as needed
    ]
    DEPARTMENT_CHOICES = [
        ('CPSB', 'CPSB'),
        ('REVENUE', 'REVENUE SERVICES'),
        # Add more choices as needed
    ]
    TypeOfInvestments =models.CharField(max_length=200)#-choice field
    InstitutionInvestmentHeld =models.CharField(max_length=200)
    DocumentOfOwnership= models.CharField(max_length=200)
    SourceOfFunds=models.CharField(max_length=200, choices=SOURCE_CHOICES)
    DateOfInvestment =models.DateField() 
    MaturityDate=models.DateField()
    DurationOfInvestment=models.IntegerField()# in months/years
    InterestRate=models.IntegerField() # applicable to the investment
    Quantity=models.IntegerField() 
    Unitcost=models.IntegerField () 
    InitialCostOfpurchase=models.IntegerField() 
    Expectedinterest =models.IntegerField()# due on maturity
    MaturityValue=models.IntegerField()
    Responsible_officer=models.ForeignKey(User,on_delete=models.DO_NOTHING)#user model
    Department=models.CharField(max_length=200, choices=DEPARTMENT_CHOICES)
    def __str__(self):
            return self.TypeOfInvestments 
