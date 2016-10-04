from django.db import models
from rest_framework import serializers
# Create your models here.


class EPS(models.Model):
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre
# Serializable


class EPSSerializable(serializers.ModelSerializer):
    class Meta:
        model = EPS
        fields = ('nombre', 'codigo', )
