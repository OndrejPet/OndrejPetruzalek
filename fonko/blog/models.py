from django.db import models

# Create your models here.
class brug(models.Model):
    nahodne_policko = models.CharField(max_length=200, default="x")
    title = models.CharField(max_length=200,default="x")

