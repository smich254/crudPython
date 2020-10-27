from django.db import models

# Create your models here.

class Correo(models.Model):
    correo=models.CharField(max_length=50)
