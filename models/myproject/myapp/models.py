from django.db import models

# Create your models here.
class MenuItems(models.Model):
    itemname = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    year = models.IntegerField()