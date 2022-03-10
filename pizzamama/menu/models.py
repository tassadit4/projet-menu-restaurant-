from django.db import models

# Create your models here.
from django.db.models import FloatField


class Pizza(models.Model):
    nom = models.CharField(max_length= 200)
    ingredients =models.CharField(max_length= 400)
    prix = models.FloatField(default=0)
    vegetarienne = models.BooleanField(default=False)
    note  = models.FloatField(default=0)
    emporte = models.BooleanField(default=False)
    def __str__(self):
        return self.nom
