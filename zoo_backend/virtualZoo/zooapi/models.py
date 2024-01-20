from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=50, unique=True)
    weight = models.DecimalField(max_digits=9, decimal_places=3)
    power = models.CharField(max_length=100)
    extinction_date = models.IntegerField(null=True, blank=True, help_text='Enter extinction date if animal extinct')

 