from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=256, blank=False, null=False)
    last_name = models.CharField(max_length=256, blank=False, null=False)
    birth_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    birth_place = models.CharField(max_length=256,blank=True, null=True)
    death_place = models.CharField(max_length=256,blank=True, null=True)

