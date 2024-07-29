from django.db import models

# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField('Phone Number', max_length=100)
    time = models.TimeField('Time of Reservation')
    count = models.IntegerField('Number of People')
    notes = models.TextField('Special Requests', blank=True, max_length=200)

    def __str__(self):
        return self.name
