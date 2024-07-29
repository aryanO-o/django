from django.db import models


# Create your models here.
class Logger(models.Model):
    first_name = models.CharField(verbose_name='First Name', max_length=100)
    last_name = models.CharField(verbose_name='Last Name', max_length=100)
    time_log = models.TimeField(help_text='Enter the time you want to log')
