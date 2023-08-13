from django.db import models
from django.contrib.auth.models import User



class Stocks_Consumables(models.Model):
    Department = (
            ('CPSB', 'CPSB'),
            ('REVENUE', 'REVENUE SERVICES'),
            # Add more choices as needed
    )    
    Description = models.CharField(max_length=200)
    Unit = models.CharField(max_length=200)  # e.g. piece, Kgs, etc.
    Quantity = models.IntegerField()
    UnitCost = models.IntegerField()
    Responsible_officer=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    Department=models.CharField(max_length=200,choices=Department)
    Remarks = models.CharField(max_length=200)

    def __str__(self):
            return self.Description    