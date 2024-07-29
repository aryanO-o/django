from django.db import models

# Create your models here.

class Category(models.Model):
    slug= models.SlugField(max_length=200, unique=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.title
