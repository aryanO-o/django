from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=50)
    cuisine = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name + ' - ' + self.cuisine + ' - ' + str(self.price) + '€'
