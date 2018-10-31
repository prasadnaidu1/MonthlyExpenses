from django.db import models

# Create your models here.
class friends(models.Model):
    expenses=models.CharField(max_length=50)
    date=models.DateField()
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    members=models.CharField(max_length=150)
    res=models.IntegerField(default=10)
class showdetails(models.Model):
    exp=models.CharField(max_length=50)
    start=models.DateField()
    end=models.DateField()  
