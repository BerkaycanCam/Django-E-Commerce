from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Brand(models.Model):
    brand=models.CharField(max_length=250)
    image=models.ImageField(upload_to="Brand Image")
    
    def __str__(self):
        return self.brand
    

class Gender(models.Model):
    gender=models.CharField( max_length=250)
    
    def __str__(self):
        return self.gender
    
    
class Color(models.Model):
    color=models.CharField( max_length=250)
    
    def __str__(self):
        return self.color
    
    
    
class CaseShape(models.Model):
    case_shape=models.CharField( max_length=250)  
    
    def __str__(self):
        return self.case_shape
    
    

class StrapType(models.Model):
    strap_type=models.CharField( max_length=250)
    def __str__(self):
        return self.strap_type
    
    
    
class GlassFeature(models.Model):
    glass_feature=models.CharField( max_length=250)
    
    def __str__(self):
     return self.glass_feature

   


class Style(models.Model):
    style=models.CharField( max_length=250)
    
    def __str__(self):
        return self.style



class Mechanism(models.Model):
    mechanism=models.CharField( max_length=250)
    
    def __str__(self):
        return self.mechanism



class Product(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    brand= models.ForeignKey(Brand, on_delete=models.CASCADE)
    model =models.CharField(max_length=250)
    description= models.TextField()
    image=models.ImageField(upload_to="Product Image")
    price= models.FloatField()
    gender=models.ForeignKey(Gender , on_delete=models.CASCADE)
    color=models.ForeignKey(Color, on_delete=models.CASCADE)
    case_shape= models.ForeignKey(CaseShape, on_delete=models.CASCADE)
    strap_type=models.ForeignKey(StrapType, on_delete=models.CASCADE) #kayış tipi
    glass_feature=models.ForeignKey(GlassFeature, on_delete=models.CASCADE)
    tarz=models.ForeignKey(Style, on_delete=models.CASCADE)
    mechanism=models.ForeignKey(Mechanism, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.model
    
    