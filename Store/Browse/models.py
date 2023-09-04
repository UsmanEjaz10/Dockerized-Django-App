from django.db import models

# Create your models here.
class Department(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 200)

class Employee(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length = 15, blank = False , null =False )
    department = models.CharField(max_length=200)
    
