from django.db import models

# Create your models here.


class EPS(models.Model):
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=10)
