from django.db import models

# Create your models here.
class plant(models.Model):
    nm=models.CharField(max_length=30)
    em=models.CharField(max_length=30)
    mo=models.CharField(max_length=30)
    ps=models.CharField(max_length=30)
    cps=models.CharField(max_length=30)   
    
    
class fedback(models.Model):
    name=models.CharField(max_length=30,default=" ")
    email=models.CharField(max_length=30,default=" ")
    fed=models.CharField(max_length=200,default=" ")
    
class address(models.Model):
    email = models.CharField(max_length=30,default=" ")
    add = models.CharField(max_length=200,default=" ")
    
class PlantInfo(models.Model):
    name=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    stock=models.CharField(max_length=50)  
    status=models.CharField(max_length=50)  
    