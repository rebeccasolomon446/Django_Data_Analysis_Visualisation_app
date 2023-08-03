from django.db import models

# Create your models here.

# single source of information about the data
# instantiated in views.py and added to the db
class Data(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    rent = models.IntegerField()
    emi = models.IntegerField()
    tax = models.IntegerField()
    exp = models.IntegerField()
    expenses_monthly = models.IntegerField(default=0)
    income_monthly = models.IntegerField(default=0)